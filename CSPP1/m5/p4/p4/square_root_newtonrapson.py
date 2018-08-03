# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    """newton-rapson method"""
    square = int(input())
    epsilon = 0.01
    guess_value = square/2.0
    while abs(guess_value * guess_value - square) >= epsilon:
        guess_value = guess_value - (((guess_value**2) - square)/(2 * guess_value))
    print(guess_value)
if __name__ == "__main__":
    main()
