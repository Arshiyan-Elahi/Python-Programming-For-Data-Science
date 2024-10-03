# LEC 1

std1='MAC'
std2='QAS'

#Comparison 
print(std1==std2)
print(std1>std2)
print(std2>=std1)
print(std1!=std2)

a=20
b=20

print(f'Greator checker {a>b} ')
print(f'Less Than checker {a<b} ')
print(f'Equality checker {a==b} ')
print(f'Not Equality checker {a!=b} ')


#Length Function Counter 
def len_counter(string:str):
    counter=0

    for i in string:
        counter=counter+1

    return counter



d1 = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
d2 = {'class': 'B'}

d1.update(d2)
d1.popitem()


# with filter
l1=[87,89,72,63,55,78]
list1 = set(filter(lambda x:(x%2==0),l1))

# with map

l1=[87,89,72,63,55,78]
list = list(map(lambda x:(x*2),l1))
print(list)

class phone:
    def make_call(self):
        print('Making phone call')

    def game_play(self):
        print('playing game')    

    
    def color(self,color:str):
        print(f'The color is {color} ')    

    def cost(self,cost:int):
        print(f'The cost is {cost}')    

    



p1=phone()
p1.game_play()
p1.make_call()
p1.cost(24000)
p1.color('black')



class Student:
    students_list = []  # Class-level attribute to store all student data
    
    def __init__(self):
        # Input student details
        while True:
            name = input("Enter the name of the student: ")
            age = int(input("Enter the age of the student: "))
            dob = input("Enter the Date of birth of the student: ")
            dept = input("Enter the Department of the student: ")

            # Store the student's details in a dictionary
            student_info = {
                "name": name,
                "age": age,
                "dob": dob,
                "dept": dept
            }

            # Append the student info to the class-level list
            Student.students_list.append(student_info)

            # Ask if the user wants to input more data
            usr = input('Do you want to input more data for another student? (Y/N): ')
            if usr.lower() != 'y':
                break  # Exit loop if the user says 'N' or anything other than 'Y'

    
      
    def show_details(self):
                
                print("All STUDENTS LIST: ")
                for students in Student.students_list:
                    print('----------------------')
                    print('Student Name is:',  students['name'] )
                    print('Student Age is:', students['age'])
                    print('Student DOB is:', students['dob'])
                    print('Student Department is:', students['dept'] , '\n' )
                






s1=Student()
s1.show_details()
print('----------------------')









class Employee:
    employee=[]
    def add_employee(self):
        id=int(input("Enter id of the employee: "))
        name=input("Enter name: ")
        age=int(input("Enter age: "))
        dept=input("Enter dept: ")
     
        emp_info={
            'id':id,
            'name':name,
            'age':age,
            'dept':dept
        }    

        Employee.employee.append(emp_info)        
        print(f"\n✅ Employee {name} added successfully!")
        print('----------------------------------')

    def remove_employee(self):
        print('Employeer list ',Employee.employee)
        usr=int(input('Enter the ID of the student you want to delete: '))
        for index, employeer in enumerate(Employee.employee):
            if usr ==  employeer['id']:
                del Employee.employee[index]  # Remove the entire dictionary
                print(f"\n✅ Employee {usr} deleted successfully!")
                break
        else:
            print(f"\n❌ No employee found with ID {usr}.")
            

        print('Employeer list ',Employee.employee)            


    def update_employee(self):
        # Display the employee list with their details
        print('Employee List: ')
        for employee in Employee.employee:
            print(employee)  # Show employee details

        try:
            # Ask for the employee's ID to update
            emp_id = int(input("Enter the ID of the employee you want to update: "))

            # Find the employee with the matching ID
            for employee in Employee.employee:
                if employee['id'] == emp_id:
                    # Ask the user what they want to update (name, age, or department)
                    user = input('What do you want to update (1. Name, 2. Age, 3. Dept): ')
                    
                    if user == '1':
                        new_name = input("Enter the new name: ")
                        employee['name'] = new_name  # Update the name
                        print(f"✅ Name updated to {new_name}!")

                    elif user == '2':
                        new_age = int(input("Enter the new age: "))
                        employee['age'] = new_age  # Update the age
                        print(f"✅ Age updated to {new_age}!")

                    elif user == '3':
                        new_dept = input("Enter the new department: ")
                        employee['dept'] = new_dept  # Update the department
                        print(f"✅ Department updated to {new_dept}!")

                    else:
                        print("❌ Invalid choice. No updates made.")
                    break  # Exit the loop once the employee is found and updated
            else:
                print(f"❌ No employee found with ID {emp_id}.")

        except ValueError:
            print("❌ Please enter a valid ID.")

        print('----------------------------------')
        print('Updated Employee List:', Employee.employee)



    def show_details(self):
        print('Employeer list ',Employee.employee)
        field = int(input("Enter the ID number of the employee you want to see the details of: "))
        
        # Loop through the employee list to find the employee with the matching ID
        for i in Employee.employee:
            if i['id'] == field:  # Check if the ID matches
                print("Complete Details of the Employee:")
                print(f"Employee ID: {i['id']}")
                print(f"Employee Name: {i['name']}")
                print(f"Employee Age: {i['age']}")
                print(f"Employee Department: {i['dept']}")
                break
        else:
            print(f"\n❌ No employee found with ID {field}.")
        print('----------------------------------')
         
                
    def menu(self):
        while True:
            print("\n======== VIP Employee Management Menu ========")
            print("1. Add Employee")
            print("2. Show Employee Details")
            print("3. Update Employee")
            print("4. Remove Employee")
            print("5. Exit")

            choice = input("\nEnter your choice (1-5): ")

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.show_details()
            elif choice == '3':
                self.update_employee()
            elif choice == '4':
                self.remove_employee()
            elif choice == '5':
                print("\n👋 Exiting Employee Management. Goodbye!")
                exit()
            else:
                print("\n❌ Invalid choice, please try again.")


if __name__ == "__main__":
    emp = Employee()  # Create an instance of Employee
    emp.menu()        # Call the menu function to start the program
                

n = int(input("Enter a number: "))
for i in range(0, n):        # Outer loop from 0 to n-1
    for j in range(1, n-i+1):  # Inner loop from 1 to n-i
        print(j, end=" ")      # Print numbers in the row
    print()  # New line after each row


# Write a program that takes an integer n as input and 
# calculates the factorial of that number using a for loop

# 1x2x3x4x5


# Taking input from the user
n = int(input("Enter a number: "))

# Initializing the factorial result to 1
factorial = 1

# Using a for loop to calculate the factorial
for i in range(1, n+1):
    factorial = factorial * i
  # Multiply factorial by i in each iteration

# Printing the result
print(f"The factorial of {n} is: {factorial}")


n=int(input("Enter no: "))
sums=1

for i in range(2,n+1,2):
    # sums=i
    sums=sums*i

print(sums)    

        

'''

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1



 '''


counter = 0
while True:
    rows = int(input("Enter rows: "))
    col = int(input("Enter col: "))
    symbol = input("Enter Symbol: ")

    for col in range(rows, 0, -1):
        for j in range(col, 0, -1):
            print(symbol, end=' ')
        print()

    # Increment counter after each game round
    counter += 1

    usr = input("Do you want to play again: (Y/N)? ")
    if usr.lower() != 'y':
        break

print(f'You played {counter} times')
    

# Sample customer feedback dataset as lists
customer_ids = [101, 102, 103, 104, 105]
feedback = [
    "  Excellent service and fast delivery!!   ",
    "Horrible support, never ordering again...",
    "Great quality but packaging was bad. ",
    "    Amazing product, will recommend.    ",
    "Not happy with the product!   "
]

#Display the original dataset
print("Original Dataset:")
for i in range(len(feedback)):
    print(f"CustomerID: {customer_ids[i]}, Feedback: {feedback[i]}")


# Step 1: Strip extra spaces around the feedback
feedbacks = [fb.lower().strip() for fb in feedback]

import re
feedbacks = [re.sub(r'[^a-zA-Z0-9\s]', '', fb) for fb in feedbacks]

printcontains_good = ['good' in fb or 'excellent' in fb for fb in feedbacks]
printcontains_bad=['bad'in fb   or     'worst' in fb or  'not recommended'in fb  for fb in feedbacks]





customer_ids = [101, 102, 103, 104, 105,106]
feedback = [
    "  Excellent service and fast delivery!!   ",
    "Horrible support, never ordering again...",
    "Great quality but packaging was bad. ",
    "    Amazing product, will recommend.    ",
    "Not happy with the product!   ",
    " happy with the product!"
]



feedbacks=[fb.strip().lower() for fb in feedback]
for i in feedbacks:
    print(i)


val = input("Enter No: ")
pos = int(input("Enter Pos: "))
# print(val[pos] if 0 <= pos < len(val) else "Invalid position")
digit=val[pos]

print(digit)





'''
Sum of Digits:
Write a program that asks the user to enter a number. 
Convert that number to an integer, and then calculate the sum of its digits using a loop
'''

user=input("Enter No: ")
digit=[]
for num in user:
    digit.append(int(num))

print(sum(digit))


        
user_no=int(input("Enter a No: "))

if user_no%2==0:
    print(f"It is even no {user_no}")

else:
    print(f"It is odd no {user_no}")

usr=int(input("Enter table no: "))
for i in range(1,11):
    print(f'{usr} x {i} = {usr*i}')

'''

## Task for Students: Budget-Based Decision Making

Write a Python program that performs the following steps:

- Ask the user to input their budget.
- If the budget is more than 1000, print "Mutton" (indicating the user can afford 1 kg of meat).
- If the budget is more than 500 but less than or equal to 1000, print "Eggs" (indicating the user can afford 12 eggs).
- If the budget is 500 or less, print "keep fast" 
'''

budget=int(input("Enter your Budget: "))

if budget>1000:
    print(f"You can eat Mutton in this {budget} budget")

elif (budget>=500 and budget<=1000):
    print(f"You can eat Eggs in this {budget} budget")

elif (budget<500) :
    print(f"You can keep Fast in this {budget} budget")

