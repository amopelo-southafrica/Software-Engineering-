#Name 4 items in the cafe 
stock_items = ['Coffee','Latte','Donut','Cupcake']
#Give each item quantaties 
stock_value ={'Coffee':5,
              'Latte':10,
              'Donut':20,
              'Cupcake':30,}
quantaties= stock_value.values()
print(quantaties)
#Give each item a price
stock_price = {'Coffee':20,
               'Latte':25,
               'Donut':5,
               'Cupcake':8,}
price= stock_price.values()
print(price)
#Give the total stock worth 
worth = 0
for item  in stock_items:
    total_value= stock_value[item]*stock_price[item]
    worth +=total_value
   
#Total worth
print(f'The stock worth is: R{worth}')