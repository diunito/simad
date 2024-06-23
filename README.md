# Tools for A/D simulation for CCIT 2024
## Install
- clone this repo locally with
  ```bash
  git clone --recurse-submodules git@github.com:koraynilay/simad && git submodule foreach 'git switch master || git switch main' && git submodule foreach git status | grep HEAD
  ```
  (change `git@github.com:koraynilay/simad` to `https://github.com/koraynilay/simad` if using http auth)
- use `ctf_scripts/user/setup_vuln.sh` (or clone this repo on the vulnbox, then run `deploy.sh` (or use `sh <(curl -sL https://raw.githubusercontent.com/diunito/simad/main/deploy_clone.sh)` directly on the vulnbox))

## DestructiveFarm
- modify `DestructiveFarm/.env` based on what's the flag regex, the submission server, etc
- modify path of `.env` in `start_df.sh`
- run `start_df.sh`

## Tulip
- modify `tulip/.env` according to your necessities
- modify `tulip/services/api/configurations.py` to include the vulnbox ip, the various services and their ports
- - modify path of `.env` in `start_tulip.sh`
- run `start_tulip.sh`

## Firegex
- make a `.env` file with `FIREGEX_PORT` and `FIREGEX_PSWD`
- change the path to the `.env` in `start_firegex.sh`
- run `start_firegex.sh`

## SSH config
add these lines to your `~/.ssh/config` to not have to put the password everytime
```
Host your.vuln.ip
    ControlMaster yes
    ControlPath ~/.ssh/controlsocket-%h:%p:%r
    ControlPersist 10h
```
or just copy your ssh key to the vuln (with `ssh-copy-id`)
