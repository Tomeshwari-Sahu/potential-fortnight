#Hospital Management System using OOPS

#  Person Class 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Doctor Class 
class Doctor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def show(self):
        print("Doctor Name:", self.name,
              " Age:", self.age,
              "Department:", self.department)


# Patient Class
class Patient(Person):
    def __init__(self, name, age, problem):
        super().__init__(name, age)
        self.problem = problem
        self.bill = 0

    def add_bill(self, amount):
        self.bill += amount

    def show(self):
        print("Patient Name:", self.name,
              "| Age:", self.age,
              "| Problem:", self.problem,
              "| Bill: Rs", self.bill)


#  Hospital Class
class Hospital:
    def __init__(self):
        self.doctors = []
        self.patients = []

    def add_doctor(self):
        name = input("Enter doctor name: ")
        age = int(input("Enter age: "))
        dept = input("Enter department: ")
        self.doctors.append(Doctor(name, age, dept))
        print("Doctor added successfully!")

    def add_patient(self):
        name = input("Enter patient name: ")
        age = int(input("Enter age: "))
        prob = input("Enter problem: ")
        self.patients.append(Patient(name, age, prob))
        print("Patient registered successfully!")

    def show_doctors(self):
        if not self.doctors:
            print("No doctors available.")
        for d in self.doctors:
            d.show()

    def show_patients(self):
        if not self.patients:
            print("No patients available.")
        for p in self.patients:
            p.show()

    def generate_bill(self):
        name = input("Enter patient name: ")
        for p in self.patients:
            if p.name == name:
                amount = int(input("Enter bill amount: "))
                p.add_bill(amount)
                print("Bill generated successfully!")
                return
        print("Patient not found!")

hospital = Hospital()

while True:
    print("\n Hospital Management System ")
    print("1. Add Doctor")
    print("2. Add Patient")
    print("3. Show Doctors")
    print("4. Show Patients")
    print("5. Generate Bill")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        hospital.add_doctor()
    elif choice == "2":
        hospital.add_patient()
    elif choice == "3":
        hospital.show_doctors()
    elif choice == "4":
        hospital.show_patients()
    elif choice == "5":
        hospital.generate_bill()
    elif choice == "6":
        print("Thank you! Exiting program.")
        break
    else:
        print("Invalid choice! Try again.")