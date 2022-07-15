que=[]
size=int(input("enter size"))
top=0
def enqueue():
    global size,top
    if top>=size:
        print("queue is full")
    else:
        e=int(input("enter add digit"))
        que.append(e)
        top=top+1
        print(que)

def dequeue():
    global top,size
    if top<=0:
        print("queue is empty")
    else:
        que.remove(que[0])
        top=top-1
        print(que)


while True:
    m=int(input("choose operation\n1 for enqueue\n2 for dequeue"))
    if m==1:
        enqueue()
    else:
        dequeue()


