#2512 예산
import sys
input = sys.stdin.readline

n = int(input())
rq = list(map(int, input().split()))
total = int(input())

rq.sort()

for i in range(n):
    if i == n-1:
        res = rq[i]
        break
    elif total//(n-i) >= rq[i]:
        total -= rq[i]
        continue
    elif total//(n-i) < rq[i]:
        res = total//(n-i)
        break

print(res)

#2512 예산_다른 사람의 코드
import sys
input = sys.stdin.readline

n = int(input())
rq = list(map(int, input().split()))
budgets = int(input())
start, end = 0, max(rq)

while start <= end:
    mid = (start+end) // 2
    total = 0
    for i in rq:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= budgets:
        start = mid + 1
    else:
        end = mid - 1

print(end)

# while start < end:
#     mid = (start+end) // 2
#     total = 0
#     for i in rq:
#         if i > mid:
#             total += mid
#         else:
#             total += i
#     if total <= budgets:
#         start = mid + 1
#     else:
#         end = mid - 1