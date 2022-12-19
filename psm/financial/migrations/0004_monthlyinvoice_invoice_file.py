# Generated by Django 4.0.3 on 2022-05-24 20:34

from django.db import migrations, models
import financial.utils.invoice_files_path


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0003_dailyvalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlyinvoice',
            name='invoice_file',
            field=models.FileField(blank=True, null=True, upload_to=financial.utils.invoice_files_path.invoice_files_path),
        ),
    ]
