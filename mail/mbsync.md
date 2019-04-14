# `mbsync`

To get the certificate, copy the first `-----BEGIN CERTIFICATE-----` to `-----END CERTIFICATE-----` block into a `.pem` file.

	openssl s_client -connect imap.server.com:993 -showcerts
