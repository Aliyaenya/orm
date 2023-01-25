import peewee

db = peewee.PostgresqlDatabase(     
    'orm_py25',
    user = 'alia',
    password = '1',
    host='localhost',    # где находится - в локальном
    port=5432     # defoltный вход постгреса
)