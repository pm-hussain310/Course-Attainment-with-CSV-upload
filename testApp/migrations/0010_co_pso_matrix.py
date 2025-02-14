# Generated by Django 4.2.7 on 2024-02-29 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0009_alter_co_po_matrix_po1_alter_co_po_matrix_po10_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CO_PSO_Matrix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pso1', models.CharField(choices=[('-', '-'), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10)),
                ('pso2', models.CharField(choices=[('-', '-'), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10)),
                ('pso3', models.CharField(choices=[('-', '-'), ('1', 1), ('2', 2), ('3', 3)], default='-', max_length=10)),
                ('co', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.co')),
            ],
        ),
    ]
