import serilog

print('Posting data from python')
try:
    serilog.information('trying to divide by zero')
    a = 1/0
except Exception as err:
    print(err)
    print(err.args)
    serilog.error(err, 'post from python')

print('Data posted')
