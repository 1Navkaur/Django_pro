from django.db import models

class Student(models.Model):
  name = models.TextField(max_length=255)#consider as a var char 
  email = models.EmailField()   # auto_now :- bool
  roll_no=models.IntegerField(primary_key=True)
  DOA=models.DateField(auto_now_add=True)

class Classroom(models.Model):
  standard=models.TextField()
  classteacher=models.TextField(max_length=15)
  no_of_student=models.IntegerField()

class Teachers(models.Model):
  name = models.TextField(max_length=15)
  subject_of_teacher=models.TextField()
  teacher_id=models.IntegerField(primary_key=True)
  
class Marks(models.Model):
  DBMS=models.IntegerField()
  DSA=models.IntegerField()
  SE=models.IntegerField()
  DCCN=models.IntegerField()
  
 
#to know the  the number of object of perticular class <n>.object.get()
#Stu1=Student("Nav")