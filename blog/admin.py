from django.contrib import admin
from blog.models import (
      KategoriModel,YazilarModel, YorumModel,IletisimModel  
) # tuple içinde, güzel görünsün ...

admin.site.register(KategoriModel)

@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
      search_fields = ('baslik','icerik') #baslik ve icerik'te ara
      list_display= ('baslik', 'olusturulma_tarihi', 'duzenleme_tarihi')


@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
      list_display =('yazan_kisi','olusturulma_tarihi', 'duzenleme_tarihi') #admin panelinde gözükmesini istediğimiz...
      search_fields = ('yazan_kisi__username',) # yazan_kisi obje olduğu için onun username'ine göre arama yap dedik 

@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
      list_display = ('email','olusturulma_tarihi')
      search_fields=('email',)


