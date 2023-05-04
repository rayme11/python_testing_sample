import unittest

from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def test_lookup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add("Ray", "12345")
        number = phonebook.lookup("Ray")
        self.assertEqual("12345", number)
