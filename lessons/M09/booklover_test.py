import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def setUp(self):
        self.booklover = BookLover("manav", "manav@gmail.com", "Sports")
        
    def test_1_add_book(self): 
        self.booklover.add_book("Percy Jackson", 2)
        self.assertTrue(self.booklover.has_read("Percy Jackson"))

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        self.booklover.add_book("Percy Jackson", 2)
        self.booklover.add_book("Percy Jackson", 2) 
        self.assertEqual(len(self.booklover.book_list), 1)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        self.booklover.add_book("Percy Jackson", 2)
        self.assertTrue(self.booklover.has_read("Percy Jackson"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        self.assertFalse(self.booklover.has_read("Percy Jackson Part 2"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        self.booklover.add_book("Percy Jackson", 2)
        self.booklover.add_book("Tale of Two Cities", 1)
        self.booklover.add_book("Eragon", 5)
        self.booklover.add_book("Life of Pi", 4)
        self.booklover.add_book("A new book", 1)
        self.booklover.add_book("A bad book", 1)
        self.booklover.add_book("An ok book", 3)
        
        assert self.booklover.num_books_read() == 7

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        self.booklover.add_book("Percy Jackson", 2)
        self.booklover.add_book("Tale of Two Cities", 1)
        self.booklover.add_book("Eragon", 5)
        self.booklover.add_book("Life of Pi", 4)
        
        fav_books = self.booklover.fav_books()
        self.assertEqual(len(fav_books), 2) 
        self.assertTrue((fav_books['book_rating'] > 3).all())
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)