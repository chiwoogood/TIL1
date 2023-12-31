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

lst = list(map(int, input().split()))

for i in range(len(lst)):
    min_idx = i  # 변수명 수정: min_idx로 변경
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[min_idx]:  # 부등호 방향 수정: 최소값을 찾아야 하므로
            min_idx = j

    lst[i], lst[min_idx] = lst[min_idx], lst[i]

print(lst)
