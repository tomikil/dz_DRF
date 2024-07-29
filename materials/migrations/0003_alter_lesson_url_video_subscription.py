# Generated by Django 5.0.7 on 2024-07-26 11:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_course_owner_lesson_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='url_video',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='ссылка на видео'),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='materials.course', verbose_name='курс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'подписка',
                'verbose_name_plural': 'подписки',
            },
        ),
    ]
