date = int(input())
dow = int(input())
nd = date + 7
if nd % 7 == 1 and dow == 1:
    nd += 1
print(nd)
