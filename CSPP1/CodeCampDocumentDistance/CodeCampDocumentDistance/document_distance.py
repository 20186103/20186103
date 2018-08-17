'''
    Document Distance - A detailed description is given in the PDF
'''
import math
FILE = "stopwords.txt"

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    list1 = dict1.split(' ')
    list2 = dict2.split(' ')
    list3 = list1+list2
    dictionary = {}
    for i in list3:
    	if i not in load_stopwords(FILE).keys():
    		if i not in "!@#$%^&*()_+":
                 dictionary = (dict1.count(i), dict2.count(i))
    numerator = 0
    sum1 = 0
    sum2 = 0
    for i in dictionary :
    	numerator += dictionary[i][0] * dictionary[i][1]
    	sum1 += dictionary[i][0] ** 2
    	sum2 += dictionary[i][2] ** 2
    denom = math.sqrt(sum1) * math.sqrt(sum2)
    output = numerator//denom
    return output


def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
