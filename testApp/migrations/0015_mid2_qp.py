# Generated by Django 4.2.7 on 2024-02-29 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0014_alter_co_co_alter_po_po_mid1_qp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mid2_QP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('co_mapped', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.co')),
            ],
        ),
    ]
