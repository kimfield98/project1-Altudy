# Generated by Django 3.2.18 on 2023-05-29 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0002_auto_20230529_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='내용')),
            ],
            options={
                'db_table': 'review',
            },
        ),
        migrations.RemoveField(
            model_name='comment',
            name='solution',
        ),
        migrations.AddField(
            model_name='comment',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.TextField(verbose_name='설명'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='Solution',
        ),
        migrations.AddField(
            model_name='review',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.problem', verbose_name='문제'),
        ),
        migrations.AddField(
            model_name='review',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
        migrations.AddField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reviews.review', verbose_name='리뷰'),
            preserve_default=False,
        ),
    ]
