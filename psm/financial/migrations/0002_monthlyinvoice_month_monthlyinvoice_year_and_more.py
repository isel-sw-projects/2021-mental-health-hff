# Generated by Django 4.0.3 on 2022-05-22 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlyinvoice',
            name='month',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Janeiro'), (2, 'Fevereiro'), (3, 'Março'), (4, 'Abril'), (5, 'Maio'), (6, 'Junho'), (7, 'Julho'), (8, 'Agosto'), (9, 'Setembro'), (10, 'Outubro'), (11, 'Novembro'), (12, 'Dezembro')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monthlyinvoice',
            name='year',
            field=models.PositiveSmallIntegerField(default=2022),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='monthlyinvoice',
            name='status',
            field=models.CharField(choices=[('temp', 'Dados Temporários'), ('awaits_payment', 'Aguarda Pagamento'), ('paid', 'Pago'), ('rejected', 'Reprovado')], max_length=15),
        ),
    ]
