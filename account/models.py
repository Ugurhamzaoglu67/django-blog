from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
      avatar = models.ImageField(upload_to ='avatar/', blank =True, null= True) #avatar diye klasör oluştur, resimleri ben yükleyince sen oraya taşı


      class Meta:
            db_table = 'user' #tablo oluşturuyoruz.
            verbose_name = 'Kullanıcı'
            verbose_name_plural = 'Kullanıcılar'


      def __str__(self):
            return self.username

#1___________ bunu hemen migrate etmeyecez, Djangonun default kullandığı authuser modelini, biz kullanmak istemiyoruz. Onun yerine kendi oluşturduğumuz modeli kullanmak istiyoruz demek gerek: 
#root(config)-> settings.py  -> AUTH_USER_MODEL  değişkeni oluşturcaz.
#2___________ Yazilar & Yorum' la oluşturduğumuz usermodeli ilişkilendir
# accout-> yazi.py ve yorum.py User yazan yerlere : 'account.CustomUserModel' ilişkilendir.
#3___________ sonra makemigrations & migrate....