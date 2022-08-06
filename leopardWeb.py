from database import *

# Brennan


class user:
    def __init__(self):
        self.stud = studentController()
        self.inst = instructorController()
        self.adm = adminController()
        self.crs = courseController()

    def printCourse(self):
        try:
            ret = False
            data = self.crs.printCourse()
            courseReg = False
            for val in data:
                ret = True
                print(
                    f"{val['crn']} | {val['title']} | {val['instructor']} | {val['time']} | {val['credit']}")

                courseReg = True
            if courseReg == False:
                print("\nNo Classes Found")
            return ret

        except Exception as e:
            print("No Classes Found")
            return False

    def searchCourseByName(self, name):
        try:
            ret = False
            data = self.crs.searchCourseByName(name)
            courseReg = False

            for val in data:
                ret = True
                print(
                    f"{val['title']} | {val['instructor']} | {val['time']} | {val['credit']}")
                courseReg = True
            if courseReg == False:
                print("\nNo Classes Found")
            return ret

        except Exception as e:
            print("No Classes Found")
            return False

    def searchCourseByCrn(self, crn):
        try:
            ret = False
            data = self.crs.searchCourseByCrn(crn)
            courseReg = False

            for val in data:
                ret = True
                print(
                    f"{val['title']} | {val['instructor']} | {val['time']} | {val['credit']}")
                courseReg = True
            if courseReg == False:
                print("\nNo Classes Found")
            return ret

        except Exception as e:
            print("No Classes Found")
            return False

    # Zach
    def searchCourseByTime(self, time):
        try:
            ret = False
            data = self.crs.searchCourseByTime(time)
            courseReg = False

            for val in data:
                ret = True
                print(
                    f"{val['title']} | {val['instructor']} | {val['time']} | {val['credit']}")

                courseReg = True
            if courseReg == False:
                print("\nNo Classes Found")
            return ret
        except Exception as e:
            print("No Classes Found")
            return False

    def searchCourseByDay(self, days):
        try:
            ret = False
            data = self.crs.searchCourseByDay(days)
            courseReg = False

            for val in data:
                ret = True
                print(
                    f"{val['title']} | {val['instructor']} | {val['time']} | {val['credit']}")
                courseReg = True
            if courseReg == False:
                print("\nNo Classes Found")

            return ret
        except Exception as e:
            print("No Classes Found")
            return False
    # End Zach

# Brennan


class student(user):
    def login(self, uid, password):
        logRet = self.stud.checkLogin(uid, password)
        if logRet == True:
            self.uid = uid
        return logRet

    def addClass(self, crn):
        try:
            ret = self.crs.addStudentTo(self.uid, crn)
            if ret:
                print("Class Added")
                return True
            else:
                print("Class Not Valid")
                return False
        except Exception as e:
            print("Error")
            return False

    def dropClass(self, crn):
        try:
            self.crs.removeStudentFrom(self.uid, crn)
            print("Class Dropped")
            return True
        except Exception as e:
            print("Error")
            return False

    def printSchedule(self):
        try:
            data = self.stud.printSchedule(self.uid)
            courseReg = False
            print("\n")

            for val in data:
                print(
                    f"{val['title']} | {val['instructor']} | {val['time']} | {val['credit']}")
                courseReg = True
            print("\n")

            if courseReg == False:
                print("\nNo Classes Found\n")
            return True
        except Exception as e:
            print(e)
            return False


class instructor(user):
    def login(self, uid, password):
        logRet = self.inst.checkLogin(uid, password)
        if logRet == True:
            self.uid = uid

        return logRet

    def printSchedule(self):
        try:
            data = self.inst.printSchedule(self.uid)
            courseReg = False
            print("\n")
            for val in data:
                
                print(f"{val['title']} | {val['crn']} | {val['time']} | {val['days']}")

                courseReg = True
            print("\n")

            if courseReg == False:
                print("\nNo Classes Found\n")
            return True
        except Exception as e:
            print(e)
            return False

    def printClassList(self, crn):
        try:
            data = self.crs.printRoster(crn)
            courseReg = False

            print("\n")

            for val in data:
                print(f"{val['uid']} | {val['name']} | {val['email']}")
                courseReg = True
            print("\n")

            if courseReg == False:
                print("\nNo Classes Found\n")
            return True
        except Exception as e:
            print(e)
            return False


class admin(user):
    def login(self, uid, password):
        logRet = self.adm.checkLogin(uid, password)
        if logRet == True:
            self.uid = uid

        return logRet
 # End Brennan

    # Zach
    # add course to COURSE db
    def addCourse(self, crn, title, dept, time, days, semester, year, creditVal, instructor):
        try:
            self.crs.createCourse(crn, title, dept, time,
                                  days, semester, year, creditVal, instructor)
            print("Course added")
            return True
        except Exception as e:
            print("Error: Course already exists")
            return False

    def removeCourse(self, crn):  # remove course from COURSE db
        try:
            self.crs.removeCourse(crn)
            print("Course removed")
            return True
        except Exception as e:
            print("Error: Course not found")
            return False

    def addStudentTo(self, uid, crn):  # add student to course list for specified course
        try:
            self.crs.addStudentTo(uid, crn)
            print("Student added to course")
            return True
        except Exception as e:
            print("Error: Student already in course")
            return False

    # remove student from course list for specified course
    def removeStudentTo(self, uid, crn):
        try:
            self.crs.removeStudentFrom(uid, crn)
            print("Student removed from course")
            return True
        except Exception as e:
            print("Error: Student not in course")
            return False

    # add student to STUDENT db
    def addStudent(self, uid, pword, fname, lname, gradyear, major, email):
        try:
            self.stud.createStudent(
                uid, pword, fname, lname, gradyear, major, email)
            print("Student added")
            return True
        except Exception as e:
            print("Error")
            return False

    # add instructor to INSTRUCTOR db
    def addInstructor(self, uid, pword, fname, lname, title, hireyear, dept, email):
        try:
            self.inst.createInstructor(
                uid, pword, fname, lname, title, hireyear, dept, email)
            print("Instructor added")
            return True
        except Exception as e:
            print("Error")
            return False

    def addAdmin(self, uid, pword, fname, lname, title, office, email):  # add admin to ADMIN db
        try:
            self.adm.createAdmin(uid, pword, fname, lname,
                                 title, office, email)
            print("Admin added")
            return True
        except Exception as e:
            print("Error")
            return False

    def removeStudent(self, uid):  # remove student from STUDENT db
        try:
            self.stud.removeStudent(uid)
            print("Student removed")
            return True
        except Exception as e:
            print("Error")
            return False

    def removeInstructor(self, uid):  # remove instructor from INSTRUCTOR db
        try:
            self.inst.removeInstructor(uid)
            print("Instructor removed")
            return True
        except Exception as e:
            print("Error")
            return False

    def removeAdmin(self, uid):  # remove admin from ADMIN db
        try:
            self.adm.removeAdmin(uid)
            print("Admin removed")
            return True
        except Exception as e:
            print("Error")
            return False
    # End Zach

# Brennan
    def printRoster(self, crn):
        try:
            data = self.crs.printRoster(crn)
            courseReg = False

            for val in data:
                print(f"{val['uid']} | {val['name']} | {val['email']}")
                courseReg = True
            if courseReg == False:
                print("\nNo Classes Found\n")
            return True
        except Exception as e:
            print("Error")
            return False
    
    def updateCourse(self, crn, newCrn = None, title = None, dept = None, time = None, days = None, semester = None, year = None, creditVal = None, instructor = None):
        try:
            ret = self.crs.updateCourse(crn, newCrn, title, dept, time, days, semester, year, creditVal, instructor)
            if ret == True:
                print("Course updated")
                return True
            else:
                print("Error, course not updated")
                return False
        except Exception as e:
            print("Error")
            return False


class leopardWeb():
    def __init__(self):
        print("Welcome to LeopardWeb!\n")
        self.menu()

    def menu(self):
        retry = True
        while(retry):
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
            print("\nPlease select an option:")
            print("1. Search for a class")
            print("2. Add a class")
            print("3. Drop a class")
            print("4. Print your schedule")
            print("5. Logout")
            res = input("Enter your choice: ")
            if res == "1":
                print("1. Search for a class by name")
                print("2. Search for a class by CRN")
                print("3. Search for a class by time")
                print("4. Search for a class by day")
                print("5. Print all courses")

                res = input("Enter your choice: ")
                if res == "1":
                    print("Please enter the name of the class:")
                    name = input("Name: ")
                    self.student.searchCourseByName(name)

                elif res == "2":
                    print("Please enter the CRN of the class:")
                    crn = input("CRN: ")
                    self.student.searchCourseByCrn(crn)

                elif res == "3":
                    print("Format is: (1:00pm-2:50pm)")
                    print("Please enter the meeting time of the class:")
                    time = input("Meeting time: ")
                    self.student.searchCourseByTime(time)

                elif res == "4":
                    print("M = Monday")
                    print("T = Tuesday")
                    print("W = Wednesday")
                    print("R = Thursday")
                    print("F = Friday")
                    print("Combine days with no spaces - such as (MWF) or (TR)")
                    print("Please enter the meeting days of the class:")
                    days = input("Meeting Days: ")
                    self.student.searchCourseByDay(days)

                elif res == "5":  # print all courses
                    self.student.printCourse()

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
# Brennan end

        # Zach
        retry = True
        while (retry):
            print("\nPlease select an option:")
            print("1. Search for a course")
            print("2. Add course to system")
            print("3. Remove course from system")
            print("4. Add student to course")
            print("5. Remove student from course")
            print("6. Add user to system")
            print("7. Remove user from system")
            print("8. Print roster of course by CRN")
            print("9. Update Course Information")
            print("10. Logout")
            res = input("Enter your choice: ")
            if res == "1":  # search course
                print("1. Search for a class by name")
                print("2. Search for a class by CRN")
                print("3. Search for a class by meeting day")
                print("4. Search for a class by meeting time")
                print("5. Print all courses")
                res = input("Enter your choice: ")
                if res == "1":  # search course by name
                    print("Please enter the name of the class:")
                    name = input("Name: ")
                    self.admin.searchCourseByName(name)

                elif res == "2":  # search course by CRN
                    print("Please enter the CRN of the class:")
                    crn = input("CRN: ")
                    self.admin.searchCourseByCrn(crn)

                elif res == "3":  # search course by meeting days
                    print("M = Monday")
                    print("T = Tuesday")
                    print("W = Wednesday")
                    print("R = Thursday")
                    print("F = Friday")
                    print("Combine days with no spaces - such as (MWF) or (TR)")
                    print("Please enter the meeting days of the class:")
                    days = input("Meeting Days: ")
                    self.admin.searchCourseByDay(days)

                elif res == "4":  # search course by meeting time
                    print("Format is: (1:00pm-2:50pm)")
                    print("Please enter the meeting time of the class:")
                    time = input("Meeting time: ")
                    self.admin.searchCourseByTime(time)

                elif res == "5":  # print all courses
                    self.admin.printCourse()

                else:
                    print("Invalid input.")
            elif res == "2":  # add course
                crn = input("Enter course CRN: ")
                title = input("Enter course title: ")
                dept = input("Enter course department: ")
                times = input("Enter course meeting time: ")
                days = input("Enter course meeting day(s): ")
                semester = input("Enter course semester: ")
                year = input("Enter course year: ")
                credit = input("Enter course credit amount: ")
                instructor_entry = input("Enter instructor id: ")
                self.admin.addCourse(
                    crn, title, dept, times, days, semester, year, credit, instructor_entry)
            elif res == "3":  # remove course from system
                print("Please enter the CRN of the class:")
                crn = input("CRN: ")
                self.admin.removeCourse(crn)
            elif res == "4":  # add student to course
                print("Please enter the UID of the student")
                uid = input("UID: ")
                print("Please enter the CRN of the course")
                crn = input("CRN: ")
                self.admin.addStudentTo(uid, crn)
            elif res == "5":  # remove student from course
                print("Please enter the UID of the student")
                uid = input("UID: ")
                print("Please enter the CRN of the course")
                crn = input("CRN: ")
                self.admin.removeStudentTo(uid, crn)
            elif res == "6":  # add user to system
                print("1. Add student to system")
                print("2. Add instructor to system")
                print("3. Add administrator to system")
                res = input("Enter your choice: ")
                if res == "1":  # add student to system
                    uid = input("Enter student id: ")
                    pword = input("Enter student password: ")
                    fname = input("Enter first name: ")
                    lname = input("Enter last name: ")
                    gradyear = input("Enter graduation year: ")
                    major = input("Enter student major: ")
                    email = input("Enter student email: ")
                    self.admin.addStudent(
                        uid, pword, fname, lname, gradyear, major, email)
                elif res == "2":  # add instructor to system
                    uid = input("Enter instructor id: ")
                    pword = input("Enter instructor password: ")
                    fname = input("Enter first name: ")
                    lname = input("Enter last name: ")
                    title = input("Enter title: ")
                    hireyear = input("Enter hire year: ")
                    dept = input("Enter department: ")
                    email = input("Enter instructor email: ")
                    self.admin.addInstructor(
                        uid, pword, fname, lname, title, hireyear, dept, email)
                elif res == "3":  # add admin to system
                    uid = input("Enter admin id: ")
                    pword = input("Enter admin password: ")
                    fname = input("Enter first name: ")
                    lname = input("Enter last name: ")
                    title = input("Enter title: ")
                    office = input("Enter hire year: ")
                    email = input("Enter admin email: ")
                    self.admin.addAdmin(uid, pword, fname,
                                        lname, title, office, email)
                else:
                    print("Invalid input.")
            elif res == "7":
                print("1. Remove student")
                print("2. Remove instructor")
                print("3. Remove administrator")
                res = input("Enter your choice: ")
                if res == "1":  # remove student
                    uid = input("Enter student id: ")
                    self.admin.removeStudent(uid)
                elif res == "2":  # remove instructor
                    uid = input("Enter instructor id: ")
                    self.admin.removeInstructor(uid)
                elif res == "3":  # remove admin
                    uid = input("Enter admin id: ")
                    self.admin.removeAdmin(uid)
                else:
                    print("Invalid input.")
            elif res == "8":  # print roster of a course
                print("Please enter the CRN of the course")
                crn = input("CRN: ")
                self.admin.printRoster(crn)

            elif res == "9":  # update course information
                print("1. Update CRN")
                print("2. Update Name")
                print("3. Update Department")
                print("4. Update Meeting Time")
                print("5. Update Meeting Days")
                print("6. Update Semester")
                print("7. Update Year")
                print("8. Update Credits")
                print("9. Update Instructor")
                res = input("Enter your choice: ")
                if res == "1":  # update CRN
                    print("Please enter the old CRN of the course")
                    crn = input("CRN: ")
                    print("Please enter the new CRN")
                    new_crn = input("New CRN: ")
                    self.admin.updateCourse(crn, newCrn = new_crn)
                elif res == "2":  # update name
                    print("Please enter the CRN of the course")
                    crn = input("CRN: ")
                    print("Please enter the new name")
                    new_name = input("New name: ")
                    self.admin.updateCourse(crn, title = new_name)
                elif res == "3":  # update department
                    print("Please enter the CRN of the course")
                    crn = input("CRN: ")
                    print("Please enter the new department")
                    new_dept = input("New department: ")
                    self.admin.updateCourse(crn, dept = new_dept)
                elif res == "4":  # update meeting time
                    print("Please enter the CRN of the course")
                    crn = input("CRN: ")
                    print("Please enter the new meeting time")
                    new_time = input("New meeting time: ")
                    self.admin.updateCourse(crn, time = new_time)
                elif res == "5":  # update meeting days
                    print("Please enter the CRN of the course")
                    crn = input("CRN: ")
                    print("Please enter the new meeting days")
                    new_days = input("New meeting days: ")
                    self.admin.updateCourse(crn, days = new_days)
                elif res == "6":  # update semester
                    print("Please enter the CRN of the course")
                    crn = input("CRN: ")
                    print("Please enter the new semester")
                    new_semester = input("New semester: ")
                    self.admin.updateCourse(crn, semester = new_semester)
                elif res == "7":  # update year
                    print("Please enter the CRN of the course")
                    crn = input("CRN: ")
                    print("Please enter the new year")
                    new_year = input("New year: ")
                    self.admin.updateCourse(crn, year = new_year)
                elif res == "8":  # update credits
                    print("Please enter the CRN of the course")
                    crn = input("CRN: ")
                    print("Please enter the new credits")
                    new_credits = input("New credits: ")
                    self.admin.updateCourse(crn, creditVal = new_credits)
                elif res == "9":  # update instructor
                    print("Please enter the CRN of the course")
                    crn = input("CRN: ")
                    print("Please enter the new instructor")
                    new_instructor = input("New instructor: ")
                    self.admin.updateCourse(crn, instructor = new_instructor)
                else:
                    print("Invalid input.")
            elif res == "10":  # logout
                self.menu()
            else:
                print("Invalid Input.")
    # Zach end

# Brennan
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
            print("\nPlease select an option:")
            print("1. Search for a class")
            print("2. Print your schedule")
            print("3. Print class list")
            print("4. Logout")
            res = input("Enter your choice: ")
            if res == "1":
                print("1. Search for a class by name")
                print("2. Search for a class by CRN")
                print("3. Search for a class by meeting day")
                print("4. Search for a class by time")
                print("5. Display All")

                res = input("Enter your choice: ")
                if res == "1":
                    print("Please enter the name of the class:")
                    name = input("Name: ")
                    self.instructor.searchCourseByName(name)

                elif res == "2":
                    print("Please enter the CRN of the class:")
                    crn = input("CRN: ")
                    self.instructor.searchCourseByCrn(crn)

                elif res == "3":
                    print("M = Monday")
                    print("T = Tuesday")
                    print("W = Wednesday")
                    print("R = Thursday")
                    print("F = Friday")
                    print("Combine days with no spaces - such as (MWF) or (TR)")
                    print("Please enter the meeting days of the class:")
                    days = input("Meeting Days: ")
                    self.admin.searchCourseByDay(days)

                elif res == "4":
                    print("Format is: (1:00pm-2:50pm)")
                    print("Please enter the meeting time of the class:")
                    time = input("Meeting time: ")
                    self.instructor.searchCourseByTime(time)
                
                elif res == "5":
                    self.instructor.printCourse()

                else:
                    print("Invalid input.")
            elif res == "2":
                self.instructor.printSchedule()
            elif res == "3":
                print("Please enter the CRN of the class:")
                crn = input("CRN: ")
                # Zach - added fix to print info properly
                # now displays as (student_name | student_id)
                self.instructor.printClassList(crn)

            elif res == "4":
                self.menu()


if __name__ == '__main__':
    leopardWeb()
