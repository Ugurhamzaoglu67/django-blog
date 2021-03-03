from django.contrib import admin
from django.contrib.auth.admin  import UserAdmin
from account.models import  CustomUserModel


@admin.register(CustomUserModel)
class CustomAdmin(UserAdmin):
      list_dispaly = ('username','email')
      fieldsets = UserAdmin.fieldsets + (('Avatar Değiştirme Alanı', {
                  'fields' : ['avatar']}) , ) #UserAdmin.fieldsets+e bir  tuple  ve dict ekleyerek ilave


