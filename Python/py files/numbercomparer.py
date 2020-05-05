import sys


if sys.argv[1].isdigit() == False and sys.argv[2].isdigit() == False:
    print('Error at both numbers.')

elif sys.argv[1].isdigit() &  sys.argv[2].isdigit() == True:
    if sys.argv[1] ==  sys.argv[2]:
        print("\nThese numbers are equal :)\n", sys.argv[1], "was first number\n",  sys.argv[2], "was second number.")
    elif sys.argv[1] <  sys.argv[2]:
        print("\nSecond number is Bigger than First Number :).\n", sys.argv[1], "was first number", sys.argv[2], "and was second number.")
    else:
        print("\nFirst number is Bigger than Second Number :).\n", sys.argv[1], "was first number", sys.argv[2], "and was second number.")
elif sys.argv[1].isdigit() == False:
    print("\nError at First Number.")

else:
    print("\nError at Second Number.")
