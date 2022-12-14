# Zad 1

# a = int(input())
# b = int(input())
# c = int(input())

# # arytm
# if b - a == c - b: print("C jest arytmetyczny")

# # geom
# if b / a == c / b: print("C jest geometryczny")

# # rosnący
# if a < b < c: print("C jest rosnący")

# # malejący
# if a > b and b > c: print("C jest rosnący")

# Zad 2

# suma = 0
# for i in range(100, 1000):
#     if i % 8 == 0 and i % 16 != 0:
#         suma = suma + i
# print(suma)

# Zad 3

# for i in range(99,9,-1):
#     if i % 7 == 0:
#         wielok = i
#         break

# ilość = 0
# for i in range(1000, 10000):
#     if i % wielok == 0:
#         ilość = ilość + 1

# print(ilość)

# Zad 4
# ilość = 0
# for i in range(10, 100):
#     cd = i // 10
#     cj = i % 10
#     if cd >= 2 * cj:
#         ilość += 1
# print(ilość)

# Zad 5

ilość = 0
suma = 0
for i in range(100, 1000):
    cs = i // 100
    cd = (i % 100) // 10
    # cd = (i // 10) % 10
    cj = i % 10
    
print(ilość)


