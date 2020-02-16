# `ssh`

Port forwarding:

	ssh -L <LocalPort>:<RemoteHost>:<RemotePort> user@<RemoteServer>

If a `.ssh/config` is setup, then this shorthand works:

	ssh -L <LocalPort>:localhost:<RemotePort> <hostname>
