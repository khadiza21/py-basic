# global and local variable scope
# global scope
#  global keyword is not referable for use  in normal case. IN special case we can use
balance = 345
remaining = 10
def total_cost (price, quantity):
    global remaining # set global variable's new value inside function ()
    vat = 45  #local
    cost = (price+vat )*quantity 
    remaining = balance-  cost 
    print('remaining ',remaining)
    return cost 
pay = total_cost(10,2)
print(f'please pay: {pay}')
print('remaining ',remaining)



