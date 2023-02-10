def sort_dict(d):
    keys = list(d.keys())
    values = list(d.values())
    keys.sort()
    values.sort()
    print(keys)
    for x in values:
        if((x)%2==1):
            print(keys[x-1])


print(sort_dict({'c': 3, 'b': 2, 'a': 1, 'd': 4, 'e': 5}))


