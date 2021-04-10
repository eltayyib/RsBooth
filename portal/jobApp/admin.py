from django.contrib import admin
from .models import CustomUser, Employer, Employee
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Register your models here.

# class CustomUserAdmin(UserAdmin):

#     add_form = UserCreationForm
#     form = UserChangeForm
   

    
    # fieldsets = (
    #     ('Permissions', {'fields': ('employer','employee')}),
    # )


admin.site.register(CustomUser)
admin.site.register(Employer)
admin.site.register(Employee)
