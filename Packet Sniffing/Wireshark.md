# Wireshark & Packet Sniffing

	wireshark-qt

Fish:

	sudo chgrp admin /dev/bpf* ;and sudo chmod g+rw /dev/bpf* ;and echo "ChmodBPF ran successfully."

bash

	chgrp admin /dev/bpf* && chmod g+rw /dev/bpf* && echo "ChmodBPF ran successfully."

## Filters

	cp.port==443
	tshark -Y 'http contains dowjones'
	http.host contains "www.sbb.ch" 


## Analyzing `HTTPS` traffic to `iwap` URL

	tcpdump -s 0 -A -i en0 port 443 | grep iwap

Or even better:

	tcpdump -i en0 port 443