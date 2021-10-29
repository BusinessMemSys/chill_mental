# Generated by Django 3.2.8 on 2021-10-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_commentpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentpost',
            old_name='post',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='commentpost',
            old_name='user',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='commentpost',
            name='created',
        ),
        migrations.RemoveField(
            model_name='commentpost',
            name='moder',
        ),
        migrations.RemoveField(
            model_name='commentpost',
            name='text',
        ),
        migrations.AddField(
            model_name='commentpost',
            name='comment',
            field=models.CharField(default=1, max_length=500, verbose_name='Текст комментария'),
            preserve_default=False,
        ),
    ]
