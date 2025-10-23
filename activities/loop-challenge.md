## Rules
You as a class have to work together
(without computers, phones, any tech devices, etc.)
to determine the output (it's okay if you're wrong)
and convince me **why** that is the output.

## Challenge 1
What is the output of the following code?
```
def bar(i, val, lst):
    if i % 2 == 0:
        lst.insert(len(lst),val)
        lst.insert(len(lst),val)

print('challenge 1')
lst = [1,2,3,4,5,6,7]
for i in range(len(lst)):
    val = lst[i]
    lst.pop(0)
    print(f'i={i}, val={val}, lst={lst}')
    bar(i, val, lst)
    print(f'i={i}, val={val}, lst={lst}')
```
<br><br><br><br>

## Challenge 2
What is the output of the following code?
```
def foo(i, val, lst):
    if i < 4:
        lst.insert(len(lst), val)

print('challenge 2')
lst = [1,2,3,4,5,6,7]
for i in range(len(lst)):
    val = lst[i]
    lst.pop(0)
    print(f'i={i}, val={val}, lst={lst}')
    foo(i, val, lst)
    print(f'i={i}, val={val}, lst={lst}')
```
