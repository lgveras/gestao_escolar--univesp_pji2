# Generated by Django 4.0.4 on 2022-06-19 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaConhecimento',
            fields=[
                ('codigo', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('matricula', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('idade', models.IntegerField()),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=200)),
                ('carga_horaria', models.IntegerField(null=True)),
                ('periodo', models.IntegerField(null=True)),
                ('contagem_periodo', models.CharField(max_length=10, null=True)),
                ('ano_oferta', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField(null=True)),
                ('fim', models.DateField(null=True)),
                ('ano_semestre', models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiarioAlunos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diario_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='escolar.diario')),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('cadastro_fk', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='escolar.cadastro')),
                ('serie', models.IntegerField(null=True)),
                ('curso_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='escolar.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gestor', models.BooleanField()),
                ('cadastro_fk', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='escolar.cadastro')),
            ],
        ),
        migrations.CreateModel(
            name='FaltasDiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_presenca', models.DateField(null=True)),
                ('presenca', models.BooleanField(null=True)),
                ('diario_alunos_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='escolar.diarioalunos')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('carga_horaria', models.IntegerField(null=True)),
                ('area_conhecimento_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='escolar.areaconhecimento')),
                ('curso_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='escolar.curso')),
            ],
        ),
        migrations.AddField(
            model_name='diario',
            name='disciplina_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='escolar.disciplina'),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('cadastro_fk', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='escolar.cadastro')),
                ('area_conhecimento_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='escolar.areaconhecimento')),
            ],
        ),
        migrations.AddField(
            model_name='diarioalunos',
            name='aluno_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='escolar.aluno'),
        ),
        migrations.AddField(
            model_name='diario',
            name='professor_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='escolar.professor'),
        ),
    ]
