# Generated by Django 3.2 on 2023-08-09 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0003_auto_20230806_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('메뉴얼', '메뉴얼'), ('카드뉴스', '카드뉴스')], max_length=30)),
                ('tags', models.CharField(blank=True, max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageMulti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='cardnews/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cardnews', to='boards.cardnews')),
            ],
        ),
        migrations.CreateModel(
            name='CardScrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scrap', models.BooleanField(default=None)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.cardnews')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_card', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
