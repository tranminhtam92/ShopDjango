from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 50)
    age = models.IntegerField()

class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length = 50)
    description = models.TextField()
    address = models.CharField(max_length = 60)
    picture = models.CharField(max_length = 60)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.IntegerField()
    id_shop = models.IntegerField()
    time = models.DateTimeField('date published')
    content = models.TextField()


class Subcoment(models.Model):
    id = models.AutoField(primary_key=True)
    id_comment = models.IntegerField()
    time = models.DateTimeField('date published')
    content = models.TextField()

class Evaluate(models.Model):
    id = models.AutoField(primary_key=True)
    evaluate_price = models.IntegerField(choices=((1, "thap"),
                                                    (2, "nomal"),
                                                    (3, "cao")),
                                                default=2)

    evaluate_quality = models.IntegerField(choices=((1, "thap"),
                                                    (2, "binh thuong"),
                                                    (3, "cao")),
                                                default=2)
    service_attitude = models.IntegerField(choices=((1, "kem"),
                                                    (2, "tam duoc"),
                                                    (3, "tot")),
                                                default=2)

    security = models.IntegerField(choices=((1, "kem"),
                                            (2, "tam duoc"),
                                            (3, "tot")),
                                            default=2)
    id_user = models.IntegerField()
    id_shop = models.IntegerField()
