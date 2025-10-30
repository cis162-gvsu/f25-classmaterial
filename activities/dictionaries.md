## Dictionaries

Consider the following dictionary:

```
populations = {'CA': 39431263,
               'TX': 31290831,
               'MI': 10140459,
               'IL': 12710158,
               'NY': 19867248,
               'PA': 13078751,
               'OH': 11883304,
               'TN': 7227750,
               'WI': 5960975,
               'IN': 6924275,
               'GA': 11180878,
               'MD': 6263220,
               'MO', 6245466,
               'NM', 2130256,
               'MA': 1405012,
               'MT': 1137233}
```

### Question 1
What line of code would you use to access the population for MI
and store it in a variable named `mi_pop`?
<br><br><br>

### Question 2
What would happen/output if you run the following line of code:
```
print(populations['RI'])
```
<br><br>

### Question 3
What would happen/output if you run the following line of code:
```
print(populations.get('RI', -1)
```
<br><br>

### Question 4
Write a function named `get_population_sums` that takes
in the populations dictionary and returns a new dictionary
containing three entries, one for `'big_states'` (those with
populations over 10,000,000), one for `'medium_states'` (those with
populations between 5,000,000 and 10,000,000) and `'small states'`
(those with populations less than 5,000,000).
<br><br>

