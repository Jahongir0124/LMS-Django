from django.contrib import admin
from . models import *
from django.contrib.auth.admin import UserAdmin
from . forms import UserCreateForm



class UserAdmin(UserAdmin):

    add_form = UserCreateForm
    model = User

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "email", "password1", "password2", "is_teacher", "is_student"
                
            )}
        ),
    )


    
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(User, UserAdmin)
