import sys

prefix = '.cheese'
boot = '.boot'
snake = '.snake'

try:
    x = sys.argv[2]
    if sys.argv[1] == prefix and x != None:
        print("big ol snickers bar")
    if sys.argv[1] == boot and x != None:
        print("Massive Big Ol Boot")
    if sys.argv[1] == snake and x != None:
        print("There's a snake, although, not in my boot.")
except IndexError as H:
    print("BADBROKEN")


