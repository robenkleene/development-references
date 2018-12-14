# `iptables`

- `sudo iptables -L`: List current rules
- `sudo iptables -S`: Output rules by configuration command

## Dangerous

- `sudo iptables -F`: Revert to default rules

## `iptables-persistent`
To save new rules made after installing `iptables-persistent` use:

	sudo netfilter-persistent save

Reload from disk:

	sudo netfilter-persistent reload
