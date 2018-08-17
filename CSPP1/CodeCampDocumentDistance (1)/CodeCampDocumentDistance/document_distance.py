'''
    Document Distance - A detailed description is given in the PDF
'''
import math
import re
stopwords = "stopwords.txt"
def cleaning(input1):
    reg = re.compile('[^a-z]')
    input1 = input1.lower()
    input1 = [reg.sub('',w.strip())for w in input1]
    return input1
def create_dictionary(input1,input2):
    d = {}
    d = load_stopwords(stopwords)
    list1 = cleaning(input1)
    list2 = cleaning(input2)
    world_list = list1 + list2
    dictionary = {}
    for word in world_list:
        if word not in d and len(word)>0:
            dictionary[word] = (list1.count(word),list2.count(word))
    return dictionary 
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dictionary ={}
    dictionary=create_dictionary(dict1,dict2)
    numerator = 0
    for d in dictionary.values():
        numerator = numerator + d[0]*d[1]
        d1 = d1 + (d[0]**2)
        d2 = d2 + (d[0]**2)
        denominator = math.sqrt(d1)*math.sqrt(d2)
        return (numerator/denominator)

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
