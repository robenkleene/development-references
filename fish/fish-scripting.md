# Fish Scripting

## Quoting

Numeric values don't need to be quoted:

    if test $status -eq 0
        echo -n (basename $git_path)
    end

## Parameter Expansion

Parameter expansion is the act of expanding special characters in parameters, for example globbbing. Parameter expansion does *not* happen in quotes.

    echo *.sh # a_file.sh
    echo "*.sh" # *.sh
