#sets.py
from hashtable import HashTable

class Set(object):
    def __init__(elements=None):
        """ - initialize a new empty set structure, and add each element if a sequence is given"""
        if elements is not None:
            self.ht = HashTable(len(elements))

            for element in elements:
                self.add(element)

    def size():
        """ - property that tracks the number of elements in constant time"""
        return self.ht.size()

    def contains(element):
        """ - return a boolean indicating whether element is in this set"""
        return self.ht.contains(element)

    def add(element):
        """ - add element to this set, if not present already"""
        #item already exists
        if self.ht.contains(element):
            return
        else:
            self.set(element)

    def remove(element):
        """ - remove element from this set, if present, or else raise KeyError"""
        self.ht.delete(element)



    def union(other_set):
        """ - return a new set that is the union of this set and other_set"""
        pass
    def intersection(other_set):
        """ - return a new set that is the intersection of this set and other_set"""
        pass
    def difference(other_set):
        """ - return a new set that is the difference of this set and other_set"""
        pass
    def is_subset(other_set): 
        """return a boolean indicating whether other_set is a subset of this set"""