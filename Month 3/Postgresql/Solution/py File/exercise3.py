import psycopg2

#1
try:
    conn = psycopg2.connect(dbname="exercise3",user="postgres",password="123",host="localhost",port="5432")
    print("Connection with database established successfully.")
except:
    print("Connection with database has not been established")

#2
try:
    cur = conn.cursor()
    print("\nCursor created successfully")
except:
    print("\nCursor has not been created")

#3
try:
    cur.execute("create table if not exists product(id serial primary key,name varchar,cost_price numeric,sale_price numeric)")
    conn.commit()
    print("\nProduct table created successfully")
except:
    print("\nProduct table has not been created")

#4
try:
    cur.execute("create table if not exists category(id serial primary key,code varchar unique,name varchar not null)")
    conn.commit()
    print("\nCategory table created successfully")
except:
    print("\nCategory table has not been created")

#5
try:
    cur.execute("alter table product add column category_id integer references category(id)")
    conn.commit()
    print("\nCategory ID column added to Product table successfully with foreign key constraint")
except:
    print("\nError occurred while adding Category ID column to Product table")

#6
try:
    categories = [
        ("C001", "Electronics"),
        ("C002", "Clothing"),
        ("C003", "Home Appliances"),
        ("C004", "Books"),
        ("C005", "Toys")
    ]

    cur.executemany("insert into category (code,name) values(%s,%s)",categories)
    conn.commit()
    print("\nData inserted to category table")

    products = [
        ("Smartphone", 399.99, 499.99, 1),
        ("Laptop", 799.99, 999.99, 2),
        ("Headphones", 49.99, 69.99, 3),
        ("Bluetooth Speaker", 29.99, 39.99, 4),
        ("Tablet", 299.99, 399.99, 5),
        ("Smartwatch", 199.99, 249.99, 1),
        ("Gaming Console", 299.99, 399.99, 2),
        ("Digital Camera", 249.99, 349.99, 3),
        ("Fitness Tracker", 79.99, 99.99, 4),
        ("Wireless Earbuds", 69.99, 89.99, 5),
        ("External Hard Drive", 79.99, 119.99, 1),
        ("Monitor", 149.99, 199.99, 2),
        ("Printer", 99.99, 149.99, 3),
        ("Keyboard", 29.99, 49.99, 4),
        ("Mouse", 19.99, 29.99, 5),
        ("Router", 59.99, 79.99, 1),
        ("Webcam", 39.99, 59.99, 2),
        ("Graphics Tablet", 149.99, 199.99, 3),
        ("Microphone", 49.99, 69.99, 4),
        ("Portable Charger", 19.99, 29.99, 5)
    ]

    cur.executemany("Insert into product(name,cost_price,sale_price,category_id) values(%s,%s,%s,%s)",products)
    conn.commit()
    print("\nData inserted to Product table")
except:
    print("\nRecords failed to be inserted")

#7
cur.execute("select * from product")
print("\n",cur.fetchall())

#8
cur.execute("select * from product limit 1")
print("\n",cur.fetchone())

#9
cur.execute("select * from product order by cost_price")
print("\n",cur.fetchall())

#10
cur.execute("select * from product order by sale_price desc limit 1")
print("\n",cur.fetchone())

#11
cur.execute("SELECT id FROM product LIMIT 3")
product_ids_to_update = cur.fetchall()
for product_id in product_ids_to_update:
    cur.execute("UPDATE product SET cost_price = cost_price + 5 WHERE id = %s", (product_id,))
print("\nRecord updted successfully")

#12
cur.execute("SELECT id FROM product LIMIT 2")
product_ids_to_update = cur.fetchall()
for product_id in product_ids_to_update:
    cur.execute("UPDATE product SET cost_price = cost_price + 10 WHERE id = %s", (product_id,))
print("\nRecord updted successfully")

#13
cur.execute("select * from product")
print("\n",cur.fetchall())

#14
cur.execute("SELECT p.id, p.name, p.cost_price, p.sale_price, c.code, c.name FROM product p JOIN category c ON p.category_id = c.id")
print(cur.fetchall())

#15
cur.close()
print("\nCursor closed successfully")

conn.close()
print("\nConnection closed successfully")