
# functions 
def cal_sum(a, b):
    sum = a+b
    print(sum)
    return sum

cal_sum(2, 4)

cal_sum(6, 8)

def cal_sum(a, b):
    return a+b
sum= cal_sum(8, 13)
print(sum)

def cal_avg(a,b,c):
    sum = a+b+c
    avg = a+b+c/3
    print(avg)
    return avg
cal_avg(15, 17, 8)
# waf to print the length of list 
values = ["single", "double"]
cities = ["guj", "lahore", "karachi"]
def print_len(list):
    print(len(list))
print_len(values)
print_len(cities)

def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(cities)
print()

# factorial 
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
    print(fact)
cal_fact(6)
# converter
def converter(usd):
    ind= usd*83
    print("usd =", ind)
converter(1)

# recursion
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(3)
# fact
def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1) * n
print(fact(6))
#recursion sum of first n natural numbers
def cal_sum(n):
    sum=0
    if(n==0):
        return 0
    return cal_sum(n-1) + n
print (cal_sum(7))
# recursion
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
fruits = ["banana", "apple", "cherry",]
print_list(fruits)