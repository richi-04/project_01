from django.contrib import admin
from .models import Profile
from .forms import UserCreationForm, UserForm
from django.contrib.auth.admin import UserAdmin



# Register your models here.
# @admin.register(Profile)
# @admin.register(UserForm)
# class CustomAdmin(UserAdmin):
#     model = Profile
#     add_form = UserForm
#     list_display = ('username','email', 'phone', 'gender', 'password', 'hobby')

#     fieldsets = (
#         *UserAdmin.fieldsets,('User role',{"fields": ('gender',),}),)
    
admin.site.register(Profile)
