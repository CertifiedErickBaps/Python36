s = [4, 8 , 15, 16, 23, 42]
print(s[3])
print(s[-1])
print(s[2:4])
print(s[::2])
print(s[::-1])
print(s+[1,2])
print([1,0]*3)

for e in s:
    print(e)
print(8 in s) #True
print(1 not in s) #True
print([1,2]==[2,3])
print([4,8,15] < s)