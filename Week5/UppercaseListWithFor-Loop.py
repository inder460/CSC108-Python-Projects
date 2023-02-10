give_lst = input().split(' ')
uppercase_lst = []
string = ''
for i in give_lst:
    string = i.upper()
    uppercase_lst.append(string)
print(give_lst)
print(uppercase_lst)

# above code runs without modifying original list
# the one below will be done with modifying the list

lst = input().split()
print(lst)
for i in range(len(lst)):
    lst[i] = lst[i].upper()
print(lst)

