import peewee
from models import Category, Product

def post_category(category_name):
    try:
        category = Category(name=category_name)
        category.save()
        print('Saved!!!')
    except peewee.IntegrityError:
        print('Такая категория уже существует')


def get_categories():
    categories = Category.select()
    # print(list(categories))   #[<Category: 1>, <Category: 3>]
    for category in categories:
        print(f'{category.id} -- {category.name} -- {category.created_at}')   #выводит все содержимое категории 
        
    # print(categories)  #SELECT "t1"."id", "t1"."name", "t1"."created_at" FROM "category" AS "t1"   - выводит sql запрос


def delete_category(category_id):
    try:
        category = Category.get(id=category_id)  #метод гет выводит только один объект со значением, если больше выведет ошибку
        category.delete_instance()
        print('Deleted!!!')
    except peewee.DoesNotExist:
        print('Категория не найдена ')


def update_category(category_id, new_name):  #обновление, изменение нового имени
    try:
        category = Category.get(id=category_id)  #метод гет выводит только один объект со значением, если больше выведет ошибку
        category.name = new_name
        category.save()        #сохраняем в базу данных
        print('Обновили!!!!!')
    except peewee.DoesNotExist:
        print('Категория не найдена ')


def detail_category(id_category):
    try:
        category = Category.get(id=id_category)
        print(category.id, end='\t')
        print(category.name, end='\t')
        print(category.created_at)
        # print(category.products)    #SELECT "t1"."id", "t1"."name", "t1"."price", "t1"."amount", "t1"."category_id" FROM "product" AS "t1" WHERE ("t1"."category_id" = 3)
        for i in category.products:      #[p1, p2, p1, p2, p1]
            print(f'{i.name} -- {i.price} -- {i.amount}')
    except peewee.DoesNotExist:
        print('Нет такой категории')


def post_product(name, price, amount, category):
    try:
        product = Product(name=name, price=price, amount=amount, category=category)
        product.save()
    except peewee.IntegrityError:
        print('такой категории не существует')


def get_products():
    products = Product.select()
    for i in products:
        print(f'{i.name} -- {i.price} -- {i.amount} -- {i.category.name} -- {i.category.id}')

# get_products() 


def get_products_by_name(name):
    products = Product.select().where(Product.name==name) #select * from product where name='product';
    for i in products:
        print(i.name, i.price)

# get_products_by_name('product')