import delorean

from decimal import Decimal


log = '[2018-05-05T11:07:12.267897] - SALE - PRODUCT: 1345 - PRICE: $09.99'

# basic - isolate each element and parse them into proper type
# split log into parts and create vars ignoring 'SALE'
divide_it = log.split(' - ')
timestamp_string, _, product_string, price_string = divide_it

# parse timestamp into a datetime object isolate the ISO format
timestamp = delorean.parse(timestamp_string.strip('[]'))

# isolate and parse product_id into integer
product_id = int(product_string.split(':')[-1])

# parse the product_id into a Decimal type - split('$') and Decimal (NOT FLOAT ! )
price = Decimal(price_string.split('$')[-1])


# OUTPUT - all values are nin native Python formats
print('log - ', log)
print('divide_it - ',  divide_it)
print(timestamp_string, _, product_string, price_string)
print('timestamp - ', timestamp)
print(product_string, ' - ' , product_id)
print('price - ', type(price), price)

print('timestamp         product_id          price')
print(timestamp, product_id, price)
# timestamp         product_id          price
# Delorean(datetime=datetime.datetime(2018, 5, 5, 11, 7, 12, 267897), timezone='UTC') 1345 9.99
''' OUTPUT 
log -  [2018-05-05T11:07:12.267897] - SALE - PRODUCT: 1345 - PRICE: $09.99
divide_it -  ['[2018-05-05T11:07:12.267897]', 'SALE', 'PRODUCT: 1345', 'PRICE: $09.99']
[2018-05-05T11:07:12.267897] SALE PRODUCT: 1345 PRICE: $09.99
timestamp -  Delorean(datetime=datetime.datetime(2018, 5, 5, 11, 7, 12, 267897), timezone='UTC')
PRODUCT: 1345  -  1345
price -  <class 'decimal.Decimal'> 9.99
timestamp         product_id          price
Delorean(datetime=datetime.datetime(2018, 5, 5, 11, 7, 12, 267897), timezone='UTC') 1345 9.99

'''

# it could be done as a class !!!!
class PriceLog(object):
    def __init__(self, timestamp, product_id, price):
        self.timestamp = timestamp
        self.product_id = product_id
        self.price = price
    def __repr__(self):
        # return '<PriceLog ({}, {}, {})>'.format(self.timestamp, self.product_id, self.price)
        return f"<PriceLog ({self.timestamp}, {self.product_id}, {self.price})>"

    @classmethod
    def parse(cls, text_log):
        """
        Parse form a text log with the format
        [<Timestamp>] - SALE - PRODUCT: <product_id> - PRICE: $<price_id>
        to a PriceLog object
        """
        divide_it = text_log.split(' - ')
        tmp_sting, _, product_string, price_string = divide_it
        timestamp = delorean.parse(tmp_sting.strip('[]'))
        product_id = int(product_string.split(':')[-1])
        price = Decimal(price_string.split('$')[-1])
        return cls(timestamp=timestamp, product_id=product_id, price=price)


print("CLASSS PARSER : ", PriceLog.parse(log))

"""
CLASSS PARSER :  <PriceLog (Delorean(datetime=datetime.datetime(2018, 5, 5, 11, 7, 12, 267897), timezone='UTC'), 1345, 9.99)>
"""