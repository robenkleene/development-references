# Notarize

## Results

If you're app fails notarization, you'll get an email that includes a UUID, insert that and your Apple ID into the following command, and some metadata will be output, which includes a URL, that URL then contains the error message:

	xcrun altool -u "Apple ID" --notarization-info UUID -p @keychain:altool
