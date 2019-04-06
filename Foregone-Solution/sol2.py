
def divsum(n):
    #math library having problems. maybe something deleted from interpreter
    if n%2 == 0:
        up=n
    else:
        up=(n//2) + 1

    for i in range(1,up+1):
        if(n%i!=4 or n%i!=44 or n%i!=444 or n%i!=4444 or n%i!=44444 or n%i!=444444 or n%i!=4444444 or n%i!=44444444 or n%i!=444444444 or n%i!=4444444444 or n%i!=44444444444):
            if(notfour(str(i),str(n-i))):
                return (int(i),int(n-i))


def notfour(num1,num2):
    #confirmation = True
    for i in num1+num2:
        if i=="4":
            #confirmation = False
            return False
    return True

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
