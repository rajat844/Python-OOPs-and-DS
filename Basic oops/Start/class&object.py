class Student:
     def __init__(self, name,major,gpa,isOnProbation):
         self.name = name
         self.major = major
         self.gpa = gpa
         self.isOnProbation = isOnProbation


student1 = Student("Jim","CS",3.2,False)
student2 = Student("Love","CS",2.2,True)

print(student1)