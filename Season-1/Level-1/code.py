'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    MAX_PAYABLE = 10000.00
    
    net = Decimal('0')
    total_products = Decimal('0')

    for item in order.items:
        if item.type == 'product':
            cost = Decimal(str(item.amount)) * Decimal(str(item.quantity))
            total_products += cost
            net -= cost
        elif item.type == 'payment':
            net += Decimal(str(item.amount))
        else:
            return f"Invalid item type: {item.type}"

    if total_products > Decimal(str(MAX_PAYABLE)):
        return "Total amount payable for an order exceeded"

    tolerance = Decimal('0.01')
    if abs(net) > tolerance:
        return f"Order ID: {order.id} - Payment imbalance: ${float(net):.2f}"
    
    return f"Order ID: {order.id} - Full payment received!"