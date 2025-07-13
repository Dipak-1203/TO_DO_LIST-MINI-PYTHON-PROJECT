def task():
    tasks = []  # empty list to store tasks
    print("-------Welcome to the task manager-------")
     
    total_tasks = int(input("Enter the number of tasks you want to add: "))
    for i in range(1,total_tasks+1):
        task_name = input(f"Enter the name of task {i}: ")
        tasks.append(task_name)

    print(f"\nHere are your tasks: {tasks}") 
    
    while True:
        opration = int(input("1 - add\n 2 - update\n 3 - delete\n 4 - view\n 5 - exit == "))
        if opration == 1:
            add = input("Enter the name of the task to add: ")
            tasks.append(add)
            print(f"Task '{add}' added successfully.")
        elif opration == 2:
            update_val = input("Enter the task name you want to update : ")
            if update_val in tasks:
                up=input("Enter the new task name: ")
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"Task  updated to '{up}'.")
                
        elif opration == 3:
            del_vel=input("which task you want to delete = ")                   
            if del_vel in tasks:
                ind = tasks.index(del_vel)
                del tasks[ind]
                print(f"task{del_vel} deleted conform")

        elif opration == 4:
            print("Here are your tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")           
                
        elif opration == 5:
            print("closing the program.....")
            break        
        
        else:
            print("invid input.....")
            
task()
                         
            