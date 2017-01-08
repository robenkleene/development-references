# `pandoc`

## Convert HTML to Markdown

From a pipe:

	pandoc -f html -t markdown

From a file:

	pandoc testfile.html -o test.md --parse-raw