def num_vowels(s: str) -> bool:
    num_vowel = 0
    for i in s:
        if i in 'AEIOUaeiou':
            num_vowel += 1
    return num_vowel(s) > 0

"""
A complete search algorithm is when all candidate solutions are found and the best one is chosen. We see this used in the lifeguard problem in the textbook. 

First, write a function that solves the problem for a particular candidate solution. Second, call the function to test. 

bisect_right
bisect_left

definitely question 1 from the reading quiz. I am not sure if I am misunderstanding something or simply just don't understand it but more clarification would be nice. 

"""


