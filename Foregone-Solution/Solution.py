#problem statement can be found at
#https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231
#I/O:      python3 solution.py < input_file.txt > output_file.txt

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.


def divsum(n):
    #math library having problems. maybe something deleted from interpreter
    if n%2 == 0:
        up=n
    else:
        up=(n//2) + 1

    for i in range(1,up+1):
        if(notfour(str(i),str(n-i))):
            return (int(i),int(n-i))


def notfour(num1,num2):
    confirmation = True
    for i in num1+num2:
        if i=="4":
            confirmation = False
    return confirmation

if __name__=="__main__":
    t = int(input()) # read a line with a single integer
    if t<1 or t>100:
        exit(0)
    for i in range(1, t + 1):
        #n = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
        n=int(input())
        if n<1:
            pass
        else:
            ans1 = divsum(n)
        print("Case #{}: {} {}".format(i, ans1[0],ans1[1]))
