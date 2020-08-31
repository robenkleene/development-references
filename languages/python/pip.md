# `pip`

## Delete All Packages

	pip3 freeze > dump.txt

Then:

	cat dump.txt | xargs pip3 uninstall -y

## List Package Install Locations

    pip3 list -v
