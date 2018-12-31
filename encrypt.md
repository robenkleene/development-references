# Encrypt

Use `openssl` to easily encrypt and decrypt a text file.

## Encrypt

	openssl enc -aes-256-cbc -salt -in file.txt -out file.enc

## Decrypt

	openssl enc -d -aes-256-cbc -in file.enc -out file.txt
