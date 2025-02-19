# Generated by Django 4.2.7 on 2024-03-02 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0018_rename_attainment_mid1_qp_attainment_level_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Attainment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final', models.FloatField(default=0, null=True)),
                ('co', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.co')),
                ('indirect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.indirect')),
            ],
        ),
        migrations.DeleteModel(
            name='CO_Attainment',
        ),
    ]
