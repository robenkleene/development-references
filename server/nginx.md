# `ngnix`

- `sudo systemctl reload nginx`: Restart
- `sudo nginx -t -c /etc/nginx/nginx.conf`: Print configuration errors

## Check if `ngnix` is Running

	ifconfig eth0 | grep inet | awk '{ print $2 }'
