# Generated by Django 2.2.1 on 2019-05-13 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemId', models.AutoField(primary_key=True, serialize=False)),
                ('itemName', models.CharField(max_length=512)),
                ('itemDescription', models.TextField(null=True)),
                ('itemPrice', models.FloatField(null=True)),
                ('itemQuantity', models.IntegerField(null=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('createdDate', models.DateTimeField(editable=False)),
                ('lastModifiedDate', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'item',
            },
        ),
    ]
