# Generated by Django 3.0.4 on 2020-03-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_for_hire', '0008_auto_20200324_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_chats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100)),
                ('seller_id', models.CharField(max_length=100)),
                ('buyer_id', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=2000)),
            ],
        ),
    ]