#!/bin/bash
serv_folder="$HOME"
pip install ruamel.yaml
cd "$serv_folder"
python3 ctf_proxy/setup_proxy.py
