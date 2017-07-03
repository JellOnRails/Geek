import collections

class Contact_list(object):
    def __init__(self):
        self.contacts = collections.defaultdict(int)
        
    def _add(self, name):
        self.contacts[name] += 1
        max = len(name)
        for i in range(1, max):
            self.contacts[name[:-1*i]] += 1            
            
    def _find(self, template):            
        return self.contacts[template]    

    def perform(self, op, name):
        if op == 'add':
            self._add(name)
        elif op == 'find':
            print self._find(name)
        else:
            print 'operation not found'

cbook = Contact_list() 
n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    cbook.perform(op, contact)
    