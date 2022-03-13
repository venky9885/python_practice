# [4,5,0,1,0,0,5]
"""
#!1
n = [6, 0, 1, 8, 0, 2]
c = 0
l = []
for i in range(len(n)):
    if(n[i] == 0):
        l.append(i)
        # n.remove(0)
        c += 1
# print(n)
for i in range(c):
    n.remove(0)
    # n.append(0)
print(n)
n.extend([0]*c)
print(n)
"""
"""
#!2
print(int(bin(10)[2:][::-1], 2))

"""
"""
#!3
"""
l = [8, 2, 6, 4, 5]

for i in range(len(l)):
    for j in range(1, len(l)-1):
        if(l[i] > l[j]):
            t = l[i]
        # pass
