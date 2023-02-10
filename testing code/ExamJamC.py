import math


def form_teams(people: list[str], num_teams: int) -> list[list[str]]:
    x = len(people) / num_teams
    x = math.ceil(x)
    new = []
    counter = 0
    hello = []
    while counter <= x:
        if counter < x:
            hello.append(people[counter])
            people.pop(0)
            new.append(hello)
        else:
            counter = 0
            hello = []
        counter += 1
    return new


lst = ['paul', 'franc', 'andrew', 'sue', 'steve', 'arnold', 'tom', 'danny', 'nick', 'anna', 'dan', 'diane', 'mic',
       'jermey', 'karen']
form_teams(lst, 4)
