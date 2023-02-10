hero_num = int(input())
superheros = input().split()

intel_num = input().split()
for i in range(len(intel_num)):
    intel_num[i] = int(intel_num[i])
strength_num = input().split()
for i in range(len(strength_num)):
    strength_num[i] = int(strength_num[i])

level3Hero = []
for i in range(len(strength_num)):
    level3Hero.append(strength_num[i] + intel_num[i])

villain_num = int(input())

vill_count = 0
villains = []
while vill_count < villain_num:
    villain_type = input().split()
    villain = []
    for i in range(len(villain_type)):
        villain_type[i] = int(villain_type[i])
        villain.append(villain_type[i])
    villains.append(villain)
    vill_count += 1

min_diff = 3183194676731478154

superIndex = []
printName = []
sorted_intel_num=intel_num[:]
sorted_strength_num=strength_num[:]
sorted_level3Hero=level3Hero[:]

sorted_intel_num.sort()

sorted_strength_num.sort()

sorted_level3Hero.sort()


for i in range(len(villains)):
    min_diff = 3183194676731478154
    if villains[i][0] == 1:
        x = villains[i][1]
        # print(x)
        for k in range(len(intel_num)):
            # print(intel_num[k])
            if intel_num[k] == x:
                printName.append(superheros[intel_num.index(intel_num[k])])
                break
            elif intel_num[k] > x:
                diff = x - intel_num[k]
                if diff < min_diff:
                    min_diff = diff
                    x = intel_num[k]
                    printName.append(superheros[intel_num.index(intel_num[k])])
                break
        if max(intel_num)<x :
           printName.append("none")


    elif villains[i][0] == 2:
        min_diff = 3183194676731478154
        x = villains[i][1]
        # print(x)
        for k in range(len(strength_num)):
            # print(strength_num[k])
            if sorted_strength_num[k] == x:
                printName.append(superheros[strength_num.index(sorted_strength_num[k])])
                break
            elif sorted_strength_num[k] > x:
                diff = x - sorted_strength_num[k]
                if diff < min_diff:
                    min_diff = diff
                    #  x = sorted_strength_num[k]
                    printName.append(superheros[strength_num.index(sorted_strength_num[k])])
                break
        if max(strength_num) < x:
            printName.append("none")
    else:
        min_diff = 3183194676731478154
        x = villains[i][1]
        for k in range(len(level3Hero)):
            if sorted_level3Hero[k] == x:
                printName.append(superheros[level3Hero.index(sorted_level3Hero[k])])
                break
            elif sorted_level3Hero[k] > x:
                diff = x - sorted_level3Hero[k]
                if diff < min_diff:
                    min_diff = diff
                    printName.append(superheros[level3Hero.index(sorted_level3Hero[k])])
                    break
        if max(level3Hero) < x:
            printName.append("none")
print(' '.join(printName))
