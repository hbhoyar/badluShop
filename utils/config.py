from cs387.settings import DATABASES

data = DATABASES['default']

config = {
    'dbname': data.get('NAME'),
    'user': data.get('USER'),
    'password': data.get('PASSWORD'),
    'host': data.get('HOST'),
    'port': data.get('PORT')
}

conn_string = """dbname=gl1_generation user=hbhoyar password="" host=localhost """

