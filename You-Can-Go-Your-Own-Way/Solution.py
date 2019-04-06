# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da
# import math


def path(n, ip):
    #  if len(ip) != (2 * (n - 1)):
    #     return None
    if n == 2:
        return ip[::-1]
        """   
        elif n == 3:
        if ip[n // 2] == ip[(n // 2) + 1]:
            return ip[0] + ip[3] + ip[1] + ip[2]
        elif ip[0:2] == ip[2:4]:
            return ip[0] + ip[2] + ip[1] + ip[3]
        else:
            return ip[2] + ip[3] + ip[0] + ip[1]"""
    else:
        # if(n%2!=0):
        #    if(ip[:n-1]==[n-1:]):
        buffer = list(ip)
        for c in range(len(buffer)):
            if buffer[c] == 'S':
                buffer[c] = 'E'
            else:
                buffer[c] = 'S'
        ip = ''.join(buffer)
        return ip


""" main function"""
if __name__ == "__main__":
    t = int(input())  # read a line with a single integer
    # if t < 1 or t > 100:
    #    exit(0)

    for i in range(1, t + 1):
        # n = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
        nn = int(input())
        if nn < 2:
            pass
        else:
            ipip: str = input()  # .upper()
            if len(ipip) < 2 or ipip.isupper() == False:
                pass
            else:
                print("Case #{}: {}".format(i, path(nn, ipip)))
"""main end"""
