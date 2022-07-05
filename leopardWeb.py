from asyncio.windows_events import NULL
from database import *  

class user:
    def __init__(self):
        self.stud = studentController()
        self.inst= instructorController()
        self.adm = adminController()
        self.crs = courseController()
    
    def searchCourseByName(self, name):
        return self.crs.searchCourseByName(name)

    def searchCourseByCrn(self, crn):
        return self.crs.searchCourseByCrn(crn)

    def searchCourseByTime(self, time):
        return self.crs.searchCourseByTime(time)

    def searchCourseByDay(self, days):
        return self.crs.searchCourseByDay(days)

class student(user):    
    def login(self, uid, password):
        logRet = self.stud.checkLogin(uid, password)
        if logRet == True:
            self.uid = uid
        return logRet
    
    def addClass(self, crn):
        self.crs.addStudentTo(self.uid, crn)
    
    def dropClass(self, crn):
        self.crs.removeStudentFrom(self.uid, crn)

    def printSchedule(self):
        return self.stud.printSchedule(self.uid)

class instructor(user):
    def login(self, uid, password):
        logRet = self.inst.checkLogin(uid, password)
        if logRet == True:
            self.uid = uid

        return logRet

    def printSchedule(self):
        return self.inst.printSchedule(self.uid)

    def printClassList(self, crn):
        return self.crs.printRoster(crn)

class admin(user):
    def login(self, uid, password):
        logRet = self.adm.checkLogin(uid, password)
        if logRet == True:
            self.uid = uid

        return logRet
        
    def searchClass(self, name):                #search for a class, print info
        return self.crs.searchCourseByName()
    
    def addCourse(self, crn, title, dept, time, days, semester, year, credits, instructor):     #add course to COURSE db
        return self.crs.createCourse(crn, title, dept, time, days, semester, year, credits, instructor)
    
    def removeCourse(self, crn):                #remove course from COURSE db
        return self.crs.removeCourse(crn)

    def addStudentTo(self, uid, crn):           #add student to course list for specified course
        return self.crs.addStudentTo(uid, crn)
    
    def removeStudentTo(self, uid, crn):        #remove student from course list for specified course
        return self.crs.removeStudentFrom(uid, crn)

    def addStudent(self, uid, pword, fname, lname, gradyear, major, email):   #add student to STUDENT db
        return self.stud.createStudent(uid, pword, fname, lname, gradyear, major, email)

    def addInstructor(self, uid, pword, fname, lname, title, hireyear, dept, email):    #add instructor to INSTRUCTOR db
        return self.inst.createInstructor(uid, pword, fname, lname, title, hireyear, dept, email)
    
    def addAdmin(self, uid, pword, fname, lname, title, office, email):                  #add admin to ADMIN db
        return self.adm.createAdmin(uid, pword, fname, lname, title, office, email)

    def removeStudent(self, uid):               #remove student from STUDENT db
        return self.stud.removeStudent(uid)

    def removeInstructor(self, uid):            #remove instructor from INSTRUCTOR db
        return self.inst.removeInstructor(uid)

    def removeAdmin(self, uid):                 #remove admin from ADMIN db
        return self.adm.removeAdmin(uid)

    def printRoster(self, crn):
        return self.crs.printRoster()


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
            login = self.admin.login(idNum, pword)
            if login:
                retry = False
            else:
                print("Invalid ID or password. Please try again.")

        retry = True
        while (retry):
            print("Please select an option:")
            print("1. Search for a course")
            print("2. Add course to system")
            print("3. Remove course from system")
            print("4. Add student to course")
            print("5. Remove student from course")
            print("6. Add user to system")
            print("7. Remove user from system")
            print("8. Print roster of course by CRN")
            print("9. Logout")
            res = input ("Enter your choice: ")
            if res == "1":              #search course
                print("1. Search for a class by name")
                print("2. Search for a class by CRN")
                print("3. Search for a class by meeting day")
                print("4. Search for a class by meeting time")
                res = input("Enter your choice: ")
                if res == "1":#search course by name
                    print("Please enter the name of the class:")
                    name = input("Name: ")
                    self.admin.searchCourseByName(name)
                elif res == "2":#search course by CRN
                    print("Please enter the CRN of the class:")
                    crn = input("CRN: ")
                    self.admin.searchCourseByCrn(crn)
                elif res == "3":#search course by meeting days
                    print("M = Monday")
                    print("T = Tuesday")
                    print("W = Wednesday")
                    print("R = Thursday")
                    print("F = Friday")
                    print("Combine days with no spaces - such as (MWF) or (TR)")
                    print("Please enter the meeting days of the class:")
                    days = input("Meeting Days: ")
                    self.admin.searchCourseByDay(self, days)
                elif res == "4":#search course by meeting time
                    print("Format is: (1:00pm-2:50pm)")
                    print("Please enter the meeting time of the class:")
                    times = input("Meeting times: ")
                    self.admin.searchCourseByMeetTime(self, times)
                else: 
                        print("Invalid input.")
            elif res == "2":            #add course
                crn = input("Enter course CRN: ")
                title = input("Enter course title: ")
                dept = input("Enter course department: ")
                times = input("Enter course meeting time: ")
                days = input("Enter course meeting day(s): ")
                semester = input("Enter course semester: ")
                year = input("Enter course year: ")
                credit = input("Enter course credit amount: ")
                instructor_entry = input("Enter instructor id: ")  
                self.admin.addCourse(crn, title, dept, times, days, semester, year, credit, instructor_entry)
            elif res == "3":            #remove course from system
                print("Please enter the CRN of the class:")
                crn = input("CRN: ")
                self.admin.removeCourse(crn)
            elif res == "4":            #add student to course
                print("Please enter the UID of the student")
                uid = input("UID: ")
                print("Please enter the CRN of the course")
                crn = input("CRN: ")
                return self.admin.addStudentTo(uid, crn)
            elif res == "5":            #remove student from course
                print("Please enter the UID of the student")
                uid = input("UID: ")
                print("Please enter the CRN of the course")
                crn = input("CRN: ")
                return self.admin.removeStudentTo(uid, crn)
            elif res == "6":            #add user to system
                print("1. Add student to system")
                print("2. Add instructor to system")
                print("3. Add administrator to system")
                res = input("Enter your choice: ")
                if res == "1":#add student to system
                    uid = input("Enter student id: ")
                    pword = input("Enter student password: ")
                    fname = input("Enter first name: ")
                    lname = input("Enter last name: ")
                    gradyear = input("Enter graduation year: ")
                    major = input("Enter student major: ")
                    email = input("Enter student email: ")     
                    return self.admin.addStudent(uid, pword, fname, lname, gradyear, major, email)    
                elif res == "2":#add instructor to system
                    uid = input("Enter instructor id: ")
                    pword = input("Enter instructor password: ")
                    fname = input("Enter first name: ")
                    lname = input("Enter last name: ")
                    title = input("Enter title: ")
                    hireyear = input("Enter hire year: ")
                    dept = input("Enter department: ")
                    email = input("Enter instructor email: ") 
                    return self.admin.addInstructor(uid, pword, fname, lname, title, hireyear, dept, email)
                elif res == "3":#add admin to system
                    uid = input("Enter admin id: ")
                    pword = input("Enter admin password: ")
                    fname = input("Enter first name: ")
                    lname = input("Enter last name: ")
                    title = input("Enter title: ")
                    office = input("Enter hire year: ")
                    email = input("Enter admin email: ") 
                    return self.admin.addAdmin(uid, pword, fname, lname, title, office, email)
                else:
                    print("Invalid input.")
            elif res == "7":
                print("1. Remove student")
                print("2. Remove instructor")
                print("3. Remove administrator")
                res = input("Enter your choice: ")
                if res == "1":#remove student
                    uid = input("Enter student id: ")
                    return self.admin.removeStudent(uid)
                elif res == "2":#remove instructor
                    uid = input("Enter instructor id: ")
                    return self.admin.removeInstructor(uid)
                elif res == "3":#remove admin
                    uid = input("Enter admin id: ")
                    self.admin.removeAdmin(uid)
                else:
                    print("Invalid input.")
            elif res == "8":            #print roster of a course
                print("Please enter the CRN of the course")
                crn = input("CRN: ")
                return self.admin.printRoster(crn)
            elif res == "9":            #logout
                self.menu()
            else:
                print("Invalid Input.")
                    



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
