# Generated by Django 5.1.2 on 2024-11-04 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UDVogueApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='editorial',
            name='revistas_publicadas',
        ),
        migrations.AddField(
            model_name='producto',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revistas', to='UDVogueApp.revista'),
        ),
        migrations.AddField(
            model_name='revista',
            name='editorial',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='editoriales', to='UDVogueApp.editorial'),
        ),
    ]