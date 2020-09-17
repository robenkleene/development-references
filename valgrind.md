# `valgrind`

    valgrind --tool=memcheck --leak-check=full ./a.out 

Verbose example:

    valgrind --leak-check=full \
             --show-leak-kinds=all \
             --track-origins=yes \
             --verbose ./a.out
