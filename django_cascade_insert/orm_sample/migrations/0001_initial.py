# Generated by Django 2.2.7 on 2019-11-12 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataRegistry',
            fields=[
                ('id', models.AutoField(db_column='IO_DATA_ID', primary_key=True, serialize=False)),
                ('file_name', models.CharField(db_column='DATA_FILE_NAME', max_length=100)),
                ('file_path', models.CharField(db_column='DATA_FILE_PATH', max_length=100)),
            ],
            options={
                'db_table': 'IO_DATA_REGISTRY',
            },
        ),
        migrations.CreateModel(
            name='GroupRegistry',
            fields=[
                ('id', models.AutoField(db_column='IO_GROUP_ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='IO_GROUP_NAME', max_length=100)),
            ],
            options={
                'db_table': 'IO_GROUP_REGISTRY',
            },
        ),
        migrations.CreateModel(
            name='GroupDataRegistryMapper',
            fields=[
                ('id', models.AutoField(db_column='IO_DATA_ASSOC_ID', primary_key=True, serialize=False)),
                ('data_registry', models.ForeignKey(db_column='IO_DATA_ID', on_delete=None, to='orm_sample.DataRegistry')),
                ('group_registry', models.ForeignKey(db_column='IO_GROUP_ID', on_delete=None, to='orm_sample.GroupRegistry')),
            ],
            options={
                'db_table': 'IO_GROUP_DATA_ASSOC',
            },
        ),
    ]