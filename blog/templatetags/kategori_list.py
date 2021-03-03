from django import  template
from blog.models import KategoriModel #db'den ...


register = template.Library()   #template tagları ve filter için 


@register.simple_tag #customtag olusturuldu gibi..
def kategori_list():
      kategoriler = KategoriModel.objects.all()
      return kategoriler
