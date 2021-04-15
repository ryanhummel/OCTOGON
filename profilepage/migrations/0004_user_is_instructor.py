# Generated by Django 3.1.7 on 2021-04-15 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilepage', '0003_remove_user_is_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_instructor',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
            preserve_default=False,
        ),
    ]
