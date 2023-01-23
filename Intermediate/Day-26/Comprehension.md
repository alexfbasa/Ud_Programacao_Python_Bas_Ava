# Comprehension 
## # List Comprehension  

```text
For loop 
```
```commandline
numbers = [1, 2, 3]
plus_one = [new_each_number(do something) for each_number in list]
plus_one = [n + 1 for n in numbers]
plus_one = [2, 3, 4]
```
```text
Conditional with IF

```
```commandline
new_list = [new_item for item in list if {condition}
new_list = [n for n in list if n % 2 == 0]
names = ['Alexandre', 'Carla', 'Rodrigo', 'Hiago']
name_owner = [name for name in names if name == 'Alexandre']
```
```text
name_owner = {list: 1} ['Alexandre']
 0 = {str} 'Alexandre'
 __len__ = {int} 1
```
```commandline
names = ['Alexandre', 'Carla', 'Rodrigo', 'Hiago']
names_upper = [name.upper() for name in names] 
names_upper = {list: 4} ['ALEXANDRE', 'CARLA', 'RODRIGO', 'HIAGO']
```text
 long_names = [name.upper() for name in names if len(name) > 5]
 long_names = {list: 2} ['ALEXANDRE', 'RODRIGO']
 0 = {str} 'ALEXANDRE'
 1 = {str} 'RODRIGO'
 __len__ = {int} 2
```
## Dict Comprehension  
```text
new_dict = {new_key:new_value for (key,value) in dict.items()}
```
```commandline
names = ['Alexandre', 'Carla', 'Rodrigo', 'Hiago']
students_random_score = {student:random.randonint(1, 100) for student in names}
```
```text
print(students_random_score)
{'Alexandre': 34, 'Carla': 26, 'Rodrigo': 87, 'Hiago': 32}
```
```commandline
new_dict = {student:score for (student, score) in students_random_score.items() if score >= 60}
```
```text
new_dict = {dict: 1} {'Rodrigo': 87}
 'Rodrigo' = {int} 87
 __len__ = {int} 1
```