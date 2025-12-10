# assignment part-1
#1. write a print statement to display 
print("Hello, I am learning Python")
#print the following on one line using sep
print(10,20,30,40,sep="-")
#print "python" and  "programming" on the same line without using two print statements
print("python programming")
#2 input three different variables for different data types and print the data
name = input("enter ur name")
age = int(input("enter ur age"))
height = float(input("enter ur height"))
print("name: ",name)
print("age: ",age)
print("height: ",height)
#3 Evaluate each expression on ur notebook and check whether it is right or wrong using pythom
a=3+7*7
print("a= ",a)
b=10-2/2+6
print("b= ",b)
c=2+3*4
print("c= ",c)
d=(5+3)*(2**2)
print("d= ",d)
e=20//3+8%3*2
print("e= ",e)
# 4. 
num=int(input("enter ur number"))
if(num%2==0):
	print("even")
else:
	print("odd")
#5.
day = int(input("Enter day number 1-7: "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid input")
 #6.
 print("Menu")
 print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
choice = int(input("Enter your choice [1-5]: "))

match choice:
	case 1|2|3|4:
		n1 = float(input("enter 1st no."))
		n2 = float(input("enter 2nd no."))
        match choice:
            case 1:
                 print("Sum:", n1 + n2)
            case 2:
        
                 print("Difference:", n1 - n2)
            case 3:
        
                 print("Product:", n1 * n2)
            case 4:
       
                   if n2 != 0:
                   print("Quotient:", n1 / n2)
             else:
                print("Division by zero error!")
             case 5:
               print("exiting...")
             case _:
             	printf("invalid choice")
#7
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print("Sum of first 10 natural numbers:", total)
#print the odd numbers from 1 to 13
num=10 
while num<=13:
if num%2!=0:
	print(num,end=" ")
	num+=1

#assignment part 2
#13 input a list from the user and reverse a list using list slicing.
list1 = input("enter elements seperated by spaces: ").split()
reversed_list = list1[::-1]
print("reversed list: ", reversed_list)

#14 wap to search for a number entered by the user in the list using a for else loop
list1 = list(map(int,input("enter your numbers seperated by space: ").split()))
target = int(input("enter the number to search: "))
for item in list1:
	if item == target:
		print("number found")
		print("the number is:", target)
		break
    else:
	    print("number not found")


#15 wap to read a list of integers. create two new lists, one having all posistive integers and other having all negative integers from the given list. print all the 3 list.
list1 = list(map(int, input("enter integers seperated by space: ").split()))
positive = []
negative = []
for num in list1:
	if num>=0:
		positive.append(num)
	else:
		negative.append(num)
print("original list:",list1)
print("positive list:",positive)
print("negative list:",negative)
#16 wap to find the second largest and second smallest integer from an inputed list from the user.
list1 = list(map(int, input("enter numbers seperated by space:").split()))
unique_list = list(set(list1))
if len(unique_list)< 2:
	print("not enough unique numbers to find largest/smallest numbers")
else:
	unique_list.sort()
	second_smallest = unique_list[1]
	second_largest = unique_list[-2]
	print("second smallest:", second_smallest)
	print("second largest:", second_largest)
#17
list1 = [4, 1, 9, 3, 7, 1, 5]
list1.sort()
list1.append(18)
list1.remove(1)
popped = list1.pop()
print("popped element:",popped)
if popped in list1:
	print(popped, "is still present in the list.")
else:
	print(popped,"is not present in the list.")
#18
t = (1, 2, 3, 4, 5)
print("Tuple:", t)
print("1. Search")
print("2. Add")
print("3. Remove")
ch = int(input("Enter your choice [1-3]: "))

if ch == 1:
    val = int(input("Enter element to search: "))
    if val in t:
        print("Element found in tuple")
    else:
        print("Element not found in tuple")

elif ch == 2:
    val = int(input("Enter element to add: "))
    t = t + (val,)
    print("After adding:", t)

elif ch == 3:
    val = int(input("Enter element to remove: "))
    if val in t:
        temp = list(t)
        temp.remove(val)
        t = tuple(temp)
        print("After removing:", t)
    else:
        print("Element not found in tuple")

else:
    print("Invalid choice")

# 19
n = int(input("enter number of classes: "))
classes = {}
for i in range(n):
	cls = input("enter class name: ")
	teacher = input("enter class teachers name: ")
	classes[cls] = teacher
print("class-teacher dictionary: ")
print(classes)
search = input("enter class to search: ")
if search in classes:
	print("class teacher is:",classes[search])
else:
	print("class not found")


# 20
stock = {"apple": 50, "banana": 30, "mango": 20}
stock["orange"] = 40
stock["banana"] = 45
stock.pop("mango")
if "apple" in stock:
    print("Apple is available")
print("Products:", list(stock.keys()))
print("Quantities:", list(stock.values()))
print("Total products in stock:", len(stock))

 # 21
 phonebook = {
    "Arun": "9876543210",
    "Neha": "9123456789"
}
print("Phonebook:", phonebook)
name = input("Enter name to search: ")
if name in phonebook:
    print("Number:", phonebook[name])
else:
    print("Contact not found")
#22
text = input("enter a string")
t = text.lower()
count = 0
for ch in t:
	if ch in "aeiou":
		count+= 1
	print("Total vowels: ",count)


#23
text = "I love programming in Python. Python is powerful."
with open("myfile.txt", "w") as f:
    f.write(text)

with open("myfile.txt", "r") as f:
    data = f.read()
    print("File content:", data)

  
  # 24
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
print("Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")
choice = int(input("Enter choice (1-5): "))
match choice:
    case 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", add(a, b))
    case 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", sub(a, b))
    case 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", mul(a, b))
    case 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", div(a, b))
    case 5:
        print("Exiting...")
    case _:
        print("Invalid choice")














