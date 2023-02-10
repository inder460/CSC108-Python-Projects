"""
Q4: Getting the Grade
5 marks


Michael is taking n courses this semester, numbered from 1 to n.
Each of these courses has a final exam. Unfortunately, these exams
are all held on the same day.

Michael has d days left to study for the exams. In each of these days,
he has exactly h hours of free time he can use to study (note that
h might be greater than 24 as Michael lives in a different universe with
a different time system).

Moreover, for the i-th course Michael is taking,
he has a learning rate l[i] indicating the number of marks he gets
on the exam per hour of studying for that course.
Michael studies for his exams in 1 hour blocks; for example,
he can't study for an exam for 40 minutes then switch to another one.

Note that in Michael's universe, final exam grades aren't
capped at 100. In fact, there's no upper limit on how high they can go.

If Michael takes an exam without studying for it, he'll get a 0 on that exam.

In order to qualify for a nice scholarship, Michael needs
to get at least m marks on each of the n exams. Help him out by telling
him whether it's possible to do so if he manages his time wisely.


## Input

- The first line contains a single integer t denoting the number of test cases.
  The description of the t test cases follow one by one.
- Each test case is described in 2 lines. The first line contains
  4 space-separated integers n, d, h, and m, respectively.
- The second line contains n space-separated integers, specifying the list l.


## Output

For each test case, print "Yes" if Michael can qualify
for the scholarship and "No" otherwise. Print these one per line, in the same order
that the test cases appear in the input.


## Constraints

- 1 <= t <= 5
- 1 <= n <= 1000
- 1 <= d <= 100
- 0 <= h <= 10**12
- 0 <= m <= 10**9
- 1 <= l[i] <= 10**9


## Note

The test cases for this question are designed such that any reasonable
correct solution should get roughly 90%, regardless of how
efficient it is.

However, to get 100%, your code needs to be fairly efficient as well
and finish running on any valid input (under the constraints above)
within a few seconds.

## Sample Input

```
3
3 3 2 50
25 62 20
5 8 3 60
11 61 9 33 29
2 1 2 50
49 51
```

## Sample Output

```
Yes
Yes
No
```

## Sample Explanation

- The first line of the input contains a single integer 3, indicating that
  there will be 3 test cases.

- In the first test case, there are 3 courses. Michael has 3 days to study
  for their exams. He has 2 free hours in each of those 3 days. Lastly,
  he needs to get at least 50 marks in each of the exams to qualify for
  the scholarship.
- The learning rates for the 3 exams are 25, 62, and 20.
- One way for Michael to get at least 50 marks in each exam is the following:
--- Study for course 3 one hour every day. He gets 20 marks an hour. That sums
    up to 60 marks, which is greater than 50.
--- Study for course 2 one hour on the first day. He gets 62 marks, which is enough.
--- Study for course 1 one hour on days 2 and 3. He gets 50 marks, which is just enough.
"""

# TODO Write your code here.
for x in range(int(input())):

    courses, days, hours, mark = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    total_hours = days * hours

    for temp in nums:

        if temp >= mark:
            total_hours -= 1

        else:
            total_hours -= (mark // temp)
            if mark // temp < mark / temp:
                total_hours -= 1

        if total_hours < 0:
            print("No")
            break

    else:
        print("Yes")
