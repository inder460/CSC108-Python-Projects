s = 'hello#jkjjkjkjkjnd#'

x = s.index('#')
s = s[x+1:]
x = s.index('#')
slice = s[:x]
print(slice)



