# `ssh`

Port forwarding:

	ssh -L <LocalPort>:<RemoteHost>:<RemotePort> user@<RemoteServer>

If a `.ssh/config` is setup, then this shorthand works:

	ssh -L <LocalPort>:localhost:<RemotePort> <hostname>

To server HTML files use:

	python -m http.server 3000
