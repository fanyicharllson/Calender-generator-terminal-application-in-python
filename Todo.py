#To do list application with file in python

def view_task():
    with open("shome.txt", "r") as files:
        content = files.readlines()
        for line in content:
            print(line)
            line.strip()
        

def add_task():
    print("\n")
    print("\t....Add task menu....")
    with open("shome.txt", "a") as doc:
       number = input("How many tasks do you want to add? ")
       if number.isdigit():
           number = int(number)
           for _ in range(number):
               task = input("Enter task {}: ".format(_+1))
               doc.write(task + "\n")
           print("\n") 
           print("Task added successfully!") 
                            
        
       else:
           print("Enter only numbers!")   

        
def remove_task(name_file):
     with open("shome.txt","r") as file:
        content = file.readlines()

     match_found = False    
     with open("shome.txt","w") as file:
         for line in content:
            if name_file not in line:
                file.write(line)
                
            else:
                match_found = True
   
     if not match_found:
         print("Task not found ")
     else:
         print("Task deleted successfull.")    
         
          

def mark_task():
    try:
        with open("shome.txt", "r") as file:
            lines = file.readlines()

        with open("shome.txt", "w") as file:
            task_index = int(input("Enter the index of the task you want to mark as read: "))
            if task_index < 1 or task_index > len(lines):
                print("Invalid task index!")
                return
            
            for index, line in enumerate(lines):
                if index == task_index - 1: #task index -1 because python reads from 0 
                    line = line.strip() + " [Read]\n"
                file.write(line)
        
        print("Task marked as read successfully!")

    except ValueError:
        print("Invalid input! Please enter a valid index.")
    except FileNotFoundError as err:
        print(err)
        print("An error occurred! Please come back later.")



def main():
 print("\n")   
 print("                                               =========================")
 print("                                                 To-Do List Application ") 
 print("                                               =========================") 
 while True: 
  print("\n")           
  print("1) Add Task")
  print("2) View Task")
  print("3) Remove Task")
  print("4) Mark task as read")
  print("5) Exit")
  try: 
    choice = int(input("Enter your choice(1-4): "))
    if choice == 1:
        add_task()  
        
    elif choice == 2:
        try:
            with open("shome.txt", "r") as file:
                content = file.read()
                if not content.strip():
                    print("No Task added yet.")
                    print("Add task...")
                    quit()
                
                else:
                 view_task()   
        
        except FileNotFoundError as err:
            print(err)
            print("An error occurred! please come back later.")  
            quit()       
        # break 
    elif choice == 3:
         try:
            with open("shome.txt", "r") as file:
                content = file.read()
                if not content.strip():
                    print("No Task added yet.")
                    print("Add task...")
                    quit()
                
                else:
                 name_file = input("Enter the name of the task you want to remove: ")   
                 remove_task(name_file)   
        
         except FileNotFoundError as err:
            print(err)
            print("An error occurred! please come back later.")  
            quit()
                  
        
    elif choice == 4:
        mark_task()
        break
    elif choice == 5:
        print("Thankyou for using this To-Do list aplication")
        quit()       
    else:    
        print("Invalid Number!")
        print("Enter only numbers between 1 to 4")    
  except ValueError as err:
       print("\n")
       print(err)
       print("Enter only numbers!")


if __name__ == '__main__':
    main()        
                