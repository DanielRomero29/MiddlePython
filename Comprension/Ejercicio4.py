numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for num in range(0,len(numlist)):
    if (num+1) % 3 == 0 and (num+1) % 5 == 0:
        numlist[num] = "EOICloud"
    elif (num+1) % 3 == 0:
        numlist[num] = "EOI"
    elif (num+1) % 5 == 0:
        numlist[num] = "Cloud"

print(numlist)