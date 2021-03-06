'''
Given a  number int_input, find the product of all the digits
example:
	input: 123
	output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    product = 1
    if int_input == 0:
        product = 0
    if int_input < 0:
        int_input = -int_input
        product = -product
    while int_input != 0:
        rem = (int_input%10)
        product = (product * rem)
        int_input = int_input//10
    print(product)


if __name__ == "__main__":
    main()
