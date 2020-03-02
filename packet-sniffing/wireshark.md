# Wireshark

## Filters

### Port Number

	cp.port == 443

### Host

	http.host contains "www.sbb.ch" 
	ip.src_host contains "spacexdata"

Filtering by hostname will not work unless "Preferences > Name Resolution > Resolve network (IP) addresses is turned on (Wireshark does not have to collect new data after this option is toggled on).

### IP Address

	ip.addr == 104.31.87.73
