# Generated by Django 3.2.6 on 2021-11-03 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_other_features'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='Authentication_type',
            new_name='authentication_type',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Backend_framwork',
            new_name='backend_framwork',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Backend_framwork_icon',
            new_name='backend_framwork_icon',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Deployed_to',
            new_name='deployed_to',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Deployed_to_icon',
            new_name='deployed_to_icon',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Port_routing',
            new_name='port_routing',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Port_routing_icon',
            new_name='port_routing_icon',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Version_control',
            new_name='version_control',
        ),
    ]
