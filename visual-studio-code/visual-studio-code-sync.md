# Visual Studio Code Sync

Settings are stored at:

	~/Library/Application Support/Code/User

Or:

	~/Library/Application\ Support/VSCodium/User

List extensions:

	code --list-extensions

Store extensions:

	code --list-extensions >> vs_code_extensions_list.txt

Re-install extensions:

	cat vs_code_extensions_list.txt | xargs -n 1 code --install-extension
