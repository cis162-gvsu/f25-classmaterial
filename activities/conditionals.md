### Question 1:
Suppose children aged 2 through 12 (inclusive) receive a discounted
rate of admission at an attraction.
Which of the following would be appropriate boolean expressions to check the age?


* `age > 1 or age < 13`
* `age >= 2 and age < 13`
* `age >=2 and age <= 12`
* `age > 1 and < 13`
* `1 < age <= 13`
<br><br>


### Question 2:
You are given the following code to check if someone
has an acceptable number of items for the quick self-checkout lane.

What is wrong with this code?  Identify as many issues as you can.

```
MAX_ITEMS = 12
qty = 5
if qty < MAX_ITEMS
    print(all good)
elif qty = MAX_ITEMS
    print(better hope you counted right!)
else
    print(too many)
```
<br><br><br>

### Question 3:

Consider the following expression:
```
x > 10 and y == 5 or z > x + y
```

For each of the following sets of values, what is the result
when evaluating the above expression?
* `x = 11`, `y = 5`, `z = 25.0`
* `x = 9`, `y = 5`, `z = 15`
* `x = 8`, `y = 3`, `z = 20`
<br><br><br><br><br><br>



### Question 3:

Consider the following two expressions:
Expression 1:
```
x / y > 5 and y > 0
```

Expression 2:
```
y > 0 and x / y > 5
```

Are these two expressions the same?
E.g. when evaluated, will they always give the same result?
<br><br><br><br>


### Question 4:
Are the following two snippets of code equivalent?  Why?

Code snippet 1:
```
fee=0
if(age < 14):
  fee=10
else:
  fee=15
```

Code snippet 2
```
fee=10
if(age >= 14):
  fee=15
```
<br><br><br><br>


### Question 5:
Consider the following code:
```
name = “98439hdw”
if product_id[-3:] == "hdw" or "HDW":
    print("The product code is hardware.")
else:
	print(“The product code is not hardware.”)
```

What do you think this code does?
<br><br><br><br>

What is the output of the above code?
<br><br><br><br>



Describe how you would test the above code works as expected?
<br><br><br><br>



Does it work as expected?  If not, why?
<br><br><br><br>

