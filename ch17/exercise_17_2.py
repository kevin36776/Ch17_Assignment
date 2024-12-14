import sqlite3
import pandas as pd

# Step 1: Connect to the database
connection = sqlite3.connect('books.db')

# Step 2: Create a cursor object
cursor = connection.cursor()

# Step 3: Example SQL Queries
# Viewing the authors table
authors_query = "SELECT * FROM authors"
authors_df = pd.read_sql(authors_query, connection)
print("Authors Table:")
print(authors_df)

# Viewing the titles table
titles_query = "SELECT * FROM titles"
titles_df = pd.read_sql(titles_query, connection)
print("\nTitles Table:")
print(titles_df)

# Adding a new author
new_author = """INSERT INTO authors (first, last) VALUES ('John', 'Doe')"""
cursor.execute(new_author)
connection.commit()

# Viewing the updated authors table
updated_authors_df = pd.read_sql(authors_query, connection)
print("\nUpdated Authors Table:")
print(updated_authors_df)

# Updating an author's name
update_query = """UPDATE authors SET last='Smith' WHERE last='Doe'"""
cursor.execute(update_query)
connection.commit()

# Viewing the updated authors table again
updated_authors_df = pd.read_sql(authors_query, connection)
print("\nAuthors Table After Update:")
print(updated_authors_df)

# Deleting the newly added author
delete_query = """DELETE FROM authors WHERE last='Smith'"""
cursor.execute(delete_query)
connection.commit()

# Viewing the authors table after deletion
final_authors_df = pd.read_sql(authors_query, connection)
print("\nAuthors Table After Deletion:")
print(final_authors_df)

# Selecting specific columns
selected_columns_query = "SELECT title, edition FROM titles"
selected_columns_df = pd.read_sql(selected_columns_query, connection)
print("\nSelected Columns from Titles Table:")
print(selected_columns_df)

# Sorting the titles by edition
sorted_titles_query = "SELECT title, edition FROM titles ORDER BY edition DESC"
sorted_titles_df = pd.read_sql(sorted_titles_query, connection)
print("\nTitles Table Sorted by Edition (Descending):")
print(sorted_titles_df)

# Closing the connection
connection.close()
