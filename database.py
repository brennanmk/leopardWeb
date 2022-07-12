from peewee import *
import argparse
import sys

# Brennan created whole database.py
db = SqliteDatabase('leopardWeb.db')


class BaseModel(Model):
    class Meta:
        database = db


class STUDENT(BaseModel):
    UID = CharField(unique=True)
    PASSWORD = CharField()
    NAME = CharField()
    SURNAME = CharField()
    GRADYEAR = CharField()
    MAJOR = CharField()
    EMAIL = CharField()


class INSTRUCTOR(BaseModel):
    UID = CharField(unique=True)
    PASSWORD = CharField()
    NAME = CharField()
    SURNAME = CharField()
    TITLE = CharField()
    HIREYEAR = CharField()
    DEPT = CharField()
    EMAIL = CharField()


class ADMIN(BaseModel):
    UID = CharField(unique=True)
    PASSWORD = CharField()
    NAME = CharField()
    SURNAME = CharField()
    TITLE = CharField()
    OFFICE = CharField()
    EMAIL = CharField()


class COURSE(BaseModel):
    crn = CharField(unique=True)
    title = CharField()
    department = CharField()
    time = CharField()
    days = CharField()
    semester = CharField()
    year = CharField()
    credit = IntegerField()
    instructor = ForeignKeyField(INSTRUCTOR, backref='courses')


class COURSE_LIST(BaseModel):
    students = ForeignKeyField(STUDENT, backref='courses')
    course = ForeignKeyField(COURSE, backref='courses')


class courseController():
    def createCourse(self, crnEntry, titleEntry, departmentEntry, dayEntry, timeEntry, semesterEntry, yearEntry, creditEntry, instructorEntry):
        instr = INSTRUCTOR.get(INSTRUCTOR.UID == instructorEntry)
        COURSE.create(crn=crnEntry, title=titleEntry, department=departmentEntry, time=timeEntry,
                      days=dayEntry, semester=semesterEntry, year=yearEntry, credit=creditEntry, instructor=instr)

    def removeCourse(self, crnVal):
        '''remove COURSE based on CRN'''
        COURSE.delete().where(COURSE.crn == crnVal).execute()

    def printCourse(self):
        crs = COURSE.select()
        crsInfo = []
        for entry in crs:
            csrEntry = {}
            csrEntry['crn'] = entry.crn
            csrEntry['title'] = entry.title
            csrEntry['instructor'] = entry.instructor.NAME + " " + entry.instructor.SURNAME
            csrEntry['time'] = entry.time
            csrEntry['credit'] = entry.credit
            crsInfo.append(csrEntry)
        return crsInfo


    def searchCourseByCrn(self, crnVal):
        '''search COURSE by crn, return as dict'''
        crs = COURSE.select().where(COURSE.crn == crnVal)
        crsInfo = []
        for entry in crs:
            csrEntry = {}
            csrEntry['title'] = entry.title
            csrEntry['instructor'] = entry.instructor.NAME + " " + entry.instructor.SURNAME
            csrEntry['time'] = entry.time
            csrEntry['credit'] = entry.credit
            crsInfo.append(csrEntry)
        return crsInfo

    def searchCourseByName(self, nameVal):
        # search COURSE by name, return as list
        crs = COURSE.select().where(COURSE.title == nameVal)
        crsInfo = []
        for entry in crs:
            csrEntry = {}
            csrEntry['title'] = entry.title
            csrEntry['instructor'] = entry.instructor.NAME + " " + entry.instructor.SURNAME
            csrEntry['time'] = entry.time
            csrEntry['credit'] = entry.credit
            crsInfo.append(csrEntry)
        return crsInfo

    # Zach - added functions to search crs by some additional parameters
    def searchCourseByTime(self, timeVal):
        # search COURSE by time, return as nested list
        crs = COURSE.select().where(COURSE.time == timeVal)
        crsInfo = []
        for entry in crs:
            csrEntry = {}
            csrEntry['title'] = entry.title
            csrEntry['instructor'] = entry.instructor.NAME + " " + entry.instructor.SURNAME
            csrEntry['time'] = entry.time
            csrEntry['credit'] = entry.credit
            crsInfo.append(csrEntry)
        return crsInfo

    def searchCourseByDay(self, dayVal):
        # search COURSE by days, return as list
        crs = COURSE.select().where(COURSE.days == dayVal)
        crsInfo = []
        for entry in crs:
            csrEntry = {}
            csrEntry['title'] = entry.title
            csrEntry['instructor'] = entry.instructor.NAME + " " + entry.instructor.SURNAME
            csrEntry['time'] = entry.time
            csrEntry['credit'] = entry.credit
            crsInfo.append(csrEntry)
        return crsInfo

    def addStudentTo(self, uid, crn):  # add student to course - update COURSE_LIST
        stud = STUDENT.get(STUDENT.UID == uid)
        crsEntry = COURSE.get(COURSE.crn == crn)
        COURSE_LIST.create(students=stud, course=crsEntry)

    # remove student from course - update COURSE_LIST
    def removeStudentFrom(self, uid, crn):
        stud = STUDENT.get(STUDENT.UID == uid)
        crs = COURSE.get(COURSE.crn == crn)
        COURSE_LIST.delete().where(COURSE_LIST.students == stud).where(
            COURSE_LIST.course == crs).execute()

    def printRoster(self, crn):
        crs = COURSE.select().where(COURSE.crn == crn)
        roster = COURSE_LIST.select().where(COURSE_LIST.course == crs)
        crsList = []
        for entry in roster:
            data = {}
            data['uid'] = entry.students.UID
            data['name'] = entry.students.NAME + " " + entry.students.SURNAME
            data['email'] = entry.students.EMAIL
            crsList.append(data)
        return crsList

    def updateCourse(self, crnEntry=None, titleEntry=None, departmentEntry=None, timeEntry=None, dayEntry=None, semesterEntry=None, yearEntry=None, creditEntry=None, instructorEntry=None):
        '''update STUDENT, set any vals that should not be changed to null'''
        crs = COURSE.select().where(COURSE.crn == crnEntry).dicts()
        if crnEntry != None:
            crs.crn = crnEntry
        if titleEntry != None:
            crs.title = titleEntry
        if departmentEntry != None:
            crs.department = departmentEntry
        if timeEntry != None:
            crs.time = timeEntry
        if dayEntry != None:
            crs.days = dayEntry
        if semesterEntry != None:
            crs.semester = semesterEntry
        if yearEntry != None:
            crs.year = yearEntry
        if creditEntry != None:
            crs.credit = creditEntry
        if instructorEntry != None:
            instr = INSTRUCTOR.get(INSTRUCTOR.UID == instructorEntry)
            crs.instructor = instr

        crs.save()

    def matchInstructor(self):
        '''List all available instructors for each course'''
        retList = []
        for entry in COURSE:
            instList = []
            instQuery = INSTRUCTOR.select().where(INSTRUCTOR.DEPT == entry.department).get()
            try:
                for inst in instQuery:
                    instList.append(inst.NAME)
            except Exception as e:
                instList.append(instQuery.NAME)

            retList.append({entry.title: instList})

        return retList


class studentController():
    def createStudent(self, idVal, pword, fName, lName, expecGrad, majorVal, emailVal):
        STUDENT.create(UID=idVal, PASSWORD=pword, NAME=fName, SURNAME=lName,
                       GRADYEAR=expecGrad, MAJOR=majorVal, EMAIL=emailVal)

    def removeStudent(self, idNum):
        '''remove STUDENT based on uid'''
        STUDENT.delete().where(STUDENT.UID == idNum).execute()

    def searchStudentByUID(self, idVal):
        '''search STUDENT by id, return as dict'''
        stud = STUDENT.select().where(STUDENT.UID == idVal)
        return stud.get()

    def printSchedule(self, uid):
        stud = STUDENT.get(STUDENT.UID == uid)
        retList = []
        for entry in COURSE_LIST:
            if entry.students == stud:
                data = {}
                data['title'] = entry.course.title
                try: #check to see if instructor is assigned to course
                    data['instructor'] = entry.instructor.NAME + " " + entry.course.instructor.SURNAME
                except Exception as e:
                    data['instructor'] = "N/A"
                data['time'] = entry.course.time
                data['credit'] = entry.course.credit
                retList.append(data)
        return retList

    def checkLogin(self, uid, pword):
        try:
            user = STUDENT.select().where(STUDENT.UID == uid).get()
            if user.PASSWORD == pword:
                return True
            else:
                return False
        except Exception as e:
            return False

    def updateStudent(self, idVal, newID=None, pword=None, fName=None, lName=None, expecGrad=None, majorVal=None, emailVal=None):
        '''update STUDENT, set any vals that should not be changed to null'''
        stud = STUDENT.select().where(STUDENT.UID == idVal).get()

        if newID != None:
            stud.UID = newID
        if pword != None:
            stud.PASSWORD = pword
        if fName != None:
            stud.NAME = fName
        if lName != None:
            stud.SURNAME = lName
        if expecGrad != None:
            stud.GRADYEAR = expecGrad
        if majorVal != None:
            stud.MAJOR = majorVal
        if emailVal != None:
            stud.EMAIL = emailVal

        stud.save()


class instructorController():
    def createInstructor(self, idVal, pword, fName, lName, titleVal, yearHired, departmentVal, emailVal):
        INSTRUCTOR.create(UID=idVal, PASSWORD=pword, NAME=fName, SURNAME=lName,
                          TITLE=titleVal, HIREYEAR=yearHired, DEPT=departmentVal, EMAIL=emailVal)

    def removeInstructor(self, idNum):
        '''remove INSTRUCTOR based on uid'''
        INSTRUCTOR.delete().where(INSTRUCTOR.UID == idNum).execute()

    def searchInstructorByUID(self, idVal):
        '''search INSTRUCTOR by id, return as dict'''
        inst = INSTRUCTOR.select().where(INSTRUCTOR.UID == idVal)
        return inst.get()

    def printSchedule(self, uid):
        inst = INSTRUCTOR.get(INSTRUCTOR.UID == uid)
        retList = []
        for entry in COURSE_LIST:
            if entry.instructor == inst:
                data = {}
                data['title'] = entry.title
                data['crn'] = entry.crn
                data['time'] = entry.time
                data['days'] = entry.days
                retList.append(data)
        return retList

    def checkLogin(self, uid, pword):
        try:
            user = INSTRUCTOR.select().where(INSTRUCTOR.UID == uid).get()
            if user.PASSWORD == pword:
                return True
            else:
                return False
        except Exception as e:
            return False

    def updateInstructor(self, idVal, newID=None, pword=None, fName=None, lName=None, titleVal=None, yearHired=None, departmentVal=None, emailVal=None):
        '''search STUDENT by id, return as dict'''
        instr = INSTRUCTOR.select().where(INSTRUCTOR == idVal).get()

        if newID != None:
            instr.UID = newID
        if pword != None:
            instr.PASSWORD = pword
        if fName != None:
            instr.NAME = fName
        if lName != None:
            instr.SURNAME = lName
        if titleVal != None:
            instr.TITLE = titleVal
        if yearHired != None:
            instr.HIREYEAR = yearHired
        if departmentVal != None:
            instr.DEPT = departmentVal
        if emailVal != None:
            instr.EMAIL = emailVal

        instr.save()


class adminController():
    def createAdmin(self, idVal, pword, fName, lName, titleVal, officeVal, emailVal):
        ADMIN.create(UID=idVal, PASSWORD=pword, NAME=fName, SURNAME=lName,
                     TITLE=titleVal, OFFICE=officeVal, EMAIL=emailVal)

    def removeAdmin(self, idNum):
        '''remove ADMIN based on uid'''
        ADMIN.delete().where(ADMIN.UID == idNum).execute()

    def searchAdminByUID(self, idVal):
        '''search ADMIN by id, return as dict'''
        adm = ADMIN.select().where(ADMIN.UID == idVal)
        return adm.get()

    def checkLogin(self, uid, pword):
        try:
            user = ADMIN.select().where(ADMIN.UID == uid).get()
            if user.PASSWORD == pword:
                return True
            else:
                return False
        except Exception as e:
            return False

    def updateAdmin(self, idVal, newID=None, pword=None, fName=None, lName=None, titleVal=None, OfficeVal=None, emailVal=None):
        '''search STUDENT by id, return as dict'''
        adm = ADMIN.select().where(ADMIN.UID == idVal).get()

        if newID != None:
            adm.UID = newID
        if pword != None:
            adm.PASSWORD = pword
        if fName != None:
            adm.NAME = fName
        if lName != None:
            adm.SURNAME = lName
        if titleVal != None:
            adm.TITLE = titleVal
        if OfficeVal != None:
            adm.OFFICE = OfficeVal
        if emailVal != None:
            adm.EMAIL = emailVal

        adm.save()


if __name__ == '__main__':
    # Run this file on its own to create COURSE table
    parser = argparse.ArgumentParser("Create databases or delete databases.")
    parser.add_argument('mode', type=str,
                        help='flag, if c then create database tables if d delete')

    args = parser.parse_args(sys.argv[1:])
    db.connect()

    if args.mode == 'c':
        db.create_tables([INSTRUCTOR, STUDENT, COURSE, COURSE_LIST, ADMIN])
    elif args.mode == 'd':
        db.drop_tables([INSTRUCTOR, STUDENT, COURSE, COURSE_LIST, ADMIN])
    else:
        print("No Args specified. Try again.")
