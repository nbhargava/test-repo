from unittest import TestCase

from main.banana import Banana
from main.person import Person


class SimpleTest(TestCase):
    def test_eating(self):
        person = Person()
        for a in xrange(10):
            person.add_banana(Banana())
        self.assertEquals(person.total_bananas(), 10)
        person.eat_bananas()
        self.assertEquals(person.total_bananas(), 0)
