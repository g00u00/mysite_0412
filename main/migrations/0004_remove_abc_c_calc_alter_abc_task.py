# Generated by Django 4.0.3 on 2022-04-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_abc_a_alter_abc_b_alter_abc_c'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abc',
            name='c_calc',
        ),
        migrations.AlterField(
            model_name='abc',
            name='task',
            field=models.CharField(default='Равно ли С сумме A и B', max_length=256),
        ),
    ]
