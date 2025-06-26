import sys

try:
    print(sys.argv[1])
except IndexError:
    print("No argument was given. Try again.")
