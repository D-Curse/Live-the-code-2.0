from django.db import models

# Create your models here.

class Course(models.Model):
    BRANCH_CHOICES = (
        ('Science', 'science'),
        ('Commerce', 'commerce'),
        ('Arts', 'arts'),
    )
    
    index = models.IntegerField(primary_key=True)
    field_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100, choices=BRANCH_CHOICES)

    def __str__(self):
        return f"{self.field_name} - {self.branch}"

class Details(models.Model):
    CATEGORY_CHOICES = (
        ('Pros','pros'),
        ('Cons','cons'),
    )  
    
    main_head = models.CharField(max_length=100)
    image = models.ImageField(upload_to='data/media')
    
    about_career_head = models.CharField(max_length=100)
    about_career_para = models.TextField()
    

    def __str__(self):
        return self.main_head
    
class EduDetails(models.Model):
    
    main_head = models.CharField(max_length=100)
    edu_stream = models.CharField(max_length=100)
    edu_graduation = models.CharField(max_length=100)
    edu_after_grad = models.CharField(max_length=100)
    edu_post_grad = models.CharField(max_length=100)
    
    def __str__(self):
        return self.main_head
    
