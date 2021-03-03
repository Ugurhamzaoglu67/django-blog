
"""
AMAÇ : Ortak alanları, soyut bir modelin içinde grupluyoruz..
"""
from django.db import models

class DateAbstractModel(models.Model):
      olusturulma_tarihi = models.DateTimeField(auto_now_add = True) # Oto oluşturulan Tarihi vericek
      duzenleme_tarihi = models.DateTimeField(auto_now=True)          #Yazilar tablosunda bu içerik, her değiştirildiğinde  oto olarak düzenlendiği tarih için



      class Meta:
            abstract = True # Bizim için artık soyut olduğunu ifade ediyoruz.
            