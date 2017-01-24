# `mitmproxy`

## iOS

1. Make sure the device and computer are on the same Wi-Fi network.
2. Get the IP address of your computer `ifconfig` look for `en0` (or "System Preferences" -> "Network" -> "TCP/IP" -> "IPv4 Address")
3. Set the device to use a proxy with the IP address and port 8080.
4. Run `mitmproxy`
5. Go to "http://mitm.it" to install the certificate
6. Start generating traffic

If your certificate is expired, delete the `.mitmproxy`.

## Filter

* `f`: Enter filter mode, once in filter mode:
	* `~d google`: Filter by domain
