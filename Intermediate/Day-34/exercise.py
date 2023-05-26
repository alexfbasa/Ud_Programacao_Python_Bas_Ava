def police_check(age: int) -> bool:
    if age >= 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


can_i = police_check(18)
print(can_i)
