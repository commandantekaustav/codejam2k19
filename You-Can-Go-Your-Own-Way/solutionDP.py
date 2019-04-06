"""dynamic programming"""

"""path"""


def newpath(num, oldwalk):
    if 2 == num:
        return oldwalk[::-1]
    elif 3 == num:
        if len(oldwalk) == 2:
            newpath(2,oldwalk)
        elif(oldwalk[0]==oldwalk[1]):
            return newpath(2,oldwalk[0]+oldwalk[2])+newpath(2,oldwalk[3]+oldwalk[1])
        else:
            return newpath(2,oldwalk[0]+oldwalk[1])+newpath(2,oldwalk[2]+oldwalk[3])
    elif 4 == num:
        if len(oldwalk) == 2:
            newpath(2, oldwalk)
        elif len(oldwalk) == 3:
            newpath(3, oldwalk)
        elif(oldwalk[0]==oldwalk[1]):
            if(oldwalk[1]==oldwalk[2]):
                return oldwalk[::-1]
            else:
                if(oldwalk[3]==oldwalk[5] and oldwalk[3]!=oldwalk[4]):
                    return oldwalk[::2]+oldwalk[1::2]
                else:
                    return oldwalk[:3:-1]+oldwalk[3::-1]
        else:
            if(oldwalk[0]==oldwalk[2]):
                if(oldwalk[3]==oldwalk[5] and oldwalk[3]!=oldwalk[4]):
                    return oldwalk[1::2]+oldwalk[::2]
                else:
                    return oldwalk[::2]+reversed(oldwalk[1::2])
    elif 5 == num:
        if len(oldwalk) == 2:
            newpath(2, oldwalk)
        elif len(oldwalk) == 3:
            newpath(3, oldwalk)
        elif len(oldwalk) == 4:
            newpath(4, oldwalk)

        else:
            return newpath(4,oldwalk[:6])+newpath(2,oldwalk[6:])
    elif 6 == num:
        if len(oldwalk) == 2:
            newpath(2, oldwalk)
        elif len(oldwalk) == 3:
            newpath(3, oldwalk)
        else:
            return newpath(5,oldwalk[:8])+newpath(2,oldwalk[8:])
    else:
        lenpath=len(oldwalk)
        if len(oldwalk) == 2:
            newpath(2, oldwalk)
        elif len(oldwalk) == 3:
            newpath(3, oldwalk)
        else:
            for count in range(0,lenpath+1,8):
                return newpath(8,oldwalk[count:count+8])

"""path end"""
"""main start"""
if __name__ == "__main__":
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n = int(input())
        walk: str = input().upper()
        newwalk = newpath(n, walk)
        print("Case #{}: {}".format(i, newwalk))
"main end"
