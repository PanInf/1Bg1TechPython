# 1. Wczytaj dowolny napis i wypisz z niego pierwszą i ostatnią literkę

# x = input()
# print(x[0], x[-1])
# print(x[0], x[len(x)-1])

# 2. Wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej

# a = input()
# for i in range(1, len(a)-1):
#     print(a[i], end="")
# print()

# print(a[1:len(a)-1])

# 3. Wypisz 4 ostatnie literki z wpisanego napisy w kolejności od końca

# b = input()

# for i in range(len(b)-1, len(b)-5, -1):
#     print(b[i], end="")
# print()

# print(b[len(b)-1:len(b)-5:-1])

# L = list(b)
# L.reverse()
# b = "".join(L)
# for i in range(4):
#     print(b[i], end="")
# print()

# 4. Waga napisu to suma kodów ascii jego liter. Zważ wpisny napis

c = input()
suma = 0
for i in c:
    suma += ord(i)
print(suma)

# 5. Policz ile we wpisanym napisie jest liter A.



# 6. Podaj dominującą literkę we wpisanym napisie. Niech to będzie tylko jedna literka.

