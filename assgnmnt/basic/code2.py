def grade(n1):
    if n1>100:
        return "invalid"
    elif n1>=90:
        return "A+"
    elif n1>=80:
        return "A"
    elif n1>=70:
        return "B"
    elif n1>=60:
        return "C"
    elif n1>=50:
        return "D"
    else:
        return "fail"

print(grade(10))