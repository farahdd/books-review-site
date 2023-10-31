# Generated by Django 4.2.6 on 2023-10-29 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('review', models.TextField(blank=True)),
                ('rating', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_reviews', to='books.book')),
            ],
            options={
                'ordering': ['created'],
                'indexes': [models.Index(fields=['created'], name='books_revie_created_a0b48c_idx')],
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='books.book')),
            ],
            options={
                'ordering': ['created'],
                'indexes': [models.Index(fields=['created'], name='books_quote_created_64dc5e_idx')],
            },
        ),
    ]