def find_min(L: list, i: int) -> int:

    smallest_index = i

    for j in range(i+1, len(L)):
        if L[j] < L[smallest_index]:
            smallest_index = j
    return smallest_index


def selection_sort(L: list) -> None:

    for i in range(len(L)-1):
        smallest_index = find_min(L, i)
        L[i], L[smallest_index] = L[smallest_index], L[i]


lst = input().split()
for j in range(len(lst)):
    lst[j] = int(lst[j])
print(lst)
selection_sort(lst)
print(lst)