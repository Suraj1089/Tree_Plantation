# Generated by Django 4.0.4 on 2022-05-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPageContent', '0002_alter_homecontent_slider_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecontent',
            name='slider_images',
            field=models.ImageField(upload_to='static/slider_images/ %Y / %m / %d/'),
        ),
        migrations.AlterField(
            model_name='homecontent',
            name='tree_plantation_map_image',
            field=models.ImageField(upload_to='static/slider_images/ %Y / %m / %d/'),
        ),
        migrations.AlterField(
            model_name='homepagetrees',
            name='tree_image',
            field=models.ImageField(upload_to='static/homepageTrees/ %Y / %m / %d/'),
        ),
    ]
