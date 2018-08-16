def main():
	"main function"
	num = int(input())
	adict = {}
	i = 0
	while i<num:
		data = input()
		list1 = data.split("")
		if list1[0] not in adict:
			adict