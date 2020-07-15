# `wget`

Download a website:

	wget --recursive --no-parent http://usecheck.com/
	wget -r --no-parent http://usecheck.com/

This approach can be a bit more thorough:

	wget -m -p -E -k usecheck.com

## Options

- `-m`, `--mirror`
- `-p`, `--page-requisites`
- `-E`, `--adjust-extension`
- `-k`, `--convert-links`
