# `mitmproxy`

## Reverse Proxy

You can use a reverse proxy to sniff all traffic between a browser and a local server.

If the server you want to sniff is on `http://localhost:4000`, then setup `mitmproxy` with:

	mitmproxy --mode reverse:http://localhost:4000 -p 4001 

Then visit `localhost:4001`.

`mitmproxy` will show every request between the browser and `localhost:4000`.

## iOS

1. Make sure the device and computer are on the same Wi-Fi network.
2. Get the IP address of your computer `ifconfig` look for `en0` (or "System Preferences" -> "Network" -> "TCP/IP" -> "IPv4 Address")
3. Set the device to use a proxy with the IP address and port 8080.
4. Run `mitmproxy`
5. Go to "http://mitm.it" to install the certificate
6. Start generating traffic

If your certificate is expired HTTPS won't work. To fix it, delete the `~/.mitmproxy` directory and re-install the certificate.

## Filter

* `f`: Enter filter mode, once in filter mode:
	* `~d google`: Filter by domain
* `b`: Export body
* `z`: Clear
