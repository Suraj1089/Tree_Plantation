# Generated by Django 4.0.4 on 2022-06-01 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPageContent', '0005_alter_homecontent_tree_plantation_map_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecontent',
            name='slider_images',
            field=models.ImageField(upload_to='media/sliderImages/ %Y/ %m/ %d/'),
        ),
        migrations.AlterField(
            model_name='homecontent',
            name='tree_plantation_map_image',
            field=models.ImageField(upload_to='media/sliderImages/ %Y/ %m/ %d/'),
        ),
        migrations.AlterField(
            model_name='homepagetrees',
            name='tree_image',
            field=models.ImageField(upload_to='media/treePlantedImages/ %Y/ %m/ %d/'),
        ),
    ]
