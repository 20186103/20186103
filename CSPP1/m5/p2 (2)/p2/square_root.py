# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    """using approximation method"""
    given_number = int(input())
    epsilon = 0.01
    increment = 0.1
    guess_value = 0.0
    while abs((guess_value ** 2) - given_number) >= epsilon and guess_value <= given_number:
        guess_value += increment
    print(guess_value)
if __name__ == "__main__":
    main()
