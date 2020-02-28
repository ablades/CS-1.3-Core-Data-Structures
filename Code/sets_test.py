from sets import Set
import unittest


class SetTest(unittest.TestCase):

    def test_init(self):
        elements = ['A','B','C','D']
        s = Set(elements)
        assert s.ht.length() == 4
        assert s.size() == 4

    def test_add(self):
        s = Set()
        #Add elements to set
        assert s.add('A') == True
        assert s.add('B') == True
        assert s.add('C') == True
        #Test size after duplicates
        assert s.size() == 3

        #add duplicate element to set
        assert s.add('C') == False
        assert s.add('B') == False
        assert s.add('A') == False   

        #Test size after duplicates
        assert s.size() == 3

    def test_remove(self):
        s = Set()
        s.add('A')
        s.add('B')
        s.add('C')

        #Verify removals by asserting size
        s.remove('C')
        assert s.size() == 2

        s.remove('B')
        assert s.size() == 1

        s.remove('A')
        assert s.size() == 0

        #Test remove with no element
        with self.assertRaises(KeyError):
            s.remove('A')

    def test_contains(self):
        s = Set()

        s.add('A')
        assert s.contains('A') == True
        assert s.contains('B') == False

        s.add('B')
        assert s.contains('B') == True
        assert s.contains('A') == True

    def test_union(self):
        s1 = Set(['A', 'B', 'C', 'D'])
        s2 = Set(['E', 'F', 'G', 'H'])
        s3 = s1.union(s2)
        assert s3.contains('A') == True
        assert s3.contains('B') == True
        assert s3.contains('C') == True
        assert s3.contains('D') == True
        assert s3.contains('E') == True
        assert s3.contains('F') == True
        assert s3.contains('G') == True
        assert s3.contains('H') == True
        assert s3.size() == 8

    def test_intersection(self):
        s1 = Set(['A', 'B', 'C', 'D'])
        s2 = Set(['C', 'D', 'G', 'H'])
        s3 = s1.intersection(s2)
        assert s3.contains('D') == True
        assert s3.contains('C') == True
        assert s3.size() == 2

    def test_difference(self):
        s1 = Set(['A', 'B', 'C', 'D'])
        s2 = Set(['C', 'D', 'G', 'H'])
        s3 = s1.difference(s2)
        assert s3.contains('A') == True
        assert s3.contains('B') == True
        assert s3.contains('G') == True
        assert s3.contains('H') == True
        assert s3.size() == 4

    def test_is_subset(self):
        s1 = Set(['A', 'B', 'C', 'D'])
        s2 = Set(['C', 'D'])
        s3 = Set(['A', 'B'])
        s4 = Set(['E', 'F'])

        assert s1.is_subset(s2) == True
        assert s1.is_subset(s3) == True
        assert s1.is_subset(s4) == False
        

if __name__ == '__main__':
    unittest.main()


