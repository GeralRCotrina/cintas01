# Generated by Django 2.2.4 on 2019-08-02 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimientos', '0002_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('alp', models.IntegerField()),
                ('descripcion', models.IntegerField()),
            ],
            options={
                'db_table': 'proyectos',
                'managed': False,
            },
        ),
    ]
