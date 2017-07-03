print 'hi!'

str = raw_input('write a string: ')
count = len(str)

ch_count = {}
odd_ch = 0
for ch in str:

  if ch in ch_count:
    ch_count[ch] += 1

    if ch_count[ch] % 2 == 0:
      odd_ch -= 1
    else: 
      odd_ch += 1

  else:
    ch_count[ch] = 1
    odd_ch += 1 

res = False
cond_1 = (odd_ch <= 1)
cond_2 = ((odd_ch + len(str)) % 2 == 0)
if cond_1 and cond_2:
  res = True

print 'length: %s' % count
print 'string: %s' % str

print '\n Palindrome: %s \n' % res
