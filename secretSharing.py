import shamirs

s1 = shamirs.shares(456, quantity=20, modulus=15485867, threshold=10)
# print(s1)
s2 = shamirs.shares(123, quantity=20, modulus=15485867, threshold=10)
# print(s2)
for i in range(len(s1)):
    s1[i].value=s1[i].value+s2[i].value
ret = shamirs.interpolate(s1[5:15], threshold=10)
print(ret)