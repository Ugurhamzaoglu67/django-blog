from django.db import models
from autoslug import AutoSlugField


class KategoriModel(models.Model):
      isim = models.CharField(max_length=30, blank= False, null= False)
      slug=AutoSlugField(populate_from='isim', unique=True) #isimden otomatik slug oluştur.
       # Bizim seolu linkler oluşturmamız gerekiyor, slug ile yapıyouz. İsimden türeyen
       #bir şey yapmak istiyorsak paket kurmamız gerek.

      class Meta:
            db_table= 'kategori'
            verbose_name_plural = "Kategoriler"
            verbose_name = "Kategori"

      def __str__(self):
            return self.isim