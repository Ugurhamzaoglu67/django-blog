from django.shortcuts import render
from blog.models  import YazilarModel
from django.core.paginator import Paginator

def anasayfa(request):
      yazilar = YazilarModel.objects.order_by('-id') #en son yazı
      sayfa=request.GET.get('sayfa')
      paginator = Paginator(yazilar,2) #Bir sayafada kaç kayıt olsun -> 2
      
      context = {

            'yazilar':paginator.get_page(sayfa)
      }

      return render(request,'pages/anasayfa.html', context)