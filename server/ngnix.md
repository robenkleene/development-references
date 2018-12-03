# `ngnix`

## Check if `ngnix` is Running

	ifconfig eth0 | grep inet | awk '{ print $2 }'
