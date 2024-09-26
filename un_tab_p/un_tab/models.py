from django.db import models


class UnmanagedTable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "unmanaged_table"
