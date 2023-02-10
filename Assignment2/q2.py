num_groups, students = [int(x) for x in input().split()]
groups = []
for x in range(num_groups):
    groups.append([])


def similar_names(name1, name2):
    diff_letter_seen = False
    name1 = name1.lower()
    name2 = name2.lower()
    if len(name1) == len(name2):
        for x in range(len(name1)):
            if name1[x] != name2[x]:
                if diff_letter_seen:
                    return False
                diff_letter_seen = not (diff_letter_seen)
        return True
    return False


for x in range(students):
    group, name = input().split()
    group = int(group) - 1
    for names in groups[group]:
        if similar_names(name, names):
            break
    else:
        groups[group].append(name)

for x in groups:
    print(" ".join(x))
