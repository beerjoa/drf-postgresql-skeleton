from django.db.models import Model, AutoField, DateTimeField


class Base(Model):
    id = AutoField(primary_key=True)
    update_date = DateTimeField(blank=True, null=True)
    delete_date = DateTimeField(blank=True, null=True)
    create_date = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
