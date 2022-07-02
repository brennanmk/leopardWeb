from database import *  

class user:
    def __init__(self):
        self.student = studentController()
        self.instructor= instructorController()
        self.admin = adminController()
        self.course= courseController()
    
    def searchCourseByName(self, name):
        return self.course.searchCourseByName(name)

    def searchCourseByCrn(self, crn):
        return self.course.searchCourseByCrn(crn)

class student(user):    
    def login(self, uid, password):
        logRet = self.student.checkLogin(uid, password)
        if logRet == True:
            self.uid = uid

        return logRet
    
    def addClass(self, crn):
        self.course.addStudentTo(self.uid, crn)
    
    def dropClass(self, crn):
        self.course.removeStudentFrom(self.uid, crn)

    def printSchedule(self):
        return self.student.printSchedule(self.uid)

class instructor(user):
    def login(self, uid, password):
        self.instructor.checkLogin(uid, password)

    def printSchedule(self):
        return self.instructor.printSchedule(self.uid)

    def printClassList(self, crn):
        return self.course.printRoster(crn)

class admin(user):
    def login(self, uid, password):
        self.admin.checkLogin(uid, password)

    def searchClass(self, name):
        return "Function called successfully"
    
    def addCourse(self, crn):
        return "Function called successfully"
    
    def removeCourse(self, crn):
        return "Function called successfully"

    def addStudentTo(self, crn):
        return "Function called successfully"
    
    def removeStudentTo(self, crn):
        return "Function called successfully"

    def addUser(self, id, firstName, lastName):
        return "Function called successfully"
    
    def removeUser(self, id):
        return "Function called successfully"

    def printRoster(self, crn):
        return "Function called successfully"


class leopardWeb():
    def __init__(self):
        self.menu()
    
    def menu(self):
        retry = True
        while(retry):
            print("Welcome to LeopardWeb!\n")
            print("Please select an option:")
            print("1. Login as a student")
            print("2. Login as an instructor")
            print("3. Login as an administrator")
            print("4. Quit")
            res = input("Enter your choice: ")
            if res == "1":
                self.student()
            elif res == "2":
                self.instructor()
            elif res == "3":
                self.admin()
            elif res == "4":
                print("Goodbye!")
                sys.exit()
            else:
                print("Invalid input.")
    
    def student(self):
        retry = True
        while(retry):
            self.student = student()
            print("Please enter your ID:")
            idNum = input("ID: ")
            print("Please enter your password:")
            pword = input("Password: ")
            login = self.student.login(idNum, pword)
            if login:
                retry = False
            else:
                print("Invalid ID or password. Please try again.")

        retry = True
        while(retry):
            print("Welcome, " + self.student.getFirstName() + " " + self.student.getLastName() + "!")
            print("Please select an option:")
            print("1. Search for a class")
            print("2. Add a class")
            print("3. Drop a class")
            print("4. Print your schedule")
            print("5. Logout")
            res = input("Enter your choice: ")
            if res == "1":
                print("1. Search for a class by name")
                print("2. Search for a class by CRN")
                res = input("Enter your choice: ")
                if res == "1":
                    print("Please enter the name of the class:")
                    name = input("Name: ")
                    self.student.searchCourseByName(name)
                elif res == "2":
                    print("Please enter the CRN of the class:")
                    crn = input("CRN: ")
                    self.student.searchCourseByCrn(crn)
                else: 
                    print("Invalid input.")
            elif res == "2":
                print("Please enter the CRN of the class:")
                crn = input("CRN: ")
                self.student.addClass(crn)
            elif res == "3":
                print("Please enter the CRN of the class:")
                crn = input("CRN: ")
                self.student.dropClass(crn)
            elif res == "4":
                self.student.printSchedule()
            elif res == "5":
                self.menu()

    def admin(self):
        retry = True
        while(retry):
            self.admin = admin()
            print("Please enter your ID:")
            idNum = input("ID: ")
            print("Please enter your password:")
            pword = input("Password: ")
            login = self.login(idNum, pword)
            if login:
                retry = False
            else:
                print("Invalid ID or password. Please try again.")

    def instructor(self):
        retry = True
        while(retry):
            self.instructor = instructor()
            print("Please enter your ID:")
            idNum = input("ID: ")
            print("Please enter your password:")
            pword = input("Password: ")
            login = self.instructor.login(idNum, pword)
            if login:
                retry = False
            else:
                print("Invalid ID or password. Please try again.")
        retry = True
        while(retry):
            print("Welcome, " + self.instructor.getFirstName() + " " + self.instructor.getLastName() + "!")
            print("Please select an option:")
            print("1. Search for a class")
            print("2. Print your schedule")
            print("3. Print class list")
            print("4. Logout")
            res = input("Enter your choice: ")
            if res == "1":
                print("1. Search for a class by name")
                print("2. Search for a class by CRN")
                res = input("Enter your choice: ")
                if res == "1":
                    print("Please enter the name of the class:")
                    name = input("Name: ")
                    self.instructor.searchCourseByName(name)
                elif res == "2":
                    print("Please enter the CRN of the class:")
                    crn = input("CRN: ")
                    self.instructor.searchCourseByCrn(crn)
                else: 
                    print("Invalid input.")
            elif res == "2":
                self.instructor.printSchedule()
            elif res == "3":
                print("Please enter the CRN of the class:")
                crn = input("CRN: ")
                self.instructor.printClassList(crn)
            elif res == "4":
                self.menu()

if __name__ == '__main__':
    leopardWeb()
