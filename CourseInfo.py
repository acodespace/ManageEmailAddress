"""
Arzoo Shahzad
CMSY-156
Lab8: CourseInfo
"""

"""
Write a program that creates a directory containing course numbers
and the room numbers of the rooms where the courses meet. The
dictionary should have the following key-value pairs:
"""

CourseRoom = {'CS101':'3004', 'CS102':'4501', 'CS103':'6755', 'NT110':'1244', 'CM241':'1411'}

"""
The program should also create a dictionary containing course
numbers and the names of the instructors that teach each course.
The dictionary should have the following key-value pairs:
"""

CourseInstructor = {'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}

"""
The program should also create a dictionary containing course
numbers and the meeting times of each course. The dictionary should
have the following key-value pairs:
"""

CourseMeeting = {'CS101':'8:00am', 'CS102':'9:00am', 'CS103':'10:00am', 'NT110':'11:00am', 'CM241':'11:00pm'}

"""
The program should let the user enter a course number, and then it
should display the course's room number, instructor, and meeting
time.
"""
CourseNumber = input("Enter the course number ")

print("Class: ", CourseNumber)
print("Room: ", CourseRoom[CourseNumber])
print("Instructor: ", CourseInstructor[CourseNumber])
print("Time: ", CourseMeeting[CourseNumber])
