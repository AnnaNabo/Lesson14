import sys

def zapSP(my_list, n,i):
    if i > n:
        return
    my_list.append(i)
    zapSP(my_list,n,i+1)

def pech(my_list,j):
    if j > (len(my_list)-1):
        print("конец списка")
        return
    print(my_list[j])
    pech(my_list, j+1)
    
my_list = []
print("введите кол-во элементов последовательности:")
n = int(input())
sys.setrecursionlimit(n*2)
i = 0
j =0

zapSP(my_list, n,i)
print("my_list:")
print(my_list)
pech(my_list,j)


