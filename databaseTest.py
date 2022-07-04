from database import *

if __name__ == '__main__':
    student = studentController()
    admin = adminController()
    instructor = instructorController()
    course =courseController()


    admin.createAdmin(30991, 'admin', 'admin', 'admin', 'admin', 'admin', 'admin')

    instructor.createInstructor(20110, 'pword', 'Aaron', 'Carpenter', 'Assistant Professor', '2002', 'Electrical', 'acarpenter')
    instructor.createInstructor(20340, 'pword', 'Hank', 'Pham', 'Assistant Professor', '2012', 'Computer Science', 'hpham')

    student.createStudent(30186, "pword", "Bob", "Dylan", "2023", "BSCO", "dylanbob")
    student.createStudent(30182, "pword", "Jimmy", "Dean", "2030", "BSEE", "deanjim")

    course.createCourse(401142, "Cyber-Physical Systems", "BSEE", "MWF", "1:00pm-2:50pm", "Spring", "2022", 3, 20110)
    course.createCourse(401156, "Computer Architecture", "BSCO", "TH", "4:00pm-6:00pm", "Spring", "2022", 3, 20110)
    course.createCourse(401173, "Physics 1", "BSAS", "MWF", "10:00am-11:50am", "Spring", "2022", 3, 20110)
    course.createCourse(401532, "Parallel Programming", "BCOS", "MWR", "11:00am-12:00pm", "Spring", "2022", 3, 20110)
    course.createCourse(401243, "Signals and Systems", "BSEE", "MWF", "8:00am-9:50am", "Spring", "2022", 3, 20110)
    