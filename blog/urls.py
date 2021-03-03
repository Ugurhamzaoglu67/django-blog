from django.urls import path, include
from blog.views import iletisim, anasayfa, kategori #kategori view'ında çağırdık


urlpatterns = [
    path('', anasayfa, name='anasayfa'),
    path('iletisim', iletisim, name='iletisim'),
    path('kategori/<slug:kategoriSlug>', kategori, name='kategori')
]


