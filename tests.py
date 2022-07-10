import unittest
from leopardWeb import *

#Assignment 6 - Testing
class TestAdmin(unittest.TestCase):
    #for each test, create a test admin
    def setUp(self):
        adminController.createAdmin(self, 90287, 'slyOmen12', 'Adam', 'Santano', 'President', 'Wentworth100', 'santanoa')
    
    #after each test, remove admin
    def tearDown(self):
        adminController.removeAdmin(self, 90287)

    #test login with correct UID & password
    def testLogin(self):
        a = admin()
        self.assertTrue(a.login(90287, 'slyOmen12'), 
                        "Expected successful login")

    #test login with incorrect credentials
    def testFalseLogin(self):
        a = admin()
        self.assertFalse(a.login(11111, 'pword'),
                         "Expected error while login")

    #test adding a course to the system
    def testAddCourse(self):
        a = admin()
        a.addCourse(918026, 'Applied Programming Concepts', 'BSCS', '8:00am-9:50am', 'TR', 'Spring', '2022', 3, 71992)
        self.assertTrue(a.course_been_added,
                        "Expected successful course addition")

    #test adding course with non-unique crn
    def testAddFalseCourse(self):
        a = admin()
        a.addCourse(401142, "Cyber-Physical Systems", "BSEE", "MWF", "1:00pm-2:50pm", "Spring", "2022", 3, 20110)
        a.addCourse(401142, "Cyber-Physical Systems", "BSEE", "MWF", "1:00pm-2:50pm", "Spring", "2022", 3, 20110)
        self.assertFalse(a.course_been_added,
                         "Expected an error while adding course")

    #test removing course from system
    def testRemoveCourse(self):
        a = admin()
        a.addCourse(401156, "Computer Architecture", "BSCO", "TR", "4:00pm-6:00pm", "Spring", "2022", 3, 20110)
        a.removeCourse(401156)
        self.assertTrue(a.course_been_removed, 
                        "Expected successful course removal")

    #test incorrectly removing course from system
    def testRemoveFalseCourse(self):
        a = admin()
        a.removeCourse(000000)
        self.assertTrue(a.course_been_removed, 
                        "Expected an error while removing course")

    #test search course by CRN
    def testSearchCourseByCRN(self):
        a = admin()
        a.addCourse(401243, "Signals and Systems", "BSEE", "MWF", "8:00am-9:50am", "Spring", "2022", 3, 20110)
        a.addCourse(300100, "Analog Circuit Design", "BSEE", "MWF", "12:00pm-1:20pm", "Spring", "2022", 3, 50842)
        a.addCourse(300200, "Digital Circuit Design", "BSEE", "MWF", "2:00pm-3:20pm", "Spring", "2022", 3, 50842)
        self.assertEqual(a.searchCourseByCrn(401243), {['Signals and Systems'], ['Aaron Carpenter'], ['8:00am-9:50am'], [3]},
                        "Expected successful course search")

    #test search course by name
    #def testSearchCourseByName(self):
    #    a = admin()
    #    a.addCourse(401243, "Signals and Systems", "BSEE", "MWF", "8:00am-9:50am", "Spring", "2022", 3, 20110)
    #    a.addCourse(300100, "Analog Circuit Design", "BSEE", "MWF", "12:00pm-1:20pm", "Spring", "2022", 3, 50842)
    #    a.addCourse(300200, "Digital Circuit Design", "BSEE", "MWF", "2:00pm-3:20pm", "Spring", "2022", 3, 50842)
    #    name = 'Signals and Systems'
    #    self.assertEqual(a.searchCourseByName(name), {['Signals and Systems'], ['Aaron Carpenter'], ['8:00am-9:50am'], [3]},
    #                    "Expected successful course search")

    #test search course by days
    #def testSearchCourseByDays(self):
    #    a = admin()
    #    a.addCourse(401243, "Signals and Systems", "BSEE", "MWF", "8:00am-9:50am", "Spring", "2022", 3, 20110)
    #    a.addCourse(300100, "Analog Circuit Design", "BSEE", "MWF", "12:00pm-1:20pm", "Spring", "2022", 3, 50842)
    #    a.addCourse(300200, "Digital Circuit Design", "BSEE", "MWF", "2:00pm-3:20pm", "Spring", "2022", 3, 50842)
    #    days = 'MWF'
    #    self.assertEqual(a.searchCourseByDays(days), {['Signals and Systems'], ['Aaron Carpenter'], ['8:00am-9:50am'], [3]},
    #                    "Expected successful course search")

    #test search course by meeting time
    

        





if __name__ == '__main__':
    unittest.main()
