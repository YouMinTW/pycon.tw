# Generated by Django 3.0.3 on 2020-08-24 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ext2020', '0005_merge_20200824_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='address',
            field=models.CharField(blank=True, max_length=64, verbose_name='Venue Address'),
        ),
        migrations.AddField(
            model_name='venue',
            name='address_en_us',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Venue Address'),
        ),
        migrations.AddField(
            model_name='venue',
            name='address_zh_hant',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Venue Address'),
        ),
        migrations.AddField(
            model_name='venue',
            name='capacity',
            field=models.IntegerField(default=0, verbose_name='Capacity Limit'),
        ),
        migrations.AddField(
            model_name='venue',
            name='community',
            field=models.CharField(blank=True, max_length=64, verbose_name='Community'),
        ),
        migrations.AddField(
            model_name='venue',
            name='community_en_us',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Community'),
        ),
        migrations.AddField(
            model_name='venue',
            name='community_zh_hant',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Community'),
        ),
        migrations.AddField(
            model_name='venue',
            name='name_en_us',
            field=models.CharField(max_length=64, null=True, verbose_name='Venue Name'),
        ),
        migrations.AddField(
            model_name='venue',
            name='name_zh_hant',
            field=models.CharField(max_length=64, null=True, verbose_name='Venue Name'),
        ),
        migrations.AddField(
            model_name='venue',
            name='topic',
            field=models.CharField(blank=True, max_length=64, verbose_name='Topic'),
        ),
    ]