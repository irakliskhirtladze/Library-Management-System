# Generated by Django 5.0.4 on 2024-05-23 19:01

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_borrow_due_date_alter_reservation_expires_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterModelOptions(
            name='borrow',
            options={'verbose_name': 'Borrow', 'verbose_name_plural': 'Borrows'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Genre', 'verbose_name_plural': 'Genres'},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name': 'Reservation', 'verbose_name_plural': 'Reservations'},
        ),
        migrations.AddField(
            model_name='book',
            name='wished_by',
            field=models.ManyToManyField(blank=True, related_name='wished_books', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.CharField(max_length=100, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.author', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.genre', verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='book',
            name='release_year',
            field=models.IntegerField(verbose_name='Release Year'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book', verbose_name='Book'),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='borrowed_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Borrowed At'),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 6, 19, 1, 31, 444647, tzinfo=datetime.timezone.utc), verbose_name='Due Date'),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='returned_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Returned At'),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book', verbose_name='Book'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 24, 19, 1, 31, 444647, tzinfo=datetime.timezone.utc), verbose_name='Expires At'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is Active'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reserved_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Reserved At'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]