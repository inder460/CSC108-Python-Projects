def make_all_values_equal(d: dict, v : object)-> None:
    for k in d:
        d[k] = v

d = {'CSC':108, 'MAT':135, 'POL':112}

make_all_values_equal(d, 1234567)
print(d)

make_all_values_equal(d, "Hello")
print(d)