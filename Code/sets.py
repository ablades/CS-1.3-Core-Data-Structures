#sets.py
from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        """ - initialize a new empty set structure, and add each element if a sequence is given"""
        
        if elements is not None:
            self.ht = HashTable(len(elements))

            for element in elements:
                self.add(element)

        else:
            self.ht = HashTable()

    def size(self):
        """ - property that tracks the number of elements in constant time"""
        return self.ht.size

    def contains(self, element):
        """ - return a boolean indicating whether element is in this set"""
        return self.ht.contains(element)

    def add(self, element):
        """ - add element to this set, if not present already"""
        #item already exists
        if self.ht.contains(element):
            return False
        else:
            self.ht.set(element, 1)
            return True

    def remove(self, element):
        """ - remove element from this set, if present, or else raise KeyError"""
        self.ht.delete(element)


    def union(self, other_set):
        """ - return a new set that is the union of this set and other_set"""
        new_set = Set()

        for item in self.ht.keys():
            new_set.add(item)
        
        for item in other_set.ht.keys():
            new_set.add(item)

        return new_set

    def intersection(self, other_set):
        """ - return a new set that is the intersection of this set and other_set"""
        new_set = Set()
        
        for item in self.ht.keys():
            if other_set.contains(item):
                new_set.add(item)
        
        for item in other_set.ht.keys():
            if self.contains(item):
                new_set.add(item)
  


    def difference(self, other_set):
        """ - return a new set that is the difference of this set and other_set"""
        pass
    def is_subset(self, other_set): 
        """return a boolean indicating whether other_set is a subset of this set"""