# Generated by Django 4.0.3 on 2022-06-29 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminManagement', '0002_remove_contrato_clienteid_remove_contrato_parqueid_and_more'),
        ('OperationManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, db_column='Nome', max_length=255, null=True)),
                ('nif', models.IntegerField(blank=True, db_column='NIF', null=True)),
                ('morada', models.CharField(blank=True, db_column='Morada', max_length=255, null=True)),
                ('data_de_nascimento', models.DateTimeField(blank=True, db_column='Data de nascimento', null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=255, null=True)),
                ('telemovel', models.CharField(blank=True, db_column='Telemovel', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('matricula', models.CharField(blank=True, db_column='Matricula', max_length=255, null=True)),
                ('data_de_inicio', models.DateField(blank=True, db_column='Data de inicio', null=True)),
                ('data_de_termino', models.DateField(blank=True, db_column='Data de termino', null=True)),
                ('valido', models.BooleanField(blank=True, db_column='Valido', max_length=255, null=True)),
                ('clienteid', models.ForeignKey(db_column='ClienteID', default=1, on_delete=django.db.models.deletion.CASCADE, to='PaymentManagement.cliente')),
                ('parqueid', models.ForeignKey(db_column='ParqueID', default=1, on_delete=django.db.models.deletion.CASCADE, to='AdminManagement.parque')),
            ],
            options={
                'db_table': 'Contrato',
            },
        ),
        migrations.CreateModel(
            name='Fatura',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nomeEmpresa', models.TextField(db_column='NomeEmpresa')),
                ('moradaEmpresa', models.TextField(db_column='MoradaEmpresa')),
                ('nifEmpresa', models.IntegerField(blank=True, db_column='NIFEmpresa', null=True)),
                ('clienteid', models.ForeignKey(blank=True, db_column='ClienteID', null=True, on_delete=django.db.models.deletion.CASCADE, to='PaymentManagement.cliente')),
            ],
            options={
                'db_table': 'Fatura',
            },
        ),
        migrations.CreateModel(
            name='Periodicidade',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('periodicidade', models.CharField(blank=True, db_column='Periodicidade', max_length=255, null=True)),
                ('horario', models.CharField(blank=True, db_column='Horario', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Periodicidade',
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('data_de_inicio', models.DateTimeField(blank=True, db_column='Data de inicio', null=True)),
                ('data_de_termino', models.DateTimeField(blank=True, db_column='Data de termino', null=True)),
                ('parqueid', models.ForeignKey(db_column='ParqueID', default=1, on_delete=django.db.models.deletion.CASCADE, to='AdminManagement.parque')),
                ('viaturaid', models.ForeignKey(db_column='ViaturaID', default=1, on_delete=django.db.models.deletion.CASCADE, to='OperationManagement.viatura')),
            ],
            options={
                'db_table': 'Reserva',
            },
        ),
        migrations.CreateModel(
            name='TabelaPrecos',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('preco_por_hora', models.FloatField(db_column='Preco por hora')),
                ('taxa_por_hora', models.FloatField(db_column='Taxa por hora')),
                ('taxa_noturna', models.FloatField(db_column='Taxa noturna')),
                ('taxa_da_multa', models.FloatField(db_column='Taxa da multa')),
                ('preco_contrato_dia', models.FloatField(db_column='Preco Contrato Dia')),
                ('preco_contrato_diurno', models.FloatField(db_column='Preco Contrato Diurno')),
                ('preco_contrato_noturno', models.FloatField(db_column='Preco Contrato Noturno')),
                ('parqueid', models.ForeignKey(db_column='ParqueID', on_delete=django.db.models.deletion.CASCADE, to='AdminManagement.parque')),
                ('reservaid', models.ForeignKey(blank=True, db_column='ReservaID', null=True, on_delete=django.db.models.deletion.CASCADE, to='PaymentManagement.reserva')),
            ],
            options={
                'db_table': 'TabelaPrecos',
            },
        ),
        migrations.CreateModel(
            name='Reclamacao',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('reclamacao', models.CharField(blank=True, db_column='Reclamacao', max_length=255, null=True)),
                ('faturaid', models.ForeignKey(blank=True, db_column='FaturaID', null=True, on_delete=django.db.models.deletion.CASCADE, to='PaymentManagement.fatura')),
            ],
            options={
                'db_table': 'Reclamacao',
            },
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('montante', models.FloatField(db_column='Montante')),
                ('estado_do_pagamento', models.TextField(db_column='Estado do pagamento')),
                ('data_de_vencimento', models.DateTimeField(blank=True, db_column='Data de vencimento', null=True)),
                ('comprovativo', models.FileField(blank=True, null=True, upload_to='')),
                ('contratoid', models.ForeignKey(blank=True, db_column='ContratoID', null=True, on_delete=django.db.models.deletion.CASCADE, to='PaymentManagement.contrato')),
                ('registoid', models.ForeignKey(blank=True, db_column='RegistoID', null=True, on_delete=django.db.models.deletion.CASCADE, to='OperationManagement.registomovimento')),
                ('reservaid', models.ForeignKey(blank=True, db_column='ReservaID', null=True, on_delete=django.db.models.deletion.CASCADE, to='PaymentManagement.reserva')),
            ],
            options={
                'db_table': 'Pagamento',
            },
        ),
        migrations.AddField(
            model_name='fatura',
            name='pagamentoid',
            field=models.ForeignKey(blank=True, db_column='PagamentoID', null=True, on_delete=django.db.models.deletion.CASCADE, to='PaymentManagement.pagamento'),
        ),
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, db_column='Dia', max_length=255, null=True)),
                ('periodicidadeid', models.ForeignKey(db_column='Periodicidade', default=1, on_delete=django.db.models.deletion.CASCADE, to='PaymentManagement.periodicidade')),
            ],
            options={
                'db_table': 'Dia',
            },
        ),
        migrations.AddField(
            model_name='contrato',
            name='periodicidadeid',
            field=models.ForeignKey(db_column='PeriodicidadeID', default=1, on_delete=django.db.models.deletion.CASCADE, to='PaymentManagement.periodicidade'),
        ),
    ]
