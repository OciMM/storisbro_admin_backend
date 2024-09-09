# Generated by Django 4.2.9 on 2024-02-10 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_users', models.IntegerField(default=0)),
                ('unique_visits', models.IntegerField(default=0)),
                ('refills', models.IntegerField(default=0)),
                ('total_revenue', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('admin_earnings', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('creative_uploads', models.IntegerField(default=0)),
                ('community_uploads', models.IntegerField(default=0)),
                ('story_views', models.IntegerField(default=0)),
            ],
        ),
    ]
