"""
ORM (Object Relational Mapping - объектно реляционное отображение) - технология которая связывает БД с концепциями объектно ориентированных языков программирования. ORM - прослойка между БД и кодом который пишет программист, которая позволяет создавать в программе объекты обновлять, удалять и получать их


python:
    peewee
    sqlalchemy
    DjangoORM


класс - таблица в БД
атрибут класса - поле в БД
обЪект класса - строка в таблице
"""
# объект(db) от класса (PostgresqlDatabase) - настройка соединения субд к файлу  - настроки подключения orm
# db = peewee.PostgresqlDatabase  - одно и то же  db = PostgresqlDatabase
# category.save()   #чтобы записалось в базу данных





from views import *
from settings import db

db.connect()

get_categories()
get_products()

db.close()