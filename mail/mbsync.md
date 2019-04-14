# `mbsync`

## Notes

- `Expunge Slave`: The `maildir` `imap` implementation seems to leave a deleted message every time a message is moved to another folder. `Expunge Slave` deletes those messages locally.

## Certificate

To get the certificate, copy the first `-----BEGIN CERTIFICATE-----` to `-----END CERTIFICATE-----` block into a `.pem` file.

	openssl s_client -connect imap.server.com:993 -showcerts

## `MaxMessages`

Seems that flagged and unread messages will be always be downloaded, even if they are over the `MaxMessages` setting.
