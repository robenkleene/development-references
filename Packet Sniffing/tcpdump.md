# tcpdump

	sudo tcpdump -s 1024 -l -A dst 93.184.216.34 -i eth0 | grep HTTP

	sudo tcpdump -i en1 -n -s 0 -w - | grep -a -o -E "Host\: .*|GET \/.*"


	sudo tcpdump -s 1024 -l -A dst 93.184.216.34 -i eth0 | grep HTTP

	sudo tcpdump -s 0 -l -A dst 93.184.216.34 -i eth0 | grep HTTP
						 ^ Print packet in ascii
				 ^ Snap zero bytes from packet

	sudo tcpdump -s 0 -A -i en0 | grep HTTP
					  ^ Print packet in ascii
				 ^ Snap zero bytes from packet