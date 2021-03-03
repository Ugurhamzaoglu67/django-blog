from django.shortcuts import render


def anasayfa(request):
      context = {
            'name' : 'UGURR'
      }
      return render(request,'pages/anasayfa.html',context = context)