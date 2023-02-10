def num_pizzas(earthlings: int, andalites: int, martians: int) -> int:
    '''
    Earthlings order 2 slices of pizza, Andalites order 3 slices, and
    Martians order 1 slice

    Return the number of pizzas required for the given number of Earthlings,
    Andalites and Martians

    >>> num_pizzas(1,2,3)
    2
    '''
    total_slices = earthlings*2 + andalites*3 + martians
    total_pizzas = (total_slices+7)//8
    return total_pizzas