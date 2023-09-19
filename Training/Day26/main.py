import random

names = ["Alex", "Ana", "Julia", "Pedro", "Roberto"]

students_scores = {name: random.randint(1, 100) for name in names}

passed_students = {name: value for name, value in students_scores.items() if value >= 60}

print(passed_students)