from django.db import models
from blog.models import YazilarModel

class YorumModel(models.Model):
      yazan_kisi = models.ForeignKey('account.CustomUserModel', on_delete = models.CASCADE, related_name='yorum')#yazan kisinin yorumuna erişim:related_name='yorum' # Eğerki Kullanıcı silinirse, bu kullanıcının'da yorumları silinsin, models.CASCADE
      yazilan_icerik= models.ForeignKey(YazilarModel, on_delete = models.CASCADE, related_name='yorumlar')#her yorum bir yazıya atılacak, her atılan yorumu bir yazıyla eşleştirecez bunun içinde YazilarModel'ini sayfaya dahil edecez.#birde her yorumu, yazı ilişkilendirme
            #yazilan_iceriğin yorumlarına erişmek için : related_name='yorumlar'
      yapilan_yorum = models.TextField()
      yorum_olusturulma_tarihi = models.DateTimeField(auto_now_add = True )
      yorum_duzenlenme_tarihi = models.DateTimeField(auto_now = True )

      class Meta:
            db_table = 'yorum' 
            verbose_name = 'Yorum'
            verbose_name_plural = 'yorumlar' # admin panelde çoğul geçen yerlere 'yorumlar'
      
      def __str__(self):
            return self.yazan_kisi.username



#1____________ Django Bunu algılayabilsin diye : models -> __init__.py Bunu import et
#2__________  makemigrations  & migrate işlemlerini yap.
#3___________ admin paneline işle...    blog -> admin.py 