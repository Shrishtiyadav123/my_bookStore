# Generated by Django 5.0 on 2024-01-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='Price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='Authorname',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='books',
            name='Bookname',
            field=models.CharField(max_length=600),
        ),
    ]
