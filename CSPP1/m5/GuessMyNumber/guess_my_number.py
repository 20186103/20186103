
def main():
    '''main function'''
    num = int(input())
    adict = {}
    i = 0
    while i < num:
        data = input()
        list1 = data.split(" ")
        if list1[0] not in adict:
            adict[list1[0]] = [int(list1[1])]
        else:
            adict[list1[0]].append(int(list1[1]))
        i += 1
    print(adict)
main()
