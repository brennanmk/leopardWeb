from database import *

if __name__ == '__main__':
    student = studentController()
    admin = adminController()
    instructor = instructorController()
    course =courseController()

    #admins           ( id,   pword,  fname,    lname,      title,       office,         email )
    admin.createAdmin(30991, 'pword', 'Mark', 'Thompson', 'President', 'Williston100', 'thompsonm')
    #admin.createAdmin(90123, 'pword', 'Haley', 'McGuire', 'Associate Registrar', 'Williston101', 'mcguireh')
    #admin.createAdmin(67824, 'pword', 'Tom', 'Cat', 'Registrar', 'Williston110', 'catt')

    #15 instructors             ( id,   pword,  fname,      lname,          title,          hireyear,       dept,                   email   )
    instructor.createInstructor(20110, 'pword', 'Aaron', 'Carpenter', 'Assistant Professor', '2002', 'Electrical Engineering', 'acarpenter')
    instructor.createInstructor(20842, 'pword', 'Ahmed', 'Hassebo', 'Visiting Assistant Professor', '2020', 'Electrical Engineering', 'hasseboa')
    instructor.createInstructor(20102, 'pword', 'Saurav', 'Basnet', 'Assistant Professor', '2019', 'Computer Engineering', 'basnets')
    instructor.createInstructor(20992, 'pword', 'Marisha', 'Rawlins', 'Professor', '2000', 'Computer Engineering', 'rawlinsm') 
    instructor.createInstructor(21182, 'pword', 'Tugba', 'Arsava', 'Associate Professor', '2010', 'Civil Engineering', 'arsavat')
    instructor.createInstructor(20999, 'pword', 'Leonard', 'Anderson', 'Associate Professor', '2018',  'Civil Engineering', 'andersonl')
    instructor.createInstructor(20265, 'pword', 'Uri', 'Feldman', 'Assistant Professor', '2014', 'Biomedical Engineering', 'feldmanu')
    instructor.createInstructor(20555, 'pword', 'Ali', 'Kiapour', 'Associate Professor', '2016', 'Biomedical Engineering', 'kiapoura')
    instructor.createInstructor(20340, 'pword', 'Hank', 'Pham', 'Assistant Professor', '2012', 'Computer Science', 'hpham')     
    instructor.createInstructor(20689, 'pword', 'Magdy', 'Ellabidy', 'Assistant Professor', '2017', 'Computer Science', 'ellabidym')
    instructor.createInstructor(21832, 'pword', 'Sunjae', 'Park', 'Assistant Professor', '2018', 'Computer Science', 'parks')
    instructor.createInstructor(21820, 'pword', 'Leon', 'Cort', 'Professor', '2009', 'Humanities', 'cortl')
    instructor.createInstructor(21756, 'pword', 'Allison', 'Lange', 'Associate Professor', '2020', 'Humanities', 'langea')
    instructor.createInstructor(21233, 'pword', 'Barry', 'Husowitz', 'Assistant Professor', '2015', 'Applied Mathematics', 'husowitzb')
    instructor.createInstructor(21543, 'pword', 'Alexander', 'Meill', 'Assistant Professor', '2016', 'Sciences', 'meilla')


    #18 students         ( id,    pword,  fname, lname,  gradyear, major, email )
    student.createStudent(30181, "pword", "Bob", "Dylan", "2023", "BSCO", "dylanbob")       #BS Computer Engineering
    student.createStudent(30182, 'pword', 'Zach', 'Ray', '2023', 'BSCO', 'rayz')
    student.createStudent(30183, "pword", "Jimmy", "Dean", "2030", "BSEE", "deanjim")       #BS Electrical Engineering
    student.createStudent(30184, 'pword', 'Amelina', 'Mille', '2026', 'BSEE', 'millea')
    student.createStudent(30185, "pword", "Harold", "Columbus", "2025", "BSCS", "columbush")#BS Computer Science
    student.createStudent(30186, "pword", "Mark", "Mii", "2023", "BSCS", "miim")
    student.createStudent(30187, 'pword', 'Alex', 'Creem', '2022', 'BSCS', 'creema')
    student.createStudent(30188, 'pword', 'Tyler', 'Crepeau', '2022', 'BSCS', 'crepeaut')
    student.createStudent(30922, 'pword', 'Ifeoma', 'Kirils', '2022', 'BSCE', 'kirilsi')    #BS Civil Engineering
    student.createStudent(30289, 'pword', 'Hermine', 'Natalka', '2024', 'BSCE', 'natalkah')
    student.createStudent(30100, 'pword', 'Charleen', 'Tymoon', '2023', 'BSCE', 'tymoonc')
    student.createStudent(30221, 'pword', 'Yvonne', 'Karan', '2023', 'BSBE', 'karany')      #BS Biomedical Engineering
    student.createStudent(30991, 'pword', 'Kinich', 'Rayen', '2025', 'BSBE', 'rayenk')
    student.createStudent(30766, 'pword', 'Ronald', 'Isaac', '2026', 'BSBE', 'isaacr')
    student.createStudent(30767, 'pword', 'Johanna', 'Mack', '2027', 'BSBE', 'mackj')
    student.createStudent(30768, 'pword', 'Charlie', 'Stewart', '2027', 'BAM', 'stewartc')  #Bachelors Applied Math
    student.createStudent(30769, 'pword', 'Clay', 'Casey', '2026', 'BAM', 'caseyc')
    student.createStudent(30800, 'pword', 'Marta', 'Wright', '2025', 'BAM', 'wrightm')

    #ELEC COURSES                                                                                                               # <matching instructor>
    course.createCourse(300100, "Analog Circuit Design", "ELEC", "MWF", "12:00pm-1:20pm", "Spring", "2022", 3, 20110)           # aaron carpenter
    course.createCourse(300200, "Digital Circuit Design", "ELEC", "MWF", "2:00pm-3:20pm", "Spring", "2022", 3, 20110)           # aaron carpenter
    course.createCourse(300300, "Cyber-Physical Systems", "ELEC", "WF", "1:00pm-2:50pm", "Spring", "2022", 3, 20842)            # ahmed hassebo
    course.createCourse(300400, "Computer Architecture", "ELEC", "TR", "4:00pm-6:00pm", "Spring", "2022", 3, 20992)             # marisha rawlins
    course.createCourse(401532, "Parallel Computer Architecture", "ELEC", "TR", "11:00am-12:00pm", "Spring", "2022", 3, 20992)  # marisha rawlins
    course.createCourse(401243, "Signals and Systems", "ELEC", "WF", "8:00am-9:50am", "Spring", "2022", 3, 20102)               # saurav basnet
    #Physics
    course.createCourse(402100, "Physics 1", "PHYS", "MWF", "10:00am-11:50am", "Spring", "2022", 3, 21543)                      # alexander meill
    course.createCourse(402200, 'Thermal Physics', 'PHYS', 'MWF', '12:00pm-1:50pm', 'Spring', '2022', 4, 21543)                 # alexander meill
    #Engineering
    course.createCourse(403100, 'Introduction to Engineering', 'ENGR', 'MW', '8:00am-9:20am', 'Spring', '2022', 3, 21182)       # tugba arsava
    course.createCourse(403200, 'Fundamentals of CAD & CAM', 'ENGR', 'TR', '8:00am-9:20am', 'Spring', '2022', 1, 20999)         # leonard anderson
    course.createCourse(403300, 'Programming with MATLAB', 'ENGR', 'WF', '10:00am-11:50am', 'Spring', '2022', 1, 20842)         # ahmed hassebo
    #Humanities
    course.createCourse(404900, 'Shakespeare on Film', 'HUMN', 'TR', '3:00pm-4:50pm', 'Spring', '2022', 4, 21820)               # leon cort
    course.createCourse(404800, 'Renaissance to Romanticisim', 'HUMN', 'TR', '12:00pm-1:50pm', 'Spring', '2022', 4, 21820)      # leon cort
    course.createCourse(404700, 'The American Dream', 'HUMN', 'TR', '8:00am-9:50am', 'Spring', '2022', 4, 21756)                # allison lange
    #Civil Engineering
    course.createCourse(405500, 'Introduction to Geomatics', 'CIVE', 'MWF', '8:00am-9:50am', 'Spring', '2022', 4, 21182)        # tugba arsava
    course.createCourse(405600, 'Fluid Mechanics', 'CIVE', 'MWF',  '11:00am-12:50pm', 'Spring', '2022', 4, 20999)               # leonard anderson
    #Biomedical Engineering
    course.createCourse(406000, 'Physiology for Engineers', 'BMED', 'WF', '8:00am-9:50am', 'Spring', '2022', 4, 20265)          # uri feldman
    course.createCourse(406100, 'Medical Devices and Systems', 'BMED', 'WF', '11:00am-12:50pm', 'Spring', '2022', 4, 20555)     # ali kiapour
    #Computer science
    course.createCourse(406200, 'Computer Science', 'COMP', 'MWF', '12:00pm-1:50pm', 'Spring', '2022', 4, 20340)                # hank pham
    course.createCourse(406300, 'Introduction to Networks', 'COMP', 'WF', '2:00pm-3:50pm', 'Spring', '2022', 4, 20689)          # magdy ellabidy
    course.createCourse(406400, 'Data Structures', 'COMP', 'MWF', '4:00pm-5:20pm', 'Spring', '2022', 4, 21832)                  # sunjae park


    