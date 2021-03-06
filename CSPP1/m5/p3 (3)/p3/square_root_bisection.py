# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

'"find the square root of the given number using Bi-section method "'

def main():
    """bisection method"""
    square = int(input())
    epsilon = 0.01
    low = 0
    high = square
    guess = (high + low)/2.0
    while abs(guess ** 2 - square) >= epsilon:
        if guess ** 2 < square:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
    print(guess)
if __name__ == "__main__":
    main()
