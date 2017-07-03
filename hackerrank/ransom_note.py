import collections

def ransom_note(magazine, ransom):
    base = collections.defaultdict(int)
    for word in magazine:
        base[word] += 1
    
    for word in ransom:
        value = base.get(word)
        if value is None or value < 1:
            return False
        else:
            base[word] -= 1
    return True
            

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    