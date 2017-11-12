import pdb

def test(a, b):
    return a + b

a = 'aaa'
pdb.set_trace()
b = 'bbb'
c = 'ccc'
final = a + b + c
print('Final: ', final)
sum = test(1, 2)
print('Sum: ', sum)
