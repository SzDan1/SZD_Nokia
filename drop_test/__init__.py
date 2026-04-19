with open("drop_test/input.txt", "r") as file:
    fileContent = file.read()
    def min_num_of_drops(n,k):
        throws = [0] *(n+1)
        x=0
        while throws[n] < k:
            x+=1
            for i in range(n,0,-1):
                throws[i] = throws[i] + throws[i-1]+1
        return x 

for i in fileContent.splitlines():
    i = i.strip()
    n, x = i.split(",")
    n = int(n.strip())
    x = int(x.strip())
    print(min_num_of_drops(n,x))