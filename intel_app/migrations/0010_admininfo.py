# Generated by Django 4.1 on 2023-08-10 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0009_alter_customuser_wallet'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_number', models.BigIntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('momo_number', models.PositiveBigIntegerField(blank=True, null=True)),
            ],
        ),
    ]
