
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, CreateView,UpdateView,DeleteView, TemplateView, View
from apps.movimientos.models import *
from apps.movimientos.forms import *
from django.contrib.auth import authenticate, login

from django.contrib import messages
from django.urls import reverse_lazy


import datetime
 

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
        movs=Movimiento.objects.all().order_by('-pk')
            
        jsn ={
            'msj':'llegó',
            'alojadores':ajdrs,
            'movs':movs
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
            'procesos':procesos,
        }
        return render(request,'pag/c_lst.html',jsn)


from django.db.models import Q
class ActulizarUbicacion(View):

    def get(self, request, *args, **kwargs):
        cod = self.request.GET.get('cod')
        mov = self.request.GET.get('mov')
        alj = self.request.GET.get('alj')
        pos = self.request.GET.get('pos')

        rpta = "false"

        #print("   > cod:"+cod+"   > mov:"+mov+"   > alj:"+alj+"  >pos:"+pos)

        if Cinta.objects.filter(codigo=cod).exists():
            cnta=Cinta.objects.get(codigo=cod)
   
            if UbicacionCinta.objects.filter(Q(id_cinta=cnta) & Q(estado=1)).exists():
                UbicacionCinta.objects.filter(id_cinta=cnta).update(estado=2)
                print(" ->> Ubicación anerior descartada / se crea nueva ")
            else:
                print("   :. no existen ubicaciones anteriores.")

            alj1=Alojadores.objects.get(pk=alj)
            mov1=Movimiento.objects.get(pk=mov)
            ubcnt = UbicacionCinta(id_cinta =cnta,id_alojador=alj1,id_movimiento=mov1,posicion=pos,estado=1)
            ubcnt.save()
            rpta="true"
        return HttpResponse(rpta)

class  MovimientoCreate(CreateView):
    model=Movimiento
    form_class=MovimientoForm
    template_name='pag/m_cre.html'
    success_url=reverse_lazy('c_reordenar')

class  MovimientoCreate1(View):

    def get(self, request, *args, **kwargs):
        print("  > GET")
        ida = self.request.GET.get('id_asuth')
        des = self.request.GET.get('razon')
        print("  -> GET: "+str(ida)+"   ->"+des)
        return reverse_lazy('c_reordenar')

    def post(self, request, *args, **kwargs):
        ida = self.request.POST.get('id_asuth')
        des = self.request.POST.get('razon')
        aut = AuthUser.objects.get(pk=ida)
        dat=datetime.datetime.now()
        hor=datetime.datetime.now()

        movs=Movimiento.objects.all().order_by('-pk')

        Mvnto=Movimiento(id_asuth=aut,fecha =dat,hora =hor,razon=des)
        Mvnto.save()
        print("   > se guardó")

        ajdrs=Alojadores.objects.all()
        jsn ={
            'msj':'llegó',
            'alojadores':ajdrs,
            'movs':movs
        }
        return render(request,'pag/c_reordenar.html',jsn)


class CinLstAlj(View):

    def get(self, request, *args, **kwargs):
        ida = self.request.GET.get('ida')
        print("  > "+str(ida))
        from django.db import connection, transaction
        cursor = connection.cursor()
        cursor.execute("CALL sp_lst_cin_alsj (%s)",[ida])

        lstCnts = []
        detalles = cursor.fetchall()
        for row in detalles:
            dic = dict(zip([col[0] for col in cursor.description], row))
            lstCnts.append(dic)
        cursor.close()
       

        aljs1=Alojadores.objects.all().order_by('nombre')
        for a in aljs1:
            print(" ->"+a)

        print("  > "+str(ida))

        jsn = {
            'msj':'llegó',
            'aljs':Alojadores.objects.all().order_by('nombre'),
            'lstCnts':lstCnts
        }
        return render(request,'pag/c_lst_alj.html',jsn)



class AljCreate(CreateView):
    model=Alojadores
    form_class=AljForm
    template_name='alj/a_reg.html'
    success_url=reverse_lazy('a_lis')

class  AljUpdate(UpdateView):
    model=Alojadores
    form_class=AljForm
    template_name='alj/a_reg.html'
    success_url=reverse_lazy('a_lis')

class  AljDelete(DeleteView):
    model=Alojadores
    form_class=AljForm
    template_name='alj/a_eli.html'
    success_url=reverse_lazy('a_lis')

class  AljList(ListView):
    model=Alojadores
    template_name='alj/a_lis.html'
    paginate_by=9




class ProyCreate(CreateView):
    model=Proyectos
    form_class=ProyForm
    template_name='proy/p_reg.html'
    success_url=reverse_lazy('a_lis')

class  ProyUpdate(UpdateView):
    model=Proyectos
    form_class=ProyForm
    template_name='proy/p_reg.html'
    success_url=reverse_lazy('a_lis')

class  ProyDelete(DeleteView):
    model=Proyectos
    form_class=ProyForm
    template_name='proy/p_eli.html'
    success_url=reverse_lazy('a_lis')

class  ProyList(ListView):
    model=Proyectos
    template_name='proy/p_lis.html'
    paginate_by=9
