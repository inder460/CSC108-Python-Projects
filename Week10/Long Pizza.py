n = int(input())
lst = input().split()
r = int(input())

x = int(lst[0])
y = int(lst[1])

diff_lst = [0]*(n+2)

for run in range(r):
    lst = input().split()
    l = int(lst[0])
    right = int(lst[1])

    diff_lst[l] = diff_lst[l] + 1
    diff_lst[right+1] = diff_lst[right+1] - 1

total = 0
ivals = 0
for i in range(y+1):
    ivals = ivals + diff_lst[i]
    if i>=x:
        total = total + ivals

print(total)