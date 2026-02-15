def show_menu():
    print("/n-- todo list manger ---")
    print("1. view tasks")
    print("2. add task")
    print("3. remvoe task")
    print("4. exit")

def main():
    tasks =[]

    while True:
        show_menu()
        choice = input("choose an option")
        if choice == '1':
            if not tasks:
                print("\nyour list is empty! go takw a nap.")
            else:
                print("\n your task:")
                for index, task in enumerate(tasks, start= 1):
                    print(f"{index}. {task}")
        elif choice =='2':
            new_task = input("what do you need to do ?")
            tasks.append(new_task)
            print("task added")

        elif choice == '3':
            if not tasks:
                print("nothing to remove")
                continue

            for index, task in enumerate(tasks,start=1):
                print(f"{index}.{task}")
            try:
                task_num = int(input("enter the task nmber to delete"))
                removed = tasks.pop(task_num -1)
                print(f"deleted:{removed}")

            except(ValueError, IndexError):
                print("invalid number please try again")
        elif choice =='4':
            print("goodbye!")
            break
        else:
            print("invalid choice, try again")
if __name__== "__main__":
    main()
# new feature 