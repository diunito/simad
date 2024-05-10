#!/bin/bash
for a in `ls`;do
	./start_sploit.py cc-manager.py -u 10.81.81.16:5000 --token SaccintoSvizzeraAP1TOK &
done
