# Generated by Django 3.2.16 on 2023-01-23 14:56

from django.db import migrations, models
import senhas.validations


class Migration(migrations.Migration):

    dependencies = [
        ('senhas', '0029_auto_20220823_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='contato_responsavel',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='dt_Chegada',
            field=models.DateField(validators=[senhas.validations.validate_data], verbose_name='Data Chegada'),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='dt_Saida',
            field=models.DateField(blank=True, null=True, validators=[senhas.validations.validate_data], verbose_name='Data Saída'),
        ),
        migrations.AlterField(
            model_name='viagem_turismo',
            name='celular',
            field=models.CharField(max_length=15, validators=[senhas.validations.validate_celular]),
        ),
        migrations.AlterField(
            model_name='viagem_turismo',
            name='telefone',
            field=models.CharField(blank=True, max_length=14, null=True, validators=[senhas.validations.validate_telefone]),
        ),
    ]
