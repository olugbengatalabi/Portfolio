# Generated by Django 3.2.6 on 2021-11-03 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_github_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='other_features',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]