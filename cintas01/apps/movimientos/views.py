
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



class ReordenarCintas(View):

    def get(self, request, *args, **kwargs):
        ajdrs=Alojadores.objects.all()
        jsn ={
            'msj':'llegó',
            'alojadores':ajdrs
        }
        
        return render(request,'pag/c_reordenar.html',jsn)



class AlpListar(View):
    def get(self, request, *args, **kwargs):
        alps = Proyectos.objects.all()
        jsn = {
            'msj':'Lista de PROYECTOS',
            'alp':alps
        }
        return render(request,'pag/c_lst.html',jsn)
		
 
class CinLstAlp(View):

    def get(self, request, *args, **kwargs):
        alp = self.request.GET.get('alp')
        proy=Proyectos.objects.get(alp=alp)
        procesos=Proyectos.objects.all()

        for pc in procesos:
            print(" > "+pc.cliente)
            break


        from django.db import connection, transaction
        cursor = connection.cursor()
        cursor.execute("CALL sp_lst_alp (%s)",[alp])


        cintas = []
        detalles = cursor.fetchall()
        for row in detalles:
            dic = dict(zip([col[0] for col in cursor.description], row))
            cintas.append(dic)
        cursor.close()

        msj ="["+str(proy.alp)+"]:"+proy.nombre

        jsn = {
            'msj':msj,
            'cintas':cintas,
            'procesos':procesos
        }
        return render(request,'pag/c_lst.html',jsn)


from django.db.models import Q
class ActulizarUbicacion(View):

    def get(self, request, *args, **kwargs):
        cod = self.request.GET.get('cod')
        if Cinta.objects.filter(codigo=cod).exists():
            cnta=Cinta.objects.get(codigo=cod)
            print(" ->Cinntas ok")
        if UbicacionCinta.objects.filter(Q(id_cinta=cnta) & Q(estado=1)).exists():
            ubcnt=UbicacionCinta.objects.get(id_cinta=cnta)
            print(" ->>Ubicación ok")
        print(" >> ok;prueba LPOD03L5")

        return HttpResponse('ok')




#if HojaAsistencia.objects.filter(Q(id_asamblea=pk_asmb) & Q(id_auth_user=p.id_auth_user)).exists():