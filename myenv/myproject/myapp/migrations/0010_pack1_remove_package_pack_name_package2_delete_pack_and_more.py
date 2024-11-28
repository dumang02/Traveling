# Generated by Django 5.0.6 on 2024-05-27 05:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_pack_pack_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='pack1',
            fields=[
                ('pack_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='package',
            name='pack_name',
        ),
        migrations.CreateModel(
            name='package2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pic', models.ImageField(upload_to='media/')),
                ('place', models.CharField(max_length=30)),
                ('days', models.IntegerField()),
                ('person', models.IntegerField()),
                ('explor', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.pack1')),
            ],
        ),
        migrations.DeleteModel(
            name='pack',
        ),
        migrations.DeleteModel(
            name='package',
        ),
    ]
