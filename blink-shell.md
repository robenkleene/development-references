# Blink Shell

Key-based authentication occasionally randomly stops working, the solution is to delete and re-add the key.

You can get more information by running `ssh -vv <host>` in Blink Shell. The error where you have to re-generate the key is "could not find public key files".

Potential solution to the above key issue: It seems like there's a conflict between iCloud Sync and private keys. The host information is synced but the keys aren't, so the solution seems to be to name the two keys the same on the two different devices, so the synced host information will still point to valid key.
