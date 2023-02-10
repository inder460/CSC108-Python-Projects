"""
Q1: Short Answer
4 marks


For Parts A and B, you are being marked not only on correctness but also on simplicity.
The allowed operators are those that we have used in the course.

A. 1 mark
Suppose that x and y are variable names that already refer to Boolean values.
Write an expression (not a statement!) that evaluates to True iff at least one
of the variables is False.

# TODO: Write your expression here
answer = not(x and y)


B. 1 mark
Suppose that x, y, and z are variable names that already refer to Boolean values.
Write an expression (not a statement!) that evaluates to True iff
at least two of the three variables (x, y, z) are True.

# TODO: Write your expression here
answer = (x and y) or (y and z) or (x and z)


C. 2 marks
Consider the following function headers and type contracts:

def aragorn(x: int, y: str, z: float) -> str:

def gandalf(x: list) -> list:

def elrond(x: list, y: bool) -> bool:

If the following code runs without errors, what is a header and type contract
for treebeard?

a = aragorn(11, 'good', 2.0)
b = treebeard(5, gandalf([1, 2, 3]), a)
print(elrond(gandalf([4, 5]), b))

# TODO: Write the header and type contract for treebeard.
def treebeard(x: int, y: list, z: str) -> bool:


"""
