### Question 1:
Consider the following code:

```
def mystery1(a, b):
    if a <= 0 and b <= 0:
        return 0
    elif a > b:
        return a
    else:
        return b

def mystery2(x, y, z):
    result1 = mystery1(x, y)
    result2 = mystery1(y, z)
    result3 = mystery1(x, z)
    return result1 + result2 + result3

p = 5
q = -3
r = 2
result1 = mystery2(p, q, r)
result2 = mystery2(r, q, p)
```

In the above code, identify which lines have:
* function definitions
* function calls
<br><br><br>


When this code runs, how many times does:
* `mystery1` get called?
* `mystery2` get called?

<br><br><br>

How many lines of output does this code print?

<br><br><br>

After this code finishes running, what is the value of
* `result1`?
* `result2`?
<br><br><br>


### Question 2
Write a function that takes in a string and 
returns the string with the first letter swapped with 
the last letter and the second letter swapped with
the second to last letter.

The function should return the string with the letters swapped.
If the string does not have at least 4 letters, the function should
return the string `"invalid input"`.

