#Guess My Number Exercise

def main():
    l = 0
    h = 100
    b = input()
    while b !=  "c":
        s=(l+h)//2 
        print ("Is your secreat number is" + str(s) )
        b=input()
        if b == "c":
            break
        elif b == "l":
            l=s
        elif b == "h":
            h=s
    print(" your secreat number was " + str(s))

if __name__== "__main__":
	main()