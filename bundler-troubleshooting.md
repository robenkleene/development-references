# Bundler Troubleshooting

If `echo $PATH` is showing one version of Ruby, but when executing commands like `rake` and `bundle` is using a different version of Ruby, this could be because a version of Ruby is hard-coded into the shebang line of the path. You can check this by running, the following command:

    head -n1 $(which bundle)

If that shows the wrong version of Ruby, then usually `gem install bundle` will fix it.
