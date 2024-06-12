#!/usr/bin/python3

import os
import sys
import json
import shutil

from pathlib import Path, PosixPath

import ruamel.yaml  # pip install ruamel.yaml

"""
Why not just use the included yaml package?
Because this one preservs order and comments (and also allows adding them)
"""

blacklist = ["remote_pcap_folder", "caronte", "tulip", "ctf_proxy"]

yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True
yaml.indent(sequence=3, offset=1)

dirs: list[PosixPath] = []
services_dict = {}


class WrongArgument(Exception):
    pass


def parse_dirs():
    """
    If the user provided arguments use them as paths to find the services.
    If not, iterate through the directories and ask for confirmation
    """
    global dirs

    if sys.argv[1:]:
        for dir in sys.argv[1:]:
            d = Path(dir)
            if not d.exists():
                raise WrongArgument(f"The path {dir} doesn't exist")
            if not d.is_dir():
                raise WrongArgument(f"The path {dir} is not a directory")
            dirs.append(d)
    else:
        print(f"No arguments were provided; automatically scanning for services.")
        for file in Path(".").iterdir():
            if file.is_dir() and file.stem[0] != "." and file.stem not in blacklist:
                if "y" in input(f"Is {file.stem} a service? [y/N] "):
                    dirs.append(Path(".", file))

def parse_services():
    """
    If services.json is present, load it into the global dictionary.
    Otherwise, parse all the docker-compose yamls to build the dictionary and
    then save the result into services.json
    """
    global services_dict, dirs

    for service in dirs:
        file = Path(service, "docker-compose.yml")
        if not file.exists():
            file = Path(service, "docker-compose.yaml")

        with open(file, "r") as fs:
            ymlfile = yaml.load(file)

        services_dict[service.stem] = {"name": service.stem, "path": str(service.resolve()), "containers": {}}

        for container in ymlfile["services"]:
            try:
                ports_string = ymlfile["services"][container]["ports"]
                ports_list = [p.split(":") for p in ports_string]

                type = []
                for port in ports_list:
                    to_app = "web" if "y" in input(
                                f"Is the service from {service.stem} {container}:{port[-2]} http? [y/N] "
                            ) else "tcp" if "y" in input(
                                    f"... tcp? [y/N] "
                                ) else input(f"... what type is it? ")
                    type.append(to_app)

                container_dict = {
                    "target_port": [p[-1] for p in ports_list],
                    "listen_port": [p[-2] for p in ports_list],
                    "type": [h for h in type],
                }
                services_dict[service.stem]["containers"][container] = container_dict

            except KeyError:
                print(f"{service.stem}_{container} has no ports binding")
            except Exception as e:
                raise e

        with open("services.json", "w") as backupfile:
            json.dump(services_dict, backupfile, indent=2)
    print("Found services:")
    for service in services_dict:
        print(f"\t{service}")

def main():
    global services_dict

    tocd = os.getenv("HOME", "/root")
    os.chdir(tocd)
    print(f"changing to {tocd}")

    if Path("./services.json").exists():
        print("Found existing services file, exiting...")
        exit(1)

    parse_dirs()
    parse_services()

if __name__ == "__main__":
    main()
