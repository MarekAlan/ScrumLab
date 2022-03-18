# Generated by Django 2.2.6 on 2022-03-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0010_merge_20220316_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayname',
            name='name',
            field=models.CharField(choices=[('Mon', 'Poniedziałek'), ('Tue', 'Wtorek'), ('Wed', 'Środa'), ('Thu', 'Czwartek'), ('Fri', 'Piątek'), ('Sat', 'Sobota'), ('Sun', 'Niedziela')], max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]