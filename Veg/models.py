from django.db import models
from .uitls import generate_slug

class ReceipeManager(models.manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)

# Create your models here.
class Receipe(models.Model):
   
    receipe_name=models.CharField(max_length=200)
    receipe_desc=models.TextField()
    slug=models.SlugField(unique=True, blank=True, null= True)
    receipe_image=models.ImageField(default='')

    # to temporary delete data:-
    is_delete=models.BooleanField(default=False)
   
#    we do swap
    objects=ReceipeManager()
    admin_objects=models.Manager()

    

    def save(self,*args, **kwargs):
        self.slug=generate_slug(self.receipe_name)
        super(Receipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.receipe_name


class Department(models.Model):
    department_name=models.CharField(max_length=100)

    def __str__(self):
        return self.department_name
    
    
class StudentID(models.Model):
    student_id=models.CharField(max_length=100)
    
    def __str__(self):
        return self.student_id

class Subject(models.Model):
    subject_name=models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name
    

class Student(models.Model):
    department=models.ForeignKey(Department, related_name='depart', on_delete=models.CASCADE)
    student_id=models.OneToOneField(StudentID, related_name='studentid', on_delete=models.CASCADE) 
    student_name=models.CharField(max_length=50)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)
    student_address=models.TextField()

    def __str__(self):
        return self.student_name

    class Meta:
        ordering=['student_name']
        verbose_name='student'

class SubjectMarks(models.Model):
    student=models.ForeignKey(Student, related_name='studentmarks', on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks=models.IntegerField()

    def __str__(self):
        return f'{self.student.student_name} {self.subject.subject_name}'
    
    class Meta:
        unique_together=['student','subject']

