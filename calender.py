#Calender Generate project
import calendar

def generate_month(year, month):
    leap_year = calendar.isleap(year)
    print(calendar.month_name[month], year)
    print("Mo Tu We Th Fr Sa Su")
    month_calender = calendar.monthcalendar(year, month)
    for week in month_calender:
        for day in week:
            if day == 0:
                print(" ", end=" ")
            
            else:
                print(f"{day:2}", end=" ")
                
        
        print()                
    

def main():
    year = int(input("Enter the year for the month: "))
    month = int(input("Enter the month(1-12. Enter their corresponding numbers only): "))
    generate_month(year, month)




def generate_calender(year):
    choice = input("Do want to display all the calender for the year(yes or no): "+ str(year)+": ")
    if choice.lower() == "yes": 
      leap_year = calendar.isleap(year)
      for month in range(1,13): 
        print(calendar.month_name[month], year)
        print("Mo","Tu","We","Th","Fr","Sa","Su")
        month_calender = calendar.monthcalendar(year, month)
        for week in month_calender:
            for day in week:
                if day == 0:
                    print("  ", end= " ")
                
                else:
                    print(f"{day:2}", end=" ")   
                    
                
            print()    
        
        print() 
     
     
      
                      
                    
    
    
    elif choice.lower() == "no":
        print("\n\tSingle Month generated calender!")
        input("Press enter to procceed ")
        main()
              
        
        
    
    else:
        print("Invalid option!") 

    

def signin():
    with open("password.txt", "a") as doc:
        username = input("Enter your user name(Enter single username): ")
        for i in username:
             if " " in i:
                print("Enter only single username with no space!")
                quit()  
                 
        password = input("Enter your password: ")
        doc.write(username + " = " + password + '\n')         
    print("Successfully signed in")  
    log = input("Do you want to login now(yes or no): ").lower()
    if log == "yes":
        Login()
    else:
        print("Thankyou for signing in to this calender")
        quit()    

def Login():
    
        user_username = input("Enter username: ")
        user_password = input("Enter your password: ")
        with open("password.txt","r") as doc:
          match_found = False  
          for line in doc:
             username, password = line.strip().split(" = ")
             if user_username == username and user_password == password.strip():
                 match_found = True
                 break
        
        if match_found:
         print("Username and password correct")
         choice = input("\tDo you want to view calender now(yes or no): ")
         if choice == "yes":
            print("\n\tWelcome to calender........")
            try:
                year = int(input("Enter the year: "))
                generate_calender(year)
            
            except ValueError as err:
                        print(err)
                        print("Don't enter strings and decimal numbers")
                        quit()
        
         else:
                    print("Thankyou for logging in!")
                    quit()                     
        
        else:
            print("Invalid username and password") 
            
              
            

def forgotpassword():
    print("\t Forgot password...")
    username = input("Enter your user name:  ")
    with open("password.txt", "r") as file:
        match_found = False
        for line in file:
           if username in line:
               match_found = True
               break
        
        if match_found:
            print("Password found!")
            print(line)
        
        else:
            print("Password not found!")
            print("Ensure you have entered the right user name!")       
               
               
                 

               
         
print("\tYour Automatic Generate Calender...")
print("Choose from the option below")
print("1) Sign in to calender")
print("2) Login to calender")
print("3) Forgot password")
print("4) exit")

option = input("Enter your choice here be it in word or the number: ").lower()
if  option == "sign in to calender":
    signin()

if option.isdigit():
    option = int(option)
    if option == 1:
        signin()   
    elif option == 2:
        Login()
    elif option == 3:
        forgotpassword()
    elif option == 4:
        quit() 
    else:
        print("Invalid Number!")       

elif option == "login to calender":
    Login()
elif option == "forgot password":
    forgotpassword()  

elif option == "exit":
    quit()       
else:
    print("Invalid option!")            
            
             

