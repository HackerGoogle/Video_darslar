# Generated by Django 5.0.3 on 2024-03-22 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_dars_app', '0004_alter_card_title_alter_mavzu_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(default=1, upload_to='video/image/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='mavzu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videolar', to='video_dars_app.mavzu'),
        ),
    ]