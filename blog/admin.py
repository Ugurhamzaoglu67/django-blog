from django.contrib import admin
from blog.models import (
      KategoriModel,YazilarModel, YorumModel 
) # tuple içinde, güzel görünsün ...

admin.site.register(KategoriModel)


class YazilarAdmin(admin.ModelAdmin):
      search_fields = ('baslik','icerik') #baslik ve icerik'te ara
      list_display= ('baslik', 'olusturulma_tarihi', 'duzenleme_tarihi')


admin.site.register(YazilarModel, YazilarAdmin)


class YorumAdmin(admin.ModelAdmin):
      list_display =('yazan_kisi','yorum_olusturulma_tarihi', 'yorum_duzenlenme_tarihi') #admin panelinde gözükmesini istediğimiz...
      search_fields = ('yazan_kisi__username',) # yazan_kisi obje olduğu için onun username'ine göre arama yap dedik 


admin.site.register(YorumModel, YorumAdmin) # ModelAdmin'den TÜREMİŞ, YorumAdmin Class'ını