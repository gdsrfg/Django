# Generated by Django 4.1.5 on 2023-02-03 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('model_prod', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(upload_to='product')),
            ],
        ),
    ]