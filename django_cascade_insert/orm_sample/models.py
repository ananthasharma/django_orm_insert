from django.db import models

# Create your models here.

class GroupRegistry(models.Model):
    id = models.AutoField(primary_key=True, db_column="IO_GROUP_ID")
    name= models.CharField(db_column="IO_GROUP_NAME",max_length=100)
    class Meta:
        db_table = "IO_GROUP_REGISTRY"

class DataRegistry(models.Model):
    id = models.AutoField(primary_key=True, db_column="IO_DATA_ID")
    file_name = models.CharField(db_column="DATA_FILE_NAME",max_length=100)
    file_path = models.CharField(db_column="DATA_FILE_PATH",max_length=100)
    class Meta:
        db_table = "IO_DATA_REGISTRY"

class GroupDataRegistryMapper(models.Model):
    id = models.AutoField(primary_key=True, db_column="IO_DATA_ASSOC_ID")
    data_registry = models.ForeignKey(to=DataRegistry, on_delete=models.CASCADE,db_column="IO_DATA_ID")
    group_registry = models.ForeignKey(to=GroupRegistry, on_delete=models.CASCADE,db_column="IO_GROUP_ID")
    class Meta:
        db_table = "IO_GROUP_DATA_ASSOC"


