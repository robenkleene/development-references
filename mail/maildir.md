# `maildir`

## Directories

- `tmp`: Messages in the process of being delivered.
- `new`: Messages that have been delivered, but have not yet been "seen". (So "new" might be synonoumous 
- `cur`: Messages that have already been "seen".

## Filenames

	1491941793.M41[..]30E_0.mx1.example.com,S=10956:2,STln
	^ Arrival timestamp
											^ Size
													^ File format version
													  ^ Flags
														S: Seen
														T: Trashed
														l: IMAP Tag
														n: IMAP Tag

## Filename Tags

These appear at the end of filenames.

- `T`: "Trashed" deleted messages
- `S`: "Seen" read messages
