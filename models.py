import peewee
from datetime import datetime
from settings import db


class Category(peewee.Model):  #он рассматривает класс как табличку бд
    id = peewee.PrimaryKeyField()
    name = peewee.CharField(max_length=100, unique=True)
    created_at = peewee.DateTimeField(default=datetime.now())

    class Meta:    #настройки для класса он взаимодействует с PostgresqlDatabase
        database = db
        db_table = 'category'


class Product(peewee.Model):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField(max_length=100)
    price = peewee.DecimalField(max_digits=10, decimal_places=2, default=10)
    amount = peewee.IntegerField(null=False)
    category = peewee.ForeignKeyField(Category, related_name='products', to_field='id', on_delete='cascade')
    # category_id int references Category(id)
    # related_name='products', - для обратной связи

    class Meta:    #настройки для класса он взаимодействует с PostgresqlDatabase
        database = db
        db_table = 'product'


