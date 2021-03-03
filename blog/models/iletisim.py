from django.db import models



class IletisimModel(models.Model):
      email = models.EmailField(max_length = 250) #NEDEN EmailField()   ? ->**Auto Olarak Email Validation Yapılıyor Django tarafından...
      isim_soyisim = models.CharField(max_length= 150)
      mesaj = models.TextField()
      iletisim_olusturulma_tarihi = models.DateTimeField(auto_now_add = True) # Otomatik olarak bize gönderi geldiğinde,  oluşturulma tarihide kayıtolsun ve ne zaman gönderdiklerini tutalım..


      class Meta:
            db_table = 'iletisim' #SqLite Explorer'de 'iletisim' adında tutulsun..
            verbose_name = 'İletişim' #Admin panelde , sol taraftaki yerde görünen
            verbose_name_plural = 'İletişim'

      def __str__(self):
            return self.email

#1_________ models içindeki __init__.py'e ekle : blog -> models -> __init__.py
#2___________ makemigrations & migrate işlemleri unutma_______________
#3___________ iletişim modelini -> admin.py işle..