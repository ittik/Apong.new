# Generated by Django 2.0.6 on 2018-08-02 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180725_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('image', models.ImageField(default='\\images\\icon-user-default.png', upload_to='images')),
                ('des', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
