import unittest
from leopardWeb import *
from database import *
from leopardWeb import admin

#TODO: Fix search functions so they return False when no result is found

class adminTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.adm = admin()
        self.admin = adminController()
        self.instructor = instructorController()

        self.admin.createAdmin(90287, 'slyOmen12', 'Adam', 'Santano', 'President', 'Wentworth100', 'santanoa')
        
        self.instructor.createInstructor(201100, 'pword', 'Aaron', 'Carpenter', 'Assistant Professor', '2002', 'Electrical', 'acarpenter')
      
    #test login with incorrect credentials
    def testFalseLogin(self):
        self.assertFalse(self.adm.login(11111, 'pword'),
                         "Expected error while login")

    #test login with correct UID & password
    def testLogin(self):
        self.assertTrue(self.adm.login(90287, 'slyOmen12'), 
                        "Expected successful login")

    #test creating admin
    def testCreateAdmin(self):
        ret = self.adm.addAdmin(67824, 'pword', 'Tom', 'Cat', 'Registrar', 'Williston110', 'catt')
        self.assertTrue(ret)

    #test adding a course to the system
    def testAddCourse(self):
        ret = self.adm.addCourse(918026, 'Applied Programming Concepts', 'BSCS', '8:00am-9:50am', 'TR', 'Spring', '2022', 3, 201100)
        self.assertTrue(ret)

    #test removing course from system
    def testRemoveCourse(self):
        ret = self.adm.removeCourse(918026)
        self.assertTrue(ret)

    #test incorrectly removing course from system
    def testRemoveFalseCourse(self):
        ret = self.adm.removeCourse(000000)
        self.assertTrue(ret)
    
    #test deleting admin
    def testDeleteAdmin(self):
        ret = self.adm.removeAdmin(67824)
        self.assertTrue(ret)

    @classmethod
    def tearDownClass(self):
        self.admin.removeAdmin(90287)
        self.instructor.removeInstructor(201100)


class userTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.user = user()
        self.inst = instructorController()
        self.course = courseController()

        self.inst.createInstructor(201100, 'pword', 'Aaron', 'Carpenter', 'Assistant Professor', '2002', 'Electrical', 'acarpenter')
        self.course.createCourse(4011423, "Cyber-Physical Systems", "BSEE", "MWF", "1:00pm-2:50pm", "Spring", "2022", 3, 201100)

    #test search course by CRN
    def testSearchCourseByCRN(self):
        self.assertTrue(self.user.searchCourseByCrn(4011423))

    #test search course by invalid CRN
    def testSearchCourseByFalseCRN(self):
        self.assertFalse(self.user.searchCourseByCrn(0000000))

    #test search course by name
    def testSearchCourseByName(self):
        self.assertTrue(self.user.searchCourseByName('Cyber-Physical Systems'))

    #test search course by invalid name
    def testSearchCourseByFalseName(self):
        self.assertFalse(self.user.searchCourseByName('Course Name'))
        
    #test search course by days
    def testSearchCourseByDays(self):
        self.assertTrue(self.user.searchCourseByDay('MWF'))

    #test search course by invalid days
    def testSearchCourseByFalseDays(self):
        self.assertFalse(self.user.searchCourseByDay('days'))

    #test search course by time
    def testSearchCourseByTime(self):
        self.assertTrue(self.user.searchCourseByTime('1:00pm-2:50pm'))

    #test search course by invalid time
    def testSearchCourseByFalseTime(self):
        self.assertFalse(self.user.searchCourseByTime('time'))

    @classmethod
    def tearDownClass(self):
        self.inst.removeInstructor(201100)
        self.course.removeCourse(4011423)

class instructorTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.inst = instructor()
        self.instructor = instructorController()
        self.course = courseController()

        self.instructor.createInstructor(201100, 'pword', 'Aaron', 'Carpenter', 'Assistant Professor', '2002', 'Electrical', 'acarpenter')
        self.course.createCourse(4011422, "Cyber-Physical Systems", "BSEE", "MWF", "1:00pm-2:50pm", "Spring", "2022", 3, 201100)

    #test login with incorrect credentials
    def testFalseLogin(self):
        self.assertFalse(self.inst.login(11111, 'pword'),
                         "Expected error while login")

    #test login with correct UID & password
    def testLogin(self):
        self.assertTrue(self.inst.login(201100, 'pword'), 
                        "Expected successful login")

    def testPrintSchedule(self):
        self.assertTrue(self.inst.printSchedule())
    
    def testPrintClassList(self):
        self.assertTrue(self.inst.printClassList(4011422))
   
    @classmethod
    def tearDownClass(self):
        self.instructor.removeInstructor(201100)
        self.course.removeCourse(4011422)


class studentTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.stud = student()

        self.studentCont = studentController()
        self.instructor = instructorController()
        self.course = courseController()

        self.studentCont.createStudent(301823, "pword", "test", "student", "2023", "BSCO", "dylanbob")
        self.instructor.createInstructor(201100, 'pword', 'Aaron', 'Carpenter', 'Assistant Professor', '2002', 'Electrical', 'acarpenter')
        self.course.createCourse(4011422, "Cyber-Physical Systems", "BSEE", "MWF", "1:00pm-2:50pm", "Spring", "2022", 3, 201100)

    #test login with incorrect credentials
    def testFalseLogin(self):
        self.assertFalse(self.stud.login(30182356, 'pword'),
                         "Expected error while login")

    #test login with correct UID & password
    def testLogin(self):
        ret = self.stud.login(301823, 'pword')
        self.assertTrue(ret, 
                        "Expected successful login")

    #test adding student to course
    def testAddClass(self):
        self.stud.login(301823, 'pword')
        ret = self.stud.addClass(4011422)
        self.assertTrue(ret)

    #test adding student to invalid course
    def testAddClassInvalid(self):
        self.stud.login(301823, 'pword')
        ret = self.stud.addClass(401142223)
        self.assertFalse(ret)

    #test removing student from course
    def testDropClass(self):
        self.stud.login(301823, 'pword')
        ret = self.stud.dropClass(4011422)
        self.assertTrue(ret)

    #test removing student from invalid course
    def testDropClassInvalid(self):
        self.stud.login(301823, 'pword')
        ret = self.stud.dropClass(401142223)
        self.assertFalse(ret)

    #test incorrectly removing course from system
    def testPrintSchedule(self):
        ret = self.stud.printSchedule()
        self.assertTrue(ret)

    @classmethod
    def tearDownClass(self):
        self.studentCont.removeStudent(301823)
        self.instructor.removeInstructor(201100)
        self.course.removeCourse(4011422)



if __name__ == '__main__':
    unittest.main()
    