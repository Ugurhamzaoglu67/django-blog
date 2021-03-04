from django.shortcuts import render
from blog.models  import YazilarModel
from django.core.paginator import Paginator
from django.db.models import Q # ya da işlemi için



def anasayfa(request):
      sorgu = request.GET.get('sorgu')
      
      yazilar = YazilarModel.objects.order_by('-id') #en son yazı
      if sorgu:
            yazilar = yazilar.filter(
                  Q(baslik__icontains = sorgu) | 
                  Q(icerik__icontains = sorgu)
                  ).distinct()

      sayfa=request.GET.get('sayfa')
      paginator = Paginator(yazilar,2) #Bir sayafada kaç kayıt olsun -> 2
      
      context = {

            'yazilar':paginator.get_page(sayfa)
      }

      return render(request,'pages/anasayfa.html', context)