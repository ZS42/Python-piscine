import sys  # to allow us to take arguments from command line

# If there's more than one argument, raise an error
if len(sys.argv) > 2:
    raise AssertionError("more than one argument is provided")
# If there is exactly one argument, check if it's an integer
if len(sys.argv) == 2:
    try:
        num = int(sys.argv[1])
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        raise AssertionError("argument is not an integer.")

# expected output
# $> python whatis.py 14
# I'm Even.
# $>
# $> python whatis.py -5
# I'm Odd.
# $>
# $> python whatis.py
# $>
# $> python whatis.py 0
# I'm Even.
# $>
# $> python whatis.py Hi!
# AssertionError: argument is not an integer
# $>
# $> python whatis.py 13 5
# AssertionError: more than one argument is provided
