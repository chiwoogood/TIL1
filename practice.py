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
lst = list(input())

for i in lst[:]:
    if i.isalpha() == False:
        lst.append(lst.pop(lst.index(i)))

print(lst)