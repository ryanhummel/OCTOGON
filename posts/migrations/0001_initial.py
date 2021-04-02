# Generated by Django 3.1.7 on 2021-04-01 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_ID', models.IntegerField(default=0)),
                ('thread_date', models.DateTimeField(verbose_name='published: ')),
                ('main_post_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_ID', models.IntegerField(default=0)),
                ('user_ID', models.IntegerField(default=0)),
                ('post_date', models.DateTimeField(verbose_name='published:')),
                ('main_text', models.TextField()),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.thread')),
            ],
        ),
    ]