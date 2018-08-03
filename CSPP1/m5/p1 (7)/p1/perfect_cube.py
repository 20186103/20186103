# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
	# input is captured in s
	# watch out for the data type of value stored in s
	# your code starts here
    x = int(input('enter an integer: '))
    ans = 0
    while ans**3 < abs(x) :
        ans = ans + 1
    if ans**3 != abs(x):
        print(str(x) + ' is not a perfect cube')
    else:
        if x < 0:
            ans = - ans
        print(str(x) + ' is a perfect cube')
if __name__ == "__main__":
    main()
