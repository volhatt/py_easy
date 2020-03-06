from parse import parse

LOG = '[2018-05-06T12:58:00.714611] - SALE - PRODUCT: 1345 - PRICE: $09.99'
FORMAT = '[{date}] - SALE - PRODUCT: {product} - PRICE: ${price}'

# Run parse and check the results:
result = parse(FORMAT, LOG)
# OUTPUT
# <Result () {'date': '2018-05-06T12:58:00.714611', 'product': '1345', 'price': '09.99'}>

# The results are all strings. Define the types to be parsed:
FORMAT = '[{date:ti}] - SALE - PRODUCT: {product:d} - PRICE: ${price:05.2f}'
result = parse(FORMAT, LOG)
# OUTPUT
# <Result () {'date': datetime.datetime(2018, 5, 6, 12, 58, 0, 714611), 'product': 1345, 'price': 9.99}>

# Define a custom type for the price to avoid issues with the float type:
from decimal import Decimal
def price(string):
    return Decimal(string)

FORMAT = '[{date:ti}] - SALE - PRODUCT: {product:d} - PRICE: ${price:price}'
result = parse(FORMAT, LOG, {'price': price})
print(result)
# <Result () {'date': datetime.datetime(2018, 5, 6, 12, 58, 0, 714611), 'product': 1345, 'price': Decimal('9.99')}>

print(result['date'])
# output : 2018-05-06 12:58:00.714611