def divsum(n):
    if n % 2 == 0:
        up = n
    else:
        up = (n // 2) + 1

    for i in range(1, up + 1):
        check = True
        concatno = int(str(i) + str(n - i))
        # lenccn = len(concatno)
        #for j in str(i) + str(n - i):
        #    if j == "4":
        #        check = False
        #        break

        while concatno > 0:
            if(concatno%10!=4):
                concatno = concatno // 10
            else:
                check=False
                break

        if(check):
            return int(i)


""" main function"""
if __name__ == "__main__":
    t = int(input())  # read a line with a single integer
    if t < 1 or t > 100:
        exit(0)

    for i in range(1, t + 1):
        # n = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
        n = int(input())
        if n < 1:
            pass
        else:
            x = divsum(n)
        print("Case #{}: {} {}".format(i, str(x), str(n-x)))
"""main end"""
