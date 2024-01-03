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