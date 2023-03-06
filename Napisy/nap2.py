# palindrom za pomocą tablicy

# s = input()

# for i in range(len(s)//2):
#     if s[i] != s[len(s)-1-i]:
#         exit("NIE JEST")
# exit("JEST PALINDROMEM")

# anagramy - co to jest
# dama i adam i aamd

# anagram za pomocą funkcji

# a = input()
# b = input()
# A = list(a)
# B = list(b)
# A.sort()
# B.sort()
# a = "".join(A)
# b = "".join(B)

# print(a,b)
# if a==b:
#     print("TAK")
# else:
#     print("NIE")

# anagram za pomocą tablic

a = input()
b = input()
X = [0] * 200
Y = [0] * 200
for i in range(len(a)):
    X[ord(a[i])] += 1
for j in range(len(b)):
    Y[ord(b[j])] += 1
if X == Y:
    print("TAK")
else:
    print("NIE")
    