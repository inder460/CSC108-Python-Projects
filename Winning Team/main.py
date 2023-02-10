# prompt user for scoring categories of team apples and bananas
apple_three = int(input())
apple_two = int(input())
apple_one = int(input())

banana_three = int(input())
banana_two = int(input())
banana_one = int(input())

# calculate total points for both team apples and banana
apple_total = apple_three*3 + apple_two*2 + apple_one
banana_total = banana_three*3 + banana_two*2 + banana_one

if apple_total > banana_total:
    print('A')
elif apple_total < banana_total:
    print('B')
else:
    print('T')
