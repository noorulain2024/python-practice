class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
        #print("adding new student in database")
def welcome(self):
    print("welcome student", self.name)


def get_marks(self):
 print("maekrs", self.marks)
 
 s1 = Student("noor", 23)
 s1.welcome()
 print(s1.get_marks())


#s2 = Student("ulain", 67)
#print(s2.name, s2.marks)

#create student class that takes student name and markes of three subjects as arguments in constructor
#then create a method to print the avg
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg markes is", sum/3)
s1 = Student("noor", [23, 67, 90])
s1.avg_marks()

# account
class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc_no = acc
        
    def debit(self, amm):
        self.bal -= amm
        print("amount", amm, "is debited")    
        
    def credit(self, amm):    
        self.bal += amm
        print("amount", amm, "is credited")
        
    def total_amm(self):
        return self.bal
acc1 = Account(1000, 1234)
acc1.debit(100)
acc1.credit(1555)
        