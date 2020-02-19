def maxi(l1):
    m=l1[0]
    for i in l1:
        if len(i)>len(m):
            m=i
    return len(m)

def fill(l1, res):
    gap = 0
    for i in l1:
        if len(i) != res:
            gap = res - len


l1=["hello","world","in","a","frame"]
res=maxi(l1)
# for j in range(res+4):
#     print("*", end="")
# print()
# for i in range(len(l1)):
#     print("* {a} *".format(a = l1[i]))
# for j in range(res+4):
#     print("*", end="")
# print()
