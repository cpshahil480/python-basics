students=[('anu',67),('amal',69),('arun',65)]
s=[]


while students:
    minimum=students[0]
    for i in students:
        if i<minimum:
            minimum=i

    s.append(minimum)
    students.remove(minimum)

print(s[0])


