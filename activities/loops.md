### Question 1:
What is the output of the following code:

```
for i in range(8):
    print(i, end=" ")
```

<br><br><br>

### Question 2
What is the output of the following code:
```
mylst = [1,4,3,2,7]

for val in mylst:
    print(f'val = {val}')
```

<br><br><br>


### Question 3
What is the output of the following code:
```
mylst = ["hello", "goodbye", 1, 3, "platypus", 4, 2]
for i in range(len(mylst)):
    print(f'{i}, {mylst[i]}')
```

<br><br><br>

### Question 3
What is the output of the following code:
```
mylst = ["hello", "goodbye", 1, 3, "platypus", 4, 2]
for i in range(len(mylst)):
    print(f'{i}, {mylst[i]}')
```

<br><br><br>

### Question 4
What is the output of the following code:
```
for i in range(10):
    i += 1
    print(i)
```

<br><br><br>


### Question 5
Consider the following code:
```
for i in range(4):
    for j in range(5):
        print(f'({i},{j})', end=" ")
    print()
```

What is the output of the code?
<br><br><br>

How many times does the line `print(f'({i},{j})', end=" ")` execute?
<br><br><br>

### Question 6
Consider the following code:
```
def foo(n):
    for i in range(n):
        print('+' * n)

def bar(n1, n2):
    for i in range(n1):
        foo(n2)

bar(5,3)
```

How many times does `bar` get called when this code executes?
<br><br><br><br>

How many times does `foo` get called when this code executes?
<br><br><br><br>

What is the output of the above code?
<br><br><br><br>

### Question 7
Write a block of code using for loops
that prints given an odd number $n$
prints the following pattern of $n$ rows.
For example, for $n = 5$:

```
*
**
***
**
*
```

<br><br><br><br><br><br>


Repeat the same task using while loops:

<br><br><br><br><br><br>

Which would you prefer to use for this task?
<br><br><br>
