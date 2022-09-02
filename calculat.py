# Program make a simple calculator

from secrets import choice


def add(x, y):
    return x + y

def sub (x , y):
    return x - y
def multipy (x ,y):
    return x * y
def divide (x, y):
        return x/y

print ('Select the oporation ...') 
print ("1.add")
print ("2.sub")
print ("3.multipy")
print ("4.divide") 

while True:
    choice = ("Enter the choice (1 / 2/ 3 / 4):  ") 
      
    if choice in ('1', '2','3','4'):
        num1 = float (input('Enter the first number..:  '))
        num2 = float (input('Enter the second number.:  '))

        if choice == '1':
            print(num1, '+',num2, '=', add (num1,num2))
        elif choice == '2':
            print (num1,'-',num2, '=', sub (num1,num2))
        elif choice ==  '3':
            print(num1,'*',num2,'=',multipy(num1,num2))
        elif choice == '4':
            print(num1,'/',num2,'=',divide(num1,num2))
            next_calculation = input("Lets do next calculation ? (yes/no)")
            if next_calculation == "no":
                break
        else:
            print("Invalide Input enterd by the user")    