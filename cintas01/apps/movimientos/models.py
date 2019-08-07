# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alojadores(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion_cot = models.IntegerField()
    tamano = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alojadores'

    def Aljs(self):
        cadena="{1}"
        return cadena.format(self.pk,self.nombre)
        
    def __str__(self):
        return self.Aljs()


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

    def Usrr(self):
        cadena="{0} {1}"
        return cadena.format(self.first_name,self.last_name)
        
    def __str__(self):
        return self.Usrr()

class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cinta(models.Model):
    proyecto = models.ForeignKey('Proyectos', models.DO_NOTHING, db_column='proyecto')
    servicio = models.CharField(max_length=15)
    codigo = models.CharField(max_length=20)
    tipo = models.CharField(max_length=4, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cinta'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Movimiento(models.Model):
    id_asuth = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_asuth')
    fecha = models.DateField()
    hora = models.TimeField()
    razon = models.CharField(max_length=500)

    def Movim(self):
        cadena="Mov:[{0}] {1}[{2}]"
        return cadena.format(self.pk,self.fecha,self.hora)
        
    def __str__(self):
        return self.Movim()

    class Meta:
        managed = False
        db_table = 'movimiento'



class Proyectos(models.Model):
    nombre = models.CharField(max_length=150)
    cliente = models.CharField(max_length=100)
    alp = models.IntegerField()
    descripcion = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'proyectos'


class UbicacionCinta(models.Model):
    id_cinta = models.ForeignKey(Cinta, models.DO_NOTHING, db_column='id_cinta')
    id_alojador = models.ForeignKey(Alojadores, models.DO_NOTHING, db_column='id_alojador')
    id_movimiento = models.ForeignKey(Movimiento, models.DO_NOTHING, db_column='id_movimiento')
    posicion = models.IntegerField()
    estado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ubicacion_cinta'
