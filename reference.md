```python

class CourseGrade():
    student -> FK(student)
    course -> FK(course)

class CourseAttendance():
    student -> FK(student)
    course -> FK(course)
    datetime -> DateTime

class Courses():
    students -> M2M()
    # grade -> M2M()
    # course_obj.CourseGrade_set.all()
    # course_obj.CourseAttendance_set.all()

class Parent():
    name
    # parent_obj.student_set.all()


class Student():
    mother = FK(parent,related_name = "mother")
    father = FK(parent,related_name = "father")
    # student.mother
    # student.father
    # student.course_set.all()
    # courses -> M2M()
    # grades = M2M(Grade)
    # student.coursegrade_set.all()



```
