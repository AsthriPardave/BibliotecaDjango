# Generated by Django 5.0.4 on 2024-04-12 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='descripcion',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='fallecimiento',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nacimiento',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
