# Generated by Django 5.0.6 on 2024-07-10 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='comment',
            field=models.CharField(help_text='Type your feedback here...', max_length=255, verbose_name='Your Comment'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='signature',
            field=models.ImageField(help_text='Upload the author signature.', upload_to='feedbacks/signature/', verbose_name='Your Signature'),
        ),
    ]
