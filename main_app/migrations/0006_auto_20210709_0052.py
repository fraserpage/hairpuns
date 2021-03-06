# Generated by Django 3.2.4 on 2021-07-09 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_visits_visit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='visit',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='hairpun',
            name='categories',
            field=models.ManyToManyField(to='main_app.Category'),
        ),
    ]
