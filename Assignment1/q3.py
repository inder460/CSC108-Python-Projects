# prompt user for input
text = input()

# use string method replace
replaced_text = text.replace('.', ' .')
replaced_text2 = replaced_text.replace(' survey ', ' poll ', 3).replace(' poll ', ' survey ', 2)
replaced_text3 = replaced_text2.replace(' .', '.')

print(replaced_text3)