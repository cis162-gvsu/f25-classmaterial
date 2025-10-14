### Question 1:
What is the output of the following code?

```
for i in range(8,5,-1):
    print(i)
```

<br><br><br>

### Question 2
What is the output of the following code?
```
mylst = ["hello", "goodbye", 1, 3, "platypus", 4, 2, -4, 100]
for i in range(1, len(mylst), 2):
    print(f'{i}, {mylst[i]}')

```

<br><br><br>


### Question 3
What is the output of the following code?
```
x = 10
while x < 20:
    print(x)
    x += 2
```

<br><br><br>

### Question 4
What is the output of the following code?
```
val = 0
while val > 10:
    print(val)
    if val % 2 == 1:
        val += 1
    else:
        val *= 2
```

<br><br><br>


### Question 5
What is the output of the following code?
```
mylst = ["hello", 1, 3, "platypus",
         4, "green eggs and ham", 100,
         1, 8, 'stop']
idx = len(mylst)
while mylst[idx] != 'green egss and ham':
    print(idx, mylst[idx])
    idx -= 1
```

<br><br><br>


### Question 6
Write a block of code that counts up the number
of even numbers in a list and prints the count.
<br><br><br><br><br>

### Question 7
Write a function that takes in two lists,
`needle` and `haystack` and identifies
whether `needle` is a consecutive sublist 
(meaning occurs next to each other) of `haystack`.
Return `True` if `needle` is in `haystack`
and `False` if it is not.

For instance:
```
needle = [1,3,5]
haystack = [1,2,7,1,5,3]
```
would give `False`.

On the other hand
```
needle = [1,3,5]
haystack = [1,2,7,1,3,5,8,10]
```
would give `True`.


<br><br><br><br><br><br>

