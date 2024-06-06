CONFIG = {
    # Don't forget to remove the old database (flags.sqlite) before each competition.

    # The clients will run sploits on TEAMS and
    # fetch FLAG_FORMAT from sploits' stdout.
    'TEAMS': {'Team #{}'.format(i): '10.60.{}.1'.format(i)
              for i in range(1, 90 + 1)},
    'FLAG_FORMAT': r'[A-Z0-9]{31}=',
    #'FLAG_FORMAT': r'[A-Z0-9]{31}=',

    # This configures how and where to submit flags.
    # The protocol must be a module in protocols/ directory.

    # 'SYSTEM_PROTOCOL': 'ructf_tcp',
    # 'SYSTEM_HOST': '127.0.0.1',
    # 'SYSTEM_PORT': 31337,

    # 'SYSTEM_PROTOCOL': 'ructf_http',
    # 'SYSTEM_URL': 'http://monitor.ructfe.org/flags',
    # 'SYSTEM_TOKEN': 'your_secret_token',


    'SYSTEM_PROTOCOL': 'ructf_http',
    'SYSTEM_URL': 'http://10.10.0.1:8080/flags',
    #'SYSTEM_TOKEN': 'a032d2b07e8d76968a3abe62a5124627',
    'SYSTEM_TOKEN': '17cea63121928b09ffd8e0a5886ff0d1',
    'SYSTEM_ID_FLAGS_IP': '10.10.2.1',
    'SYSTEM_ID_FLAGS_PORT': '8084',


    # 'SYSTEM_PROTOCOL': 'volgactf',
    # 'SYSTEM_HOST': '127.0.0.1',

    # 'SYSTEM_PROTOCOL': 'forcad_tcp',
    # 'SYSTEM_HOST': '10.10.0.1',
    # 'SYSTEM_PORT': 31337,
    # 'TEAM_TOKEN': 'ea8943ee3e9ae788',

    # 'SYSTEM_PROTOCOL': 'forcad_tcp',
    # 'SYSTEM_HOST': '130.192.5.212',
    # 'SYSTEM_PORT': 7777,
    # 'TEAM_TOKEN': 'ea8943ee3e9ae788',

    # The server will submit not more than SUBMIT_FLAG_LIMIT flags
    # every SUBMIT_PERIOD seconds. Flags received more than
    # FLAG_LIFETIME seconds ago will be skipped.
    'SUBMIT_FLAG_LIMIT': 50,
    'SUBMIT_PERIOD': 5,
    'FLAG_LIFETIME': 5 * 120,

    # Password for the web interface. You can use it with any login.
    # This value will be excluded from the config before sending it to farm clients.
    'SERVER_PASSWORD': 'SaccintoSvizzera2',

    # Use authorization for API requests
    'ENABLE_API_AUTH': True,
    'API_TOKEN': 'SaccintoSvizzeraAP1TOK'
}
