# Generated by Django 5.0.2 on 2024-02-25 21:18


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_alter_post_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='visibility',

            field=models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('UNLISTED', 'UNLISTED'), ('FRIENDS', 'FRIENDS')], default='PUBLIC', max_length=10),
        ),
    ]
