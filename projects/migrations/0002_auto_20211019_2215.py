# Generated by Django 3.2.6 on 2021-10-19 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='Database',
        ),
        migrations.RemoveField(
            model_name='project',
            name='Frontend_framwork',
        ),
        migrations.RemoveField(
            model_name='project',
            name='icon_source',
        ),
        migrations.AddField(
            model_name='project',
            name='Backend_framwork_icon',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='Deployed_to_icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='Port_routing_icon',
            field=models.CharField(blank=True, default='Gunicorn', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='css',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='css_icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='database',
            field=models.CharField(default='Postgres', max_length=30),
        ),
        migrations.AddField(
            model_name='project',
            name='database_icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='frontend_framwork',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='frontend_framwork_icon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='html',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='html_icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='js_icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='server_icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='staticfiles_handling_icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='vanilla_javascript',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='project',
            name='version_control_icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='Authentication_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='Backend_framwork',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='Deployed_to',
            field=models.CharField(blank=True, default='DigitalOcean', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='Port_routing',
            field=models.CharField(blank=True, default='Gunicorn', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='server',
            field=models.CharField(default='Ubuntu v18', max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='static_files_handling',
            field=models.CharField(blank=True, default='NGINX', max_length=50, null=True),
        ),
    ]
