# `pip`

Delete all dependencies:

	pip3 freeze > dump.txt

Then:

	cat dump.txt | xargs pip3 uninstall -y
