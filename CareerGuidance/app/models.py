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
