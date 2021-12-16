# the easiest solution

def plusOne(digits):
    tmp = [str(x) for x in digits]
    tmp = ''.join(tmp)
    tmp = int(tmp)
    tmp += 1
    tmp = str(tmp)
    tmp = list(tmp)
    tmp = [int(x) for x in tmp]
    return tmp

case1 = [1,2,9]
print('Expected output:', [1,3,0])
print('Actual output:', plusOne(case1))