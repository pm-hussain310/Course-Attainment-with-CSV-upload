# Generated by Django 4.2.7 on 2024-02-29 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0005_rename_po_pso_pso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='co_po_mapping',
            name='po_mapped',
        ),
        migrations.AddField(
            model_name='co_po_mapping',
            name='po_mapped',
            field=models.ManyToManyField(to='testApp.po'),
        ),
    ]
