# PRE

# print(list(range(10)))
# print(list(range(4, 10)))
# print(list(range(1,10,2)))
# print(list(range(10,2,-1)))

# pętla liczb dwucyfrowych od 10 do 21
# for i in range(10,22):
#     print(i, end=" ")
# pętla liczb dwucyfrowych nieparzystych od 15 do 31  
# for i in range(15,33,2):
#     print(i, end=" ")
# pętla liczb dwucyfrowych malejąco (step ujemny)
# for i in range(99,9,-1):
#     print(i, end=" ")
# pętla liczb dwucyfrowych malejąco (step dodatni)
# for i in range(10, 100, 1):
#     print(109-i, end=" ")
# pętla liczb 3-cyfrowych podzielnych przez 20
# for i in range(100,1000,20):
#     print(i, end=" ")
# print()
# print()
# for i in range(5,50):
#     print(i*20, end=" ")

# Zad 1

# n = int(input())

# for i in range(n):
#     print(i**3 + 3, end=" ")

# Zad 2

# for i in range(105,1000,15):
#     print(i, end=" ")

# for i in range(100,1000):
#     if i % 15 == 0:
#         print(i, end=" ")

# Zad 3 

# n = int(input())
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i, end=" ")

# Zad 4

# s = 0
# for i in range(10,100):
#     s = s + i
# print(s)

# Zad 5
# (5)  => 2 3 1 5
# n = int(input("W ile gramy? "))
# suma = n * (n+1) // 2
# for i in range(n-1):
#     a = int(input())
#     suma = suma - a
# print("Brakuje: ", suma)

# DOD - Napisz pętle sumującą liczby dwucyfrowe parzyste

# Zad 6
# Fibo wg literatury 0 1 1 2 3 5 8 13 21 34 ...
# Fibo nasze: 1, 2, 3, 5, 8, 13 ....
n = int(input())
a, b = 0, 1
for i in range(n):
    a, b = b, a + b
    print(b, end=" ")
    






    
    




    





















