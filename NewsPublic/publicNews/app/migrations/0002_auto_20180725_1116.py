# Generated by Django 2.0.6 on 2018-07-25 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MOU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('start_date', models.DateField()),
                ('expire_date', models.DateField()),
                ('tpye', models.CharField(max_length=500)),
                ('contact', models.CharField(blank=True, max_length=500, null=True)),
                ('url', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='NewsPublic',
        ),
    ]