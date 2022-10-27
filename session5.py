products = []
orders = []
profit = 0

def inputProduct():
        product = {}
        product['name'] = input('Input Product Name: ')
        product['price'] = int(input('Input Product Price: '))
        product['stock'] = int(input('Input Product Stock: '))

        #add Product to Products variable
        products.append(product)

def showProducts():
    if(len(products) == 0):
        print('the Products is Empty')
        print('-------------')
        
    for index, product in enumerate(products):
        print('Product no: ', index + 1)
        print('Name: ',product['name'])
        print('price: ',product['price'])
        print('stock: ',product['stock'])
        print('-------------')

def inputOrder():

    showProducts()

    order = ()
    indexProduct = int(input('Select Product: '))
    orderQty = int(input('Select Qty: '))
    orderProduct = products[indexProduct]

    orderPrice = orderProduct['price'] * orderQty

    products[indexProduct]['stock'] = products[indexProduct]['stock'] - orderQty

    profit = orderPrice + (orderPrice * (10/100))

    print('Total is:', profit)

while(True):

    print('1. Show Product: ')
    print('2. Input Product: ')
    print('3. Input Order: ')
    print('4. Show Profit: ')
    print('0. Exit Program: ')

    menu = input('Menu: ')
    print('-------------')

    if(menu == '1'):
        showProducts()
        
    if(menu == '2'):
        inputProduct()

    if(menu == '3'):
        inputOrder()

    if(menu == '4'):
        print('the Profit is: ', profit)

    if(menu == '0'):
        break


print(products)