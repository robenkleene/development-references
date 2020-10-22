# `ssh`

Port forwarding:

	ssh -L <LocalPort>:<RemoteHost>:<RemotePort> user@<RemoteServer>

If a `.ssh/config` is setup, then this shorthand works:

	ssh -L <LocalPort>:localhost:<RemotePort> <hostname>

To server static HTML files use:

	python -m http.server 3000

## After Connecting

To forward a port after connecting, use the following command (the `-N` runs `ssh` without opening a shell):

    ssh -N -L 3000:localhost:3000 aresdev
