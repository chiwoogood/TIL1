#1924
# n, m = map(int, input().split())
# sum = 0
# day = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
# dic = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
# for i in range(1,n+1):
#     if i == n:
#         sum += m
#         print(day[(sum - 1) % 7])
#         break
#     sum += dic[i]



#10818
# n = int(input())

# lst = list(map(int, input().split()))

# max = lst[0]
# min = lst[0]

# for i in range(len(lst)):
#     if lst[i] > max:
#         max = lst[i]
#     if lst[i] < min:
#         min = lst[i]
# print(max,min)

#2445
# n = int(input())

# for i in range(1,n*2):
#     if i <= n:
#         for _ in range(i):
#             print("*",end="")
#         for _ in range((n-i)*2):
#             print(" ",end="")
#         for _ in range(i):
#             print("*",end="")
#         print()
#     else :
#         for _ in range(n*2-i):
#             print("*",end="")
#         for _ in range(i%n*2):
#             print(" ",end="")
#         for _ in range(n*2-i):
#             print("*",end="")
#         print()     


#2751
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))

# for i in range(len(lst)):
#     print(lst.pop())

# lst = list(map(int, input().split()))

# for i in range(len(lst)):
#     min_idx = i  # 변수명 수정: min_idx로 변경
#     for j in range(i + 1, len(lst)):
#         if lst[j] < lst[min_idx]:  # 부등호 방향 수정: 최소값을 찾아야 하므로
#             min_idx = j

#     lst[i], lst[min_idx] = lst[min_idx], lst[i]

# print(lst)



#좌표이동
# move = input().split()
# x, y = map(int, input().split())

# #우좌상하
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# for i in move:
#     if i == 'R':
#         movements = 0
#     elif i == 'L':
#         movements = 1
#     elif i == 'U':
#         movements = 2
#     else:
#         movements = 3
    
#     x += dx[movements]
#     y += dy[movements]

# print(f'입력하신 좌표에서 움직인 현재 좌표는 ({x,y})입니다.')



#체스 말병정이 움직일 수 있는 경우의수

# x, y = map(int, input().split())

# steps = [(-1, -2), (1, -2), (-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2)]

# count = 0

# for step in steps:
#     nx, ny = step
#     new_x = x + nx
#     new_y = y + ny

#     if 0 <= new_x < 8 and 0 <= new_y < 8:
#         count += 1

# print(count)


# n = input().split()
# for i in n:
#     print(ord(i) - ord('a') + 1,end="")

#2875
# W, M, I = map(int,input().split())

# team = 0

# while(W>=2):
#     W -= 2
#     M -= 1
#     if W + M >= I:
#         team += 1
    
# print(team)

#11047

# coin, money = map(int,input().split())

# count = 0

# lst = []
# for _ in range(coin):
#     lst.append(int(input()))

# def sort_value(lst):
#     for i in range(len(lst)):
#         max_idx = i
#         for j in range(i+1,len(lst)):
#             if lst[max_idx] < lst[j]:
#                 max_idx = j
#         lst[i], lst[max_idx] = lst[max_idx], lst[i]
    
#     return lst

# new_lst = sort_value(lst)
# print(new_lst)

# for i in new_lst:
#     if money < i:
#         continue
#     count += money // i
#     money = money % i

# print(count)


#10610
# 10610번

# n = input()

# if "0" not in n:
#     print(-1)

# else:
#     num_sum = 0
#     for i in range(len(n)):
#         num_sum += int(n[i])

#     if num_sum % 3 != 0:
#         print(-1)
    
#     else:
#         sorted_num = sorted(n, reverse=True)
#         answer = "".join(sorted_num)
#         print(answer)

# 복사 + 리스트를 수정하면서 순회 + pop, append 동시에 사용
# lst = list(input())

# for i in lst[:]:
#     if i.isalpha() == False:
#         lst.append(lst.pop(lst.index(i)))

# print(lst)


# n = input()
# sum = 0
# for i in n:
#     sum += int(i)
# def sort(n):
#     for i in range(len(n)):
#         max_idx = i
#         for j in range(i+1,range(len(n))):
#             if n[max_idx] < n[j]:
#                 max_idx = j
#             n[i], n[max_idx] = n[max_idx], n[i]
    
#     return n
# if sum % 3 != 0:
#     print(-1)
# else:
#     n = sort(list(n))

# for i in n:
#     print(i,end="")

# words = ['hi', 'hello', 'kimchi']
# words = "".join(words)
# print(words)


#2587
# lst = []
# for i in range(5):
#     lst.append(int(input()))
# print(sum(lst)//len(lst))
# if 


#1744

# n = int(input())
# sum = 0

# lst = []
# for i in range(n):
#     lst.append(int(input()))

# def sort_value(lst):
#     for i in range(len(lst)):
#         max_idx = i
#         for j in range(i+1,len(lst)):
#             if lst[max_idx] < lst[j]:
#                 max_idx = j
#         lst[i], lst[max_idx] = lst[max_idx], lst[i]
#     return lst

# new_lst = sort_value(lst)

# for i in range(len(new_lst)):
#     if i % 2 == 0:
#         new_lst[i]

# n = int(input())
# lst = []

# for i in range(2, n + 1):
#     is_prime = True

#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             is_prime = False
#             break

#     if is_prime:
#         lst.append(i)

# print(lst)

#삽입정렬
# n = list(map(int,input().split()))

# for i in range(len(n)):
#     min_idx = i
#     for j in range(i+1,len(n)):
#         if n[min_idx] > n[j]:
#             min_idx = j # 작은 인덱스에다 j값을 삽입 
#     n[i], n[min_idx] = n[min_idx], n[i]
# print(n)


#퀵정렬
# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# def quick_sort(array, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end

#     while(left <= right):
#         while(left <= end and array[left] <= array[pivot]):
#             left +=1
        
#         while(right > start and array[right] >= array[pivot]):
#             right -=1

#         if(left > right):
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#             array[left], array[right] = array[right],array[left]
    
#     quick_sort(array,start,right -1)
#     quick_sort(array,right+1,end)

# quick_sort(array,0,len(array)-1)
# print(array)


# 퀵정렬

# lst1 = [1, 5, 2, 4, 7, 8,12,2,0]

# def quick_sort(lst):
#     if len(lst) <=1:
#         return lst
#     pivot = lst[len(lst) // 2]
#     left = [x for x in lst if x < pivot]
#     middle = [x for x in lst if x == pivot]
#     right = [x for x in lst if x > pivot]

#     return quick_sort(left) + middle + quick_sort(right)

# new_lst = quick_sort(lst1)
# print(new_lst)



#이진탐색
def binary_search(array, target):
    start, end = 0, len(array) -1
    mid = (start + end) // 2
    while(start<=end):
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid -1
    return -1


#for else문
# n = int(input())
# while(n > 0):
#     if n == -1:
#         print('hello')
#     n -= 1
# else:
#     print('여기에 없는데용')


#10814
# n = int(input())

# dic = dict()
# for i in range(n):
#     key, value = input().split()
#     dic[int(key)] = value

# def quick_sort(lst):
#     if len(lst)<=1:
#         return lst
    
#     pivot = lst[len(lst) // 2]

#     start = [x for x in lst if x < pivot]
#     middle = [x for x in lst if x == pivot]
#     end = [x for x in lst if x > pivot]

#     return quick_sort(start) + middle + quick_sort(end)

# print(quick_sort([1,5,2,6,5]))

# n = int(input())
# lst = [list(input().split()) for _ in range(n)]

# def sort_value(lst):
#     for i in range(len(lst)):
#         min_idx = i
#         for j in range(i+1,len(lst)):
#             if int(lst[min_idx][0]) > int(lst[j][0]):
#                 min_idx = j
#     lst[i], lst[min_idx] = lst[min_idx], lst[i]
    
#     return lst

# print(sort_value(lst))

# 2609
#최대 공약수
#최소 공배수

# A , B = map(int,input().split())
# A , B = (B , A) if B > A else (A , B)

# lst = []

# for i in range(2,B+1):
#     if A % i == 0 and B % i == 0:
#         lst.append(i)

# print(max(lst), A*B // max(lst))

# A , B = map(int,input().split())
# A , B = (B , A) if B > A else (A, B)
# lst = [i for i in range(2,B+1) if A % i == 0 and B % i == 0]
# print(max(lst), (A*B)/max(lst))

# 1934
# n = int(input())
# def cal(A,B):
#     lst = []
#     A , B = (B , A) if B < A else (A, B)
#     for i in range(1,B+1):
#         if A % i == 0 and B % i == 0:
#             lst.append(i)
#     return max(lst)
# for i in range(n):
#     A, B = map(int,input().split())
#     print(A*B // cal(A,B))

#1850

# A, B = map(int,input().split())
# A , B = (B, A) if A > B else (A , B)
# lst = []
# if (B - A) % A == 0:
#     for _ in range(A):
#         print(1,end='')
# else:
#     for _ in range(B-A):
#         print(1,end='')


#2942 유클리드
# a, b =map(int,input().split())
# i = 1
# while(True):
#     if a % i == 0 and b % i == 0:
#         print(i,a//i,b//i )
#     i += 1
#     if i > b or i > a:
#         break

# def uclid(a,b):
#     while b:
#         a, b = b, a %b
#     return a

# print(uclid(18,48))

#9613
# n = int(input())
# for i in range(n):
    
# m, n = map(float,input().split())

# c, d = map(bool, map(int,input().split()))


# print(True) if c != d else print(False)

# while True:
#     user_input = input()
#     if user_input != 'q':
#         print(user_input)
#     else:
#         print(user_input)
#         break


#코드업
# pasta_lst = [int(input()) for _ in range(3)]
# drink_lst = [int(input()) for _ in range(2)]
# print(f'{(min(pasta_lst)+ min(drink_lst)) * 1.1:.1f}')


# dic = dict({1:1,2:2,3:3,4:2,5:1,6:2,7:3,8:3,9:2})

# a, b = map(int,input().split())
# def cal(a,b):
#     count = 0
#     if a - b == 0:
#         return 0
#     a , b = (b, a) if a > b else (a,b)
#     while b - a > 10:
#         b -= 10
#         count += 1
    
#     if a - b == 0:
#         return count
#     count += dic[b-a]
#     return count

# print(cal(a,b))

# pasta_price = [int(input()) for _ in range(3)]
# drink_price = [int(input()) for _ in range(2)]

# print(f'{((min(pasta_price) + min(drink_price)) *1.1):.1f}')

# a, b = map(int,input().split())
# dic = dict({1:1,2:2,3:3,4:2,5:1,6:2,7:3,8:3,9:2,10:1})

# def control(a,b):
#     count = 0
#     a, b = (b, a) if a > b else (a, b)
#     if a == b : return 0
#     while b - a > 10:
#         a += 10
#         count += 1
#     count += dic[b-a]
#     return count

# print(control(a,b))

# lst = [50000,10000,5000,1000,500,100,50,10]
# count = 0
# n = int(input())

# for i in lst:
#     if n >= i:
#         count += n // i
#         n %= i

# print(count)

# topping_count = int(input())

# dow_price, topping_price = map(int,input().split())

# dow_cal = int(input())

# topping_cal_lst = [int(input()) for _ in range(topping_count)]

# def quick_sort(lst):
#     if len(lst) == 0:
#         return lst
    
#     pivot = lst[len(lst)//2]
#     start = [x for x in lst if x > pivot]
#     middle = [x for x in lst if x == pivot]
#     end = [x for x in lst if x < pivot]

#     return quick_sort(start) + middle + quick_sort(end)

# new_topping_cal_lst = quick_sort(topping_cal_lst)

# for i in range(len(new_topping_cal_lst)):
#     pizza_total_price = (i+1) * topping_price + dow_price
#     pizaa_total_cal = dow_cal + new_topping_cal_lst[i]



# def fibo(n):
#     if n==0: return 0
#     elif n==1: return 1
#     else : 
#         return fibo(n-1)+fibo(n-2)
    

# num=int(input('피보나치 수열 F(N)의 N값을 입력 : '))
# print('F(',num,') = ',fibo(num))



# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else :
#         return fibo(n-2) + fibo(n-1)
    
# print(fibo(int(input())))


# n = int(input())

# def cal(temp):
#     if temp != 0:
#         cal(temp-1)
#         print(temp)
#     else:
#         return 0
# cal(n)

# n = int(input())

# def cal(temp):
#     if temp != 0:
#         print(temp)
#         cal(temp-1)
#     else:
#         return 0

# cal(n)

# m , n = map(int,input().split())

# def cal(m,n):
#     if m > n :
#         return 0
#     else:
#         if m % 2 == 1:
#             print(m)
#             cal(m+2,n)
#         else:
#             cal(m+1,n)

# cal(m,n)

# import sys
# sys.setrecursionlimit(1000000)

# n = int(input())

# def cal(temp):
#     if temp == 0:
#         return 0
#     else:
#         return temp + cal(temp-1)
# print(cal(n))

# n = int(input())

# def cal(n):
#     if n == 1:
#         return 1
#     else:
#         return n * cal(n-1)

# print(cal(n))

# n = int(input())
# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(n))

#1920 2진수 재귀
# n = int(input())

# def cal(n):
#     if n == 0:
#         return '0'
#     elif n == 1:
#         return '1'
#     else:
#         return cal(n // 2) + str(n % 2)

# print(cal(n))


# n = int(input())

# def cal(n):
#     print(n)
#     if n == 1: 
#         return 0
#     elif n % 2 == 0:
#         return cal(n // 2)
#     elif n % 2 == 1:
#         return cal(3 * n + 1)
# cal(n)


# n = int(input())

# def cal(n):
#     if n % 2 == 0:
#         cal(n // 2)
#         print(n)
#     elif n == 1:
#         print(n)
#         return 0
#     elif n % 2 == 1:
#         cal(n * 3 +1)
#         print(n)
# cal(n)

# n = int(input())

# def cal(n):
#     if n == 0:
#         return 0
#     else:
#         cal(n-1)
#         print('*'*n)
# cal(n)

# n = int(input())
# lst = [int(input()) for _ in range(n)]

# def quick_sort(lst):
#     if len(lst) == 0:
#         return lst
#     pivot = lst[len(lst)//2]
#     start = [x for x in lst if x < pivot]
#     middle = [x for x in lst if x == pivot]
#     end = [x for x in lst if x > pivot]

#     return quick_sort(start) + middle + quick_sort(end)

# for i in quick_sort(lst):
#     print(i)

# lst = [3, 6, 9]

# n = int(input())

# for i in range(n)

# n = int(input())
# lst = ['3','6','9']
# for i in range(1,n+1):
#     temp = 0
#     for j in str(i):
#         if j in lst:
#             temp +=1
#             continue
#     if temp == 0:
#         print(i,end=' ')
#     else:
#         print('X' * temp, end=' ')

# topping_count = int(input())

# dow_price , topping_price = map(int,input().split())

# dow_cal = int(input())

# topping_cal = [int(input()) for x in range(topping_count)]

# basic_dollar_per_cal = dow_cal / dow_price
# dollar_per_cal = 0



# def quick_sort(lst):
#     if len(lst) <= 0:
#         return lst
    
#     pivot = lst[len(lst)//2]

#     start = [x for x in lst if x > pivot]
#     middle = [x for x in lst if x == pivot]
#     end = [x for x in lst if x < pivot]
    
#     return quick_sort(start) + middle + quick_sort(end)

# sorted_topping_cal = quick_sort(topping_cal)
# optimal_idx = 0
# optimal_cal = 0
# for i in range(len(sorted_topping_cal)):
#     optimal_idx += 1

#     optimal_dollar_per_cal = (dow_cal + sum(sorted_topping_cal[:optimal_idx])) / ((optimal_idx * topping_price) + dow_price)
#     if optimal_dollar_per_cal > basic_dollar_per_cal:
#         basic_dollar_per_cal = optimal_dollar_per_cal

# print(int(basic_dollar_per_cal))


#2진수 재귀

# n = int(input())

# def cal(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return cal(n//2) + str(n%2)
    

# n = int(input())

# if n % 400 == 0 or (n % 4 == 0 and n % 100 !=0):
#     print('Leap')
# else:
#     print('Normal')

# m, n = map(int,input().split())

# n -= 30
# if n < 0:
#     n += 60
#     m -= 1
#     if m < 0:
#         m += 24

# print(m, n)

# n = input()
# temp = 0
# for i in n:
#     temp+=1
# print(temp)

# lst = [int(input()) for x in range(5)]
# print(max(lst))
# print(min(lst))

# n = int(input())

# lst = [x for x in range(1,n+1)]

# while len(lst) > 1:
#     lst.remove(int(input()))

# print(lst[0])

# def gcd_cal(a,b):
#     while b:
#         a, b = b, a % b
#     return a

# print(gcd_cal(33,66))

# n = int(input())

# def gcd_cal(a,b):
#     while b:
#         a, b = b, a % b
#     return a

# for i in range(n):
#     lst = list(map(int,input().split()))
#     gcd_lst = []
#     for j in range(1,lst[0]+1): 
#         for k in range(j+1,len(lst)): 
#             gcd_lst.append(gcd_cal(lst[j],lst[k]))
#     print(sum(gcd_lst))

# n = int(input())

# lst = [[0 for _ in range(1,20)] for _ in range(1,20)]

# for i in range(n):
#     x, y = map(int,input().split())
#     x, y = (x + 1, y + 1) if x == 0 or y == 0 else : 

# print(lst)

# x = y = 1

# ant_lst = [list(map(int,input().split())) for x in range(10)]

# while True:
    
#     ant_lst[x][y] = 9


#     if ant_lst[x][y] == 2:
#         break

#     if ant_lst[x+1][y] == 1:
#         y += 1
#         if y ==10:
#             break
#     elif ant_lst[x+1][y] == 0:
#         x += 1 
#         if x == 10:
#             break

# print(ant_lst)
