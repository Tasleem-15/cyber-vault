tasks=[]
while True:
    print("1.Add task")
    print("2.view task")
    print("3.remove task")
    print("4.exit task")
    choice = int(input("Enter your choice: "))
    if choice==1:
        task=input("enter the task :")
        tasks.append(task)
        print("task")
    elif choice==2:
        task=input("enter the task : ")
        print("task",tasks)
    elif choice==3:
        task=input("enter the task remove : ")
        if tasks in task:
            task.remove(task)
            print("task removed")
        else:
            print("task not found")
    elif choice==4:
        print("exit task")
    break
else:
    print("invalid task")