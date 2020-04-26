import sqlalchemy as sql

#docker run --name some-postgres -p 5432:5432  -e POSTGRES_PASSWORD=mysecretpassword --rm  postgres

#dialect+driver://username:password@host:port/database
engine = sql.create_engine('postgres://postgres:mysecretpassword@0.0.0.0:5432/postgres', echo=False)

metadata = sql.MetaData()
users = sql.Table('users', metadata,
     sql.Column('id', sql.Integer, primary_key=True),
     sql.Column('name', sql.String),
     sql.Column('fullname', sql.String)
)

addresses = sql.Table('addresses', metadata,
    sql.Column('id', sql.Integer, primary_key=True),
    sql.Column('user_id', None, sql.ForeignKey('users.id')),
    sql.Column('email_address', sql.String, nullable=False)
)

metadata.create_all(engine)

ins = users.insert().values(name='jack', fullname='Jack Jones')
conn = engine.connect()
conn.execute(ins)
ins = users.insert()
conn.execute(ins, name='wendy', fullname='Wendy Williams')
conn.execute(addresses.insert(), [
    {'user_id': 1, 'email_address' : 'jack@yahoo.com'},
    {'user_id': 1, 'email_address' : 'jack@msn.com'},
    {'user_id': 2, 'email_address' : 'www@www.org'},
    {'user_id': 2, 'email_address' : 'wendy@aol.com'}
])

s = sql.select([users])
result = conn.execute(s)
for row in result:
    print(row)

result2 = conn.execute(sql.select([addresses]))
for row in result2:
    print(row)
