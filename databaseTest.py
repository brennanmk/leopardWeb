from database import *
#many of the names were generated from https://www.name-generator.org.uk/quick/
if __name__ == '__main__':
    student = studentController()
    admin = adminController()
    instructor = instructorController()
    course =courseController()

    #admins
    admin.createAdmin(30991, 'pword', 'Mark', 'Thompson', 'President', 'Williston100', 'thompsonm')

    #instructors 
    instructor.createInstructor(20110, 'pword', 'Aaron', 'Carpenter', 'Assistant Professor', '2002', 'Computer Engineering', 'acarpenter')
    instructor.createInstructor(20111, 'pword', 'Hank', 'Pham', 'Assistant Professor', '2012', 'Computer Science', 'hpham')
    instructor.createInstructor(20112, 'pword', 'Marisha', 'Rawlins', 'Professor', '2000', 'Computer Engineering', 'rawlinsm')
    instructor.createInstructor(20113, 'pword', 'Ahmed', 'Hassebo', 'Professor', '2020', 'Electrical', 'hasseboa')
    instructor.createInstructor(20114, 'pword', 'Craig', 'Marks', 'Assistant Professor', '2002', 'Electrical', 'marksc')
    instructor.createInstructor(20115, 'pword', 'Yasmine', 'Price', 'Assistant Professor', '2012', 'Computer Engineering', 'pricey')
    instructor.createInstructor(20116, 'pword', 'Sofija', 'Dalton', 'Professor', '2000', 'Computer Science', 'daltons')
    instructor.createInstructor(20117, 'pword', 'Nicolas', 'Bowden', 'Professor', '2020', 'Electrical', 'bowdenn')
    instructor.createInstructor(20118, 'pword', 'Ayub', 'Collier', 'Assistant Professor', '2002', 'Physics', 'colliera')
    instructor.createInstructor(20119, 'pword', 'Maariya', 'Currie', 'Assistant Professor', '2012', 'Computer Science', 'curreym')
    instructor.createInstructor(20140, 'pword', 'Codey', 'Kemp', 'Professor', '2000', 'Computer Science', 'kempc')
    instructor.createInstructor(20142, 'pword', 'Omar', 'Mcdermott', 'Professor', '2020', 'Electrical', 'mcdermotto')
    instructor.createInstructor(20147, 'pword', 'Jason', 'Hook', 'Assistant Professor', '2002', 'Electrical', 'hookj')
    instructor.createInstructor(20148, 'pword', 'Jamal', 'Burnett', 'Assistant Professor', '2012', 'Computer Science', 'burnettj')
    instructor.createInstructor(20149, 'pword', 'Radhika', 'Crossley', 'Professor', '2000', 'Computer Science', 'crossleyr')

    #students
    student.createStudent(30180, "pword", "Bob", "Dylan", "2023", "BSCO", "dylanbob")
    student.createStudent(30181, "pword", "Jimmy", "Dean", "2030", "BSEE", "deanjim")
    student.createStudent(30182, "pword", "Harold", "Columbus", "2025", "BSCS", "columbush")
    student.createStudent(30183, "pword", "Mark", "Mii", "2023", "BSCS", "miim")
    student.createStudent(30184, "pword", "Neil", "Ferguson", "2023", "BSCO", "fergusn")
    student.createStudent(30185, "pword", "Mikayla", "Milne", "2030", "BSEE", "milnem")
    student.createStudent(30186, "pword", "Ela", "Hartman", "2025", "BSCS", "hartmane")
    student.createStudent(30187, "pword", "Elodie", "Huerta", "2023", "BSCS", "huertae")
    student.createStudent(30188, "pword", "Hawwa", "Montgomery", "2023", "BSCO", "montgomeryh")
    student.createStudent(30189, "pword", "Agnes", "Strickland", "2030", "BSEE", "stricklanda")
    student.createStudent(30190, "pword", "Ammara", "Mackie", "2025", "BSCS", "mackiea")
    student.createStudent(30191, "pword", "Milan", "Osborn", "2023", "BSCS", "osbornm")
    student.createStudent(30192, "pword", "Kameron", "Lacey", "2023", "BSCS", "laceyk")
    student.createStudent(30193, "pword", "Amanpreet", "Burton", "2023", "BSCS", "burtona")
    student.createStudent(30194, "pword", "Alyce", "Schaefer", "2023", "BSCS", "scaefera")

    #courses
    course.createCourse(401140, "Cyber-Physical Systems", "BSEE", "MWF", "1:00pm-2:50pm", "Spring", "2022", 3, 20110)
    course.createCourse(401141, "Computer Architecture", "BSCO", "TR", "4:00pm-6:00pm", "Spring", "2022", 3, 20112)
    course.createCourse(401142, "Physics 1", "BSAS", "MWF", "10:00am-11:50am", "Spring", "2022", 3, 20118)
    course.createCourse(401143, "Parallel Programming", "BCOS", "MWR", "11:00am-12:00pm", "Spring", "2022", 3, 20149)
    course.createCourse(401144, "Signals and Systems", "BSEE", "MWF", "8:00am-9:50am", "Spring", "2022", 3, 20117)
    course.createCourse(401145, "Analog Circuit Design", "BSEE", "MWF", "12:00pm-1:20pm", "Spring", "2022", 3, 20147)
    course.createCourse(401146, "Digital Circuit Design", "BSEE", "MWF", "2:00pm-3:20pm", "Spring", "2022", 3, 20142)
    course.createCourse(401147, "Physics 2", "BSAS", "MWF", "10:00am-11:50am", "Spring", "2022", 3, 20118)
    course.createCourse(401148, "Operating Systems", "BCOS", "MWR", "11:00am-12:00pm", "Spring", "2022", 3, 20115)
    course.createCourse(401149, "Digital Logic", "BSEE", "MWF", "8:00am-9:50am", "Spring", "2022", 3, 20110)
    course.createCourse(401150, "Matlab", "BSEE", "MWF", "12:00pm-1:20pm", "Spring", "2022", 3, 20116)
    course.createCourse(401151, "Robotics & Automation", "BSEE", "MWF", "2:00pm-3:20pm", "Spring", "2022", 3, 20111)