from django.shortcuts import render

def iletisim(request):
      return render(request,'pages/iletisim.html', context= {})  #2.Parametre , YORUMLANACAK TEMPLATE YOLU OLCAK.