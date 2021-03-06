# Generated by Django 4.0.3 on 2022-07-01 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PaymentManagement', '0001_initial'),
        ('AdminManagement', '0001_initial'),
        ('OperationManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lugar',
            name='contratoid',
            field=models.ForeignKey(db_column='ContratoID', null=True, on_delete=django.db.models.deletion.CASCADE, to='PaymentManagement.contrato'),
        ),
        migrations.AddField(
            model_name='lugar',
            name='reservaid',
            field=models.ForeignKey(db_column='ReservaID', null=True, on_delete=django.db.models.deletion.CASCADE, to='PaymentManagement.reserva'),
        ),
        migrations.AddField(
            model_name='lugar',
            name='viaturaid',
            field=models.ForeignKey(db_column='ViaturaID', null=True, on_delete=django.db.models.deletion.CASCADE, to='OperationManagement.viatura'),
        ),
        migrations.AddField(
            model_name='lugar',
            name='zonaid',
            field=models.ForeignKey(db_column='ZonaID', on_delete=django.db.models.deletion.CASCADE, to='AdminManagement.zona'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='parqueid',
            field=models.ForeignKey(db_column='ParqueID', on_delete=django.db.models.deletion.CASCADE, to='AdminManagement.parque'),
        ),
        migrations.AddField(
            model_name='administrador',
            name='parqueid',
            field=models.ForeignKey(db_column='ParqueID', on_delete=django.db.models.deletion.CASCADE, to='AdminManagement.parque'),
        ),
    ]
