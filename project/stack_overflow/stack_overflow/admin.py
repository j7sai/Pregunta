from django.contrib import admin
from .models import Questions,User,Answers

# Register your models here.
admin.site.register(Questions)
admin.site.register(User)
admin.site.register(Answers)
