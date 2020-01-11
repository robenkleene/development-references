# `jekyll`

## Common Configurations

Only recent:

	bundle exec jekyll serve --watch --drafts --config _config_local.yml --limit_posts 5

Everything:

	bundle exec jekyll serve --watch --drafts --config _config_local.yml

Everything No Configuration:

	bundle exec jekyll serve --watch --drafts

## Normal

	jekyll build --watch
	jekyll serve

## With Drafts

	jekyll build --watch --drafts
	jekyll serve --drafts

## With `github-pages` Gem

	bundle exec jekyll serve
	bundle exec jekyll build --watch

### Include Drafts

	bundle exec jekyll serve --drafts
	bundle exec jekyll build --watch --drafts

## Generating Faster

### Local `_config.yml`

	--config _config_local.yml

This is useful to specify a local theme that doesn't need to get fetched from the server first:

	# theme: minima
	# remote_theme: robenkleene/cyclist
	theme: cyclist

### Limit posts

	--limit_posts 5
