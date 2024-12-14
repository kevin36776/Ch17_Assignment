import sqlite3

# Connect to the database
connection = sqlite3.connect('books.db')

# Create a cursor
cursor = connection.cursor()

# 1. Display all the titles
print("All Titles in the Database:")
cursor.execute("SELECT title FROM titles")
for row in cursor.fetchall():
    print(row[0])

print("\n")

# 2. List the titles
print("Titles Sorted in Ascending Order:")
cursor.execute("SELECT title FROM titles ORDER BY title ASC")
for row in cursor.fetchall():
    print(row[0])

print("\n")

# 3. Show the authors of each book with their titles
print("Authors and Their Books:")
cursor.execute("""
    SELECT authors.first || ' ' || authors.last AS author_name, titles.title 
    FROM authors 
    JOIN author_ISBN ON authors.id = author_ISBN.id
    JOIN titles ON author_ISBN.isbn = titles.isbn
""")
for row in cursor.fetchall():
    print(f"Author: {row[0]}, Title: {row[1]}")

print("\n")

# 4. Count the number of books for each author
print("Number of Books per Author:")
cursor.execute("""
    SELECT authors.first || ' ' || authors.last AS author_name, COUNT(titles.isbn) AS book_count
    FROM authors
    JOIN author_ISBN ON authors.id = author_ISBN.id
    JOIN titles ON author_ISBN.isbn = titles.isbn
    GROUP BY authors.id
""")
for row in cursor.fetchall():
    print(f"Author: {row[0]}, Number of Books: {row[1]}")

# Close the connection
connection.close()
