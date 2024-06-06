# Tools for A/D simulation for CCIT 2024
## Install
clone this repo on the vulnbox, then run `deploy.sh`
(or use `sh <(curl -sL https://raw.githubusercontent.com/koraynilay/simad/main/deploy_clone.sh` directly on the vulnbox)

## DestructiveFarm
- modify `DestructiveFarm/server/config.py` based on what's the flag regex, the submission server, etc
- run `start_df.sh`

## tulip
- modify `tulip/.env` according to your necessities
- modify `tulip/services/configurations.py` and `tulip/services/api/configurations.py` to include the vulnbox ip, the various services and their ports
- run `start_tulip.sh`

## config ssh carina
add these lines to your `~/.ssh/config`
```
ControlMaster auto
ControlPath ~/.ssh/controlsocket-%h:%p:%r
```
