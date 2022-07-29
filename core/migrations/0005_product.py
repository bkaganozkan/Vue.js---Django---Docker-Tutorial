# Generated by Django 4.0.6 on 2022-07-23 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_user_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('image', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]