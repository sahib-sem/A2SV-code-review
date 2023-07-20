import heapq

'''
solution Idea - start from the highest beauty level and then up until you reach you k limit pick music with highest length but must have higher or equal beauty level
multipy the sum you get with the current beauty level then you maximize this result succesively going from the highest beauty level to the lowest 
'''
 
n , k = list(map(int, input().split()))
 
lst = []
for _ in range(n):
    l, b = list(map(int, input().split()))
    lst.append((b, l))
 
lst.sort()
arr = []
ans = 0
total = 0
for i in range(n - 1, -1 , -1):
    total += lst[i][1]
    heapq.heappush(arr,lst[i][1])
    ans = max(ans, total * lst[i][0])
    if n - i >= k:
        total -= heapq.heappop(arr)
 
print(ans)