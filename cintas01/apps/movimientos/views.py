
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, CreateView,UpdateView,DeleteView, TemplateView, View
from apps.movimientos.models import *
from django.contrib.auth import authenticate, login



def index(request):
	return render(request,'index.html')



def mylogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request,'Datos incorrectos!!')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')



class CinFiltrar(View):
    def get(self, request, *args, **kwargs):
        ci=Cinta.objects.all()
        print("  <->")
        jsn = {
            'msj':'ok',
            'cintas':ci
        }
        for c in ci:
            print(" >-> "+c.codigo+" || "+str(c.Proyecto.cliente))
        return render(request,'pag/c_lst.html',jsn)
		
 
