# Generated by Django 2.0.5 on 2018-06-18 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CertificateWeb', '0003_cerapply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('serialNumber', models.CharField(max_length=400)),
                ('file', models.FileField(upload_to='CertificateWeb/static/certificate')),
            ],
        ),
    ]
