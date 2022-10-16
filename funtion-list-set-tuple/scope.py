# global and local variable scope
# global scope
balance = 345
remaining = 10
def total_cost (price, quantity):
    global remaining # set global variable's new value inside function ()
    vat = 45  #local
    cost = (price+vat )*quantity 
    remaining = balance-  cost 
    print('remainging ',remaining)
    return cost 
pay = total_cost(10,2)
print(f'please pay: {pay}')
print('remainging ',remaining)



