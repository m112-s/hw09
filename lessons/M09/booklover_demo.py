from booklover import BookLover

# Create a BookLover object
book_lover = BookLover(name="Manav", email="manav@gmail.com", fav_genre="Fiction")

# Add some books to the book lover's list
book_lover.add_book("Dune", 5)
book_lover.add_book("Dune 2", 4)
book_lover.add_book("Dune 3", 1)

# Print the number of books read
print("Number of Books: ",book_lover.num_books_read())

# Print the favorite books
print("Favorite Books: ", book_lover.fav_books())

