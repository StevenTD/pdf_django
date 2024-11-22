# Generated by Django 5.1.3 on 2024-11-22 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=128)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('G', 'Generating'), ('R', 'Ready'), ('E', 'Error')], default='P', max_length=2)),
                ('error_msg', models.CharField(blank=True, max_length=128, null=True)),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='$/home/steve/projects/personal/pdf_django/pdf_django_proj/media/pdfs/')),
            ],
        ),
    ]
