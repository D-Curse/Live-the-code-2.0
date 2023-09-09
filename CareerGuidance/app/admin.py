from django.contrib import admin
from .models import Course
from .models import Details, EduDetails, Gallery

# Register your models here.

admin.site.register(Course)
admin.site.register(Details)
admin.site.register(EduDetails)
admin.site.register(Gallery)