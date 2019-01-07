# `ffmpeg`

## Convert to MP3

	ffmpeg -i input.m4a -q:a 0 output.mp3

## Convert to Apple Lossless

	ffmpeg -i input.flac -c:v copy -acodec alac output.m4a

The `-c:v` seems to be added to deal with artwork metadata.
