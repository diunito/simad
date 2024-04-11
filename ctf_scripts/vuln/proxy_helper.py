import docker
import json
import requests
import os
import glob
import logging
import yaml

# global array with services yml
services = []
all_ports = []

logging.basicConfig(level=logging.INFO, filename="proxy_helper.logs", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")


def compose_backup(compose_file):
    # create file docker-compose.yml.bak for each docker-compose.yml on same folder
    with open(compose_file, 'r') as file:
        lines = file.readlines()
        with open(compose_file + '.bak', 'w') as file2:
            file2.writelines(lines)
    logging.info('[+] Created backup for docker-compose.yml file')


def create_service(dock, host, serv):
    i = 0
    for i in range(len(host)):
        service = {
                "name": dock + '_' + str(i),
                "target_ip": dock,
                "target_port": int(serv[i]),
                "listen_port": int(host[i])
            }
        try:
            r = requests.get('http://localhost:' + str(host[i]))
            logging.info('[+] http://localhost:' + str(host[i]) + ' status code:' + str(r.status_code))
            if r.status_code == 200:
                service['http'] = True
        except Exception as e:
            logging.error(e)
            service['http'] = False
        services.append(service)
        logging.info('[+] Added service: ' + dock + " - port: " + host[i] + ' to config.json') 
    pass
   
   
def add_network(file): 
    text_to_add = '''

networks:
  default:
    name: ctf_network
    external: true'''
    
    with open(file, 'a') as file:
        file.write(text_to_add)
    
def get_docker_services(folders):
    pass
    for folder in folders:
        # if docker-compose.yaml exists rename it to docker-compose.yml
        if os.path.isfile(folder + '/docker-compose.yaml'):
            os.rename(folder + '/docker-compose.yaml', folder + '/docker-compose.yml')
            logging.info('[+] Renamed docker-compose.yaml to docker-compose.yml in folder: ' + folder)
                    
        # open docker-compose.yml file
        with open(folder + '/docker-compose.yml', 'r') as file:
            docker_config = yaml.load(file, Loader=yaml.FullLoader)
            # get all services names
            services_names = list(docker_config['services'].keys())
            # get all ports for each service
            for service in services_names:
                # get ports
                try:
                    ports = docker_config['services'][service]['ports']
                    ser_ports = []
                    host_ports = []
                    for i in range(len(ports)):
                        if len(ports[i].split(':')) > 2:
                            host_ports.append(ports[i].split(':')[1])
                            ser_ports.append(ports[i].split(':')[2])
                            all_ports.append(ports[i].split(':')[1])
                        else:
                            host_ports.append(ports[i].split(':')[0])
                            ser_ports.append(ports[i].split(':')[1])
                            all_ports.append(ports[i].split(':')[0])
                    create_service(service, host_ports, ser_ports)
                except Exception as err:  
                    logging.error(err)
                    pass        

def create_json():
    glbal_conf = {
        
        "keyword": "BLOCKED",
        "verbose": False,
        "dos": {
            "enabled": False,
            "duration": 60,
            "interval": 2
        },
        "max_stored_messages": 10,
        "max_message_size": 65535
    }
    
    data = {
        "services": services,
        "global_config": glbal_conf
    } 

    return json.dumps(data, indent=4)    


def remove_ports(compose):
    with open(compose, 'r') as file:
        docker_config = yaml.load(file, Loader=yaml.FullLoader)
        # get services names
        services_names = docker_config['services'].keys()
        # convert to list
        services_names = list(services_names)
        for service in services_names:
            try:
                del docker_config['services'][service]['ports']
            except Exception as err:
                logging.error(err)
                pass
    with open(compose, 'w') as file:
        yaml.dump(docker_config, file, default_flow_style=False)

def edit_compose(folder):
    logging.info('[+] Start editing docker-compose.yml files')
    compose_files = glob.glob(os.path.join(folder, '**/docker-compose.yml'), recursive=True)
    compose_files = [x for x in compose_files if 'ctf_proxy' not in x]
    compose_files = [x for x in compose_files if 'old' not in x]
    
    for compose_file in compose_files:
        compose_backup(compose_file)
        remove_ports(compose_file)
        add_network(compose_file)
    
    logging.info('[+] Finished editing docker-compose.yml files')

def update_proxy_compose(fodler):
    logging.info('[+] Start editing docker-compose.yml file for proxy')
    with open('./ctf_proxy/docker-compose.yml', 'r') as file:
        docker_config = yaml.load(file, Loader=yaml.FullLoader)
        # edit ports of service proxy
        re_port = []
        for port in all_ports:
            re_port.append(port + ':' + port)
        # add port 80 and 443 if not present
        if '80:80' not in re_port:
            re_port.append('80:80')
        if '443:443' not in re_port:
            re_port.append('443:443')
        docker_config['services']['proxy']['ports'] = re_port
        # update file
    with open('./ctf_proxy/docker-compose.yml', 'w') as file:
        yaml.dump(docker_config, file, default_flow_style=False)
    logging.info('[+] Finished editing docker-compose.yml file for proxy')
        
        

def very_important_print():
    # ascii art
    print("""\
        
         ___       ________  ________      ___    ___      ________  ________  ________     ___    ___ ___    ___ 
        |\  \     |\   __  \|\_____  \    |\  \  /  /|    |\   __  \|\   __  \|\   __  \   |\  \  /  /|\  \  /  /|
        \ \  \    \ \  \|\  \\|___/  /|   \ \  \/  / /    \ \  \|\  \ \  \|\  \ \  \|\  \  \ \  \/  / | \  \/  / /
         \ \  \    \ \   __  \   /  / /    \ \    / /      \ \   ____\ \   _  _\ \  \\\  \  \ \    / / \ \    / / 
          \ \  \____\ \  \ \  \ /  /_/__    \/  /  /        \ \  \___|\ \  \\  \\ \  \\\  \  /     \/   \/  /  /  
           \ \_______\ \__\ \__\\________\__/  / /           \ \__\    \ \__\\ _\\ \_______\/  /\   \ __/  / /    
            \|_______|\|__|\|__|\|_______|\___/ /             \|__|     \|__|\|__|\|_______/__/ /\ __\\___/ /     
                                         \|___|/                                           |__|/ \|__\|___|/      
                                                                                                          
                                                                                                          
        
        """)

if __name__ == "__main__":
    
    very_important_print()
    
    # start logging namee file logfile+timestamp
    logging.info("Start logging")
    
    # get all subfolders
    subfolders = [f.path for f in os.scandir('.') if f.is_dir() ]
    logging.info('[+] Get all subfolders')
    # remove all folders that start with .
    subfolders = [x for x in subfolders if not x.startswith('./.')]
    # remove all folders that end with ctf_proxy
    subfolders = [x for x in subfolders if not x.endswith('ctf_proxy')]
    subfolders = [x for x in subfolders if 'old' not in x]

    data = get_docker_services(subfolders)
    
    json_data = create_json()
    logging.info('[+] Created data for config.json file')
    
    ## write data on config.json
    with open('./ctf_proxy/proxy/config/config.json', 'w') as outfile:
        outfile.write(json_data)
    logging.info('[+] Updated config.json file with new containers')


    ## edit docker-compose.yml files
    main_folder = os.getcwd()
    edit_compose(main_folder)
    
    update_proxy_compose(main_folder)