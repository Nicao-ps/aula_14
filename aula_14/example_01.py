from sqlalchemy import create_engine, text

host = 'localhost'
user = 'root'
password = ''
database = 'analysis_bd'


def conect_bd():
    try:
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
        with engine.connect() as conection:
            query = 'SELECT * FROM vendas2'
            result = conection.execute(text(query))
            if result.rowcount > 0:
                for item in result:
                    print(item[0], item[1], item[2])
    except Exception as e:
        print(f'Something goes wrong. {e}')


conect_bd()