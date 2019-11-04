from django.db import models


class Workers(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    firstName = models.CharField(db_column='firstName', max_length=255)
    patronymic = models.CharField(db_column='patronymic', max_length=255)
    lastName = models.CharField(db_column='lastName', max_length=255)
    phone = models.CharField(db_column='phone', unique=True, max_length=11)

    class Meta:
        db_table = 'Workers'


class Tasks(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    idWorker = models.ForeignKey('Workers', models.DO_NOTHING, db_column='idWorker', null=False)
    taskName = models.CharField(db_column='name', max_length=255)
    description = models.CharField(db_column='description', max_length=255)
    deadline = models.DateTimeField(db_column='deadline')
    status = models.BooleanField(db_column='status', default=False)
    address = models.CharField(db_column='address', max_length=255)
    longitude = models.FloatField(db_column='longitude')
    latitude = models.FloatField(db_column='latitude')
    addDateTime = models.DateTimeField(db_column='addDateTime', auto_now_add=True)
    updateDateTime = models.DateTimeField(db_column='updateDateTime', auto_now=True)

    class Meta:
        db_table = 'Tasks'


class Files(models.Model):
    """
    database structure:
    id - SERIAL field, not null, primary key
    filename - char[255] or text field, not null
    file - bitea field
    """
    id = models.AutoField(db_column='id', primary_key=True)
    filename = models.CharField(db_column='filename', max_length=255, null=False)
    file = models.BinaryField(db_column='file')

    class Meta:
        db_table = 'Files'
