# `pandoc`

## Convert HTML to Markdown

From a pipe:

	pandoc -f html -t markdown

From a file:

	pandoc testfile.html -o test.md --parse-raw

## Convert Rich Text to Markdown

    osascript -e 'the clipboard as «class RTF »' | perl -ne 'print chr foreach unpack(\"C*\",pack(\"H*\",substr($_,11,-3)))' | textutil -stdin -stdout -convert html -format rtf | pandoc -f html-native_divs-native_spans -t markdown --wrap=none
