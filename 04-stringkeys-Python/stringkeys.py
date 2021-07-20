"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        # Your code goes here
        #mohan = 13+15+8+1+14 = 51 , name = 14+1+13+5 = 33 , asia = 1+19+10+1 = 31
        #mohan = 110*100+112 = 11112, name = 111*100+97 = 11197 , 
        k = self.calculate_hash_value(string)
        self.table[k] = string
        
        
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # Your code goes here
        k = self.calculate_hash_value(string)
        if self.table[k] == None or self.table[k] != string:
            return -1
        else:
            return k


    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # Your code goes here
        HashValue = (ord(string[0]) * 100) + ord(string[1])
        
        return HashValue


