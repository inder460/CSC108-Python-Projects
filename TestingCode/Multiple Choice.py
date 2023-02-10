num = int(input())
answer = ''
sol = ''
count = 0

if 0 < num < 10000:
    for i  in range(num):
        answer = answer + input()

    for j in range(num, 2*num):
        sol = sol + input()

    for i in range(num):
        if answer[i] == sol[i]:
            count = count + 1
print(count)


