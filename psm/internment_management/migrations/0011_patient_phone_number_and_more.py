# Generated by Django 4.0.3 on 2022-04-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internment_management', '0010_alter_internmentstatus_next_states_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(default=12345, max_length=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carehouseinternment',
            name='admission_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]