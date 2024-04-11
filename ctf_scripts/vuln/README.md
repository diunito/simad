
## start.sh
Auto download some utils
- tmux
- python3
- proxy & proxy_helper
- dump script

# dump.sh
Cyclic dump of the Network traffic and send to tulip

# proxy_helper.py
Script that parses running dockers and goes to modify their comopse file to suit execution under ctf_proxy

## one command
Autostart software deploy on the vulnbox

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/AlessandroMIlani/ctf_scripts/main/vuln/start.sh)"
```
