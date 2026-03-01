import oracledb

connection=oracledb.connect(
        user="your_username",
        password="your_password",
        dsn="your_dsn"
    )


cursor=connection.cursor()
cursor.execute('SELECT t_id,t_ad,t_soyad FROM telebe')
rows=cursor.fetchall()
for row in rows:
    t_id=row[0]
    t_ad=row[1]
    t_soyad=row[2]
    cursor.execute(f'SELECT q_id FROM qiymet WHERE t_id={t_id}')
    row=cursor.fetchone()
    if row:
        q_id=row[0]
        if q_id > 60:
            print(f" ID: {t_id}, Ad: {t_ad}, Soyad: {t_soyad}, Bal: {q_id}")

cursor.close()
connection.close()
