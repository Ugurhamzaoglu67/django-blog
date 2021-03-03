from django.shortcuts import render

def iletisim(request):

      context = {
            'key' : 'baslik budur işte helloo...'
      }

      return render(request,'pages/iletisim.html', context= context)  #2.Parametre , YORUMLANACAK TEMPLATE YOLU OLCAK.