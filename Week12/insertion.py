def insert(L: list, i: int) -> None:

    v = L[i]
    while v < L[i-1] and i >= 1:
        L[i] = L[i-1]
        i = i - 1
    L[i] = v


def insertion_sort(L: list) -> None:

    for i in range(1, len(L)):
        insert(L, i)


lst = input().split()
for j in range(len(lst)):
    lst[j] = int(lst[j])
print(lst)
insertion_sort(lst)
print(lst)