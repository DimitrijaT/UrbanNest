# Generated by Django 4.2.3 on 2023-08-14 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Furniture', '0011_frontcover_rename_name_testimonials_nickname_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Testimonials',
            new_name='Testimonial',
        ),
    ]