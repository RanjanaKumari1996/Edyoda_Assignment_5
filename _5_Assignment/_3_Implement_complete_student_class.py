class Student:
    __name=""
    __rollnumber=""
    student_name="Harsh"

    def setName(self,name1):
        self.__name=name1

    def getName(self):
        return self.__name

    def setRollNumber(self,rollno):
        self.__rollnumber=rollno

    def getRollNumber(self):
        return self.__rollnumber

Private_name=input("Enter student name: ")
Private_rollnumber=int(input("Enter student rollnumber: "))
print(end="\n")

Student_obj=Student()

Student_obj.setName(Private_name)
print("Name of Private Student: ",Student_obj.getName())

Student_obj.setRollNumber( Private_rollnumber)
print("Roll number of Private student: ",Student_obj.getRollNumber())

#Public properties are  accessible through the class object

print("Public student name: ", Student_obj.student_name)

#Private properties are not accessible through the class object

print(Student_obj.__name)     

     
