with open("magic_numbers/input.txt", "r") as file:
    fileContent = file.read()

    def next_magic_num(num):
       n = str(num)
       length = len(n)
       left = n[:length//2]
       if length % 2 == 0:
           magicN = left + left[::-1]
       else:
           middle = n[length//2]
           magicN = left + middle + left[::-1]
       if int(magicN) > num:
           return magicN
       if len(str(num+1)) > len(n):
           return str(num+2)
       else:
           if length % 2 == 0:
            left = str(int(left)+1)
            magicN = left + left[::-1]
           else:
            middle = str(int(left+middle)+1)
            left = middle[:-1]
            middle = middle[-1]
            magicN = left + middle + left[::-1]
       return int(magicN)
    
    def power_parse(num):
        first, last = num.split('^')
        return int(first)**int(last)
    
for i in fileContent.split():
    if '^' in i:
        num = power_parse(i)
    else:
        num = int(i)
    magicN = next_magic_num(num)
    print(magicN)
