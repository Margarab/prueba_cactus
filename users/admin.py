from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    model = MyUser
    include = ('username', 'first_name', 'last_name', 'email', 'avatar', 'password')


admin.site.register(MyUser, UserAdmin)
