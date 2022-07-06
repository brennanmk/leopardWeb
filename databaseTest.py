from database import *

if __name__ == '__main__':
    student = studentController()
    admin = adminController()
    instructor = instructorController()
    course =courseController()

    #admins
    admin.createAdmin(30991, 'pword', 'Mark', 'Thompson', 'President', 'Williston100', 'thompsonm')
    admin.createAdmin(90123, 'pword', 'Haley', 'McGuire', 'Associate Registrar', 'Williston101', 'mcguireh')
    admin.createAdmin(67824, 'pword', 'Tom', 'Cat', 'Registrar', 'Williston110', 'catt')

    #instructors
    instructor.createInstructor(20110, 'pword', 'Aaron', 'Carpenter', 'Assistant Professor', '2002', 'Electrical', 'acarpenter')
    instructor.createInstructor(20340, 'pword', 'Hank', 'Pham', 'Assistant Professor', '2012', 'Computer Science', 'hpham')
    instructor.createInstructor(71992, 'pword', 'Marisha', 'Rawlins', 'Professor', '2000', 'Computer Science', 'rawlinsm')
    instructor.createInstructor(50842, 'pword', 'Ahmed', 'Hassebo', 'Professor', '2020', 'Electrical', 'hasseboa')

    #students
    student.createStudent(30182, "pword", "Bob", "Dylan", "2023", "BSCO", "dylanbob")
    student.createStudent(30183, "pword", "Jimmy", "Dean", "2030", "BSEE", "deanjim")
    student.createStudent(30184, "pword", "Harold", "Columbus", "2025", "BSCS", "columbush")
    student.createStudent(30185, "pword", "Mark", "Mii", "2023", "BSCS", "miim")

    

    #courses
    course.createCourse(401142, "Cyber-Physical Systems", "BSEE", "MWF", "1:00pm-2:50pm", "Spring", "2022", 3, 20110)
    course.createCourse(401156, "Computer Architecture", "BSCO", "TR", "4:00pm-6:00pm", "Spring", "2022", 3, 20110)
    course.createCourse(401173, "Physics 1", "BSAS", "MWF", "10:00am-11:50am", "Spring", "2022", 3, 20110)
    course.createCourse(401532, "Parallel Programming", "BCOS", "MWR", "11:00am-12:00pm", "Spring", "2022", 3, 20110)
    course.createCourse(401243, "Signals and Systems", "BSEE", "MWF", "8:00am-9:50am", "Spring", "2022", 3, 20110)
    course.createCourse(300100, "Analog Circuit Design", "BSEE", "MWF", "12:00pm-1:20pm", "Spring", "2022", 3, 50842)
    course.createCourse(300200, "Digital Circuit Design", "BSEE", "MWF", "2:00pm-3:20pm", "Spring", "2022", 3, 50842)
    