# john kavanagh
# this is to see how a power function operates

def power(x, y):
    ans = x
    y = y - 1
    while y > 0:
        ans = ans * x
        y = y - 1
    return ans

print(power(2, 5))
