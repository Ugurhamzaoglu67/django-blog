from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
from django.contrib.auth.models import User #ForeignKey 'i User'e bağlamak için.
from ckeditor.fields import RichTextField




class YazilarModel(models.Model):
      resim = models.ImageField(upload_to = 'yazi_resimleri')
      baslik = models.CharField(max_length=50)
      icerik = RichTextField()
      olusturulma_tarihi = models.DateTimeField(auto_now_add = True) # Oto oluşturulan Tarihi vericek
      duzenleme_tarihi = models.DateTimeField(auto_now=True)          #Yazilar tablosunda bu içerik, her değiştirildiğinde  oto olarak düzenlendiği tarih için
      slug = AutoSlugField(populate_from ='baslik', unique= True) #Başlığa göre slug
      kategoriler = models.ManyToManyField(KategoriModel, related_name='yazi') #Bir yazının, kategori sayısı => 1   olması için ManyToMany.
      # 1 kategoriye ait, bütün yazılara  erişmek için  related_name kullanıyoruz   
      yazar = models.ForeignKey(User, on_delete=models.CASCADE ,related_name ='yazilar') #ForeignKey: Bir tabloyu, Başka bir tabloyla ilişkilendirmemize yarar.
      #Yazar üzerinden, Tüm Yazılarına erişmek içinde related_name='yazilar'
      #User silinirse db'den, ona ait tüm her şeyi silmek için:on_delete=models.CASCADE


      class Meta:
            verbose_name = 'Yazi'
            verbose_name_plural = 'Yazilar'
            db_table = 'Yazi'


#______________ YAZILAR MODELİ OLUSTURULDU -> makemigrations, migrate yap...

      def __str__(self):
            return self.baslik