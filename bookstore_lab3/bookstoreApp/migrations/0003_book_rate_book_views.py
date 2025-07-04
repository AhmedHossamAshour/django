# Generated by Django 5.2.3 on 2025-06-17 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstoreApp', '0002_alter_book_added_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rate',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
        migrations.AddField(
            model_name='book',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
