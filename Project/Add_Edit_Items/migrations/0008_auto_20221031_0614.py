# Generated by Django 3.1.2 on 2022-10-31 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Add_Edit_Items', '0007_remove_food_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
