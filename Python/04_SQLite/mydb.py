import sqlite3
import csv
from myProducts import Products

# CREATE db at main dir
# connection = sqlite3.connect('product.db')
# cursor = connection.cursor()

# RUNNING IN MEMORY (TESTING)
connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

# CREATING THE TABLES

cursor.execute("""CREATE TABLE products (
               name text,
               category text,
               value real
               )""")


# FUNCTIONS
def insert_from_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            item = Products(row[0], row[1], row[2])
            insert_product(item)


def insert_product(product):
    with connection:
        cursor.execute("INSERT INTO products VALUES (:name, :category, :value)",
        {'name': product.name, 'category': product.category, 'value': product.value})


def update_value(product, value):
    with connection:
        cursor.execute("UPDATE products SET value= :value WHERE name = :name",
                       {'name': product.name, 'value': value})


def remove_product(product):
    with connection:
        cursor.execute("DELETE from products WHERE name = :name",
                       {'name': product.name})


def get_product_by_name(name):
    with connection:
        cursor.execute("SELECT name, category, value FROM products WHERE name=:name",
        {'name': name})
        return cursor.fetchall()


def get_all():
    with connection:
        cursor.execute("SELECT * FROM products")
        return cursor.fetchall()


def get_value_by_category():
    with connection:
        cursor.execute("SELECT category, SUM(value) FROM products GROUP BY category")
        return cursor.fetchall()

def get_count_of_items_by_category():
    with connection:
        cursor.execute("SELECT category, COUNT(name) FROM products GROUP BY category")
        return cursor.fetchall()


# INSERTING VALUES WITH METHODS

item1 = Products('Dress', "clothes", 40)
item2 = Products('Banana', "food", 1)

insert_product(item1)
insert_product(item2)

insert_from_csv('product.csv')

print(get_all())

print(get_product_by_name('apple'))

print(get_value_by_category())
print(get_count_of_items_by_category())

# INSERTING FROM THE CLASS
# cursor.execute("INSERT INTO products VALUES (?, ?, ?)", (item1.name, item1.category, item1.value))
# cursor.execute("INSERT INTO products VALUES (?, ?, ?)", (item2.name, item2.category, item2.value))

# INSERTING VALUES HARDCODE

# cursor.execute("INSERT INTO products VALUES ('hammer', 'tools', '15')")
# cursor.execute("INSERT INTO products VALUES ('screw', 'tools', '10')")
# cursor.execute("INSERT INTO products VALUES ('shirt', 'clothes', '20')")
# cursor.execute("INSERT INTO products VALUES ('pants', 'clothes', '50')")
# cursor.execute("INSERT INTO products VALUES ('drill', 'tools', '80')")


# SELECTING VALUES

# cursor.execute("SELECT category, sum(value) FROM products GROUP BY category")
# print(cursor.fetchall())

# print('Tools: ')
# cursor.execute("SELECT name, value FROM products WHERE category=:category", {'category': 'tools'})
# print(cursor.fetchall())


# commit and close
# connection.commit()
connection.close()