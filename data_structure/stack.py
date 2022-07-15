#stack
new=[]
size=int(input("enter size"))
top=0

def push():
    global size,top
    if top>=size:
        print("stack is full")
    else:
        e=int(input("enter element"))
        new.append(e)
        top=top+1
        print(new)

def pop():
    global size,top
    if top<=0:
        print("stack is empty")
    else:
        new.pop()
        top=top-1
        print(new)


while True:
    m=int(input("select operation\n1 for push\n2 for pop"))
    if m==1:
        push()
    else:
        pop()