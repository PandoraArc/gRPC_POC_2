
def making_coffee(coffee_order: str, protocol):
    if coffee_order.lower() == 'espresso':
        return {
            'message': "got it here, recipe",
            'ingredient': ['1/2 cup ground coffee (French or other dark roast)', '1-1/2 cups cold water'],
            'status': 'complete',
            'protocol': protocol
        }
    elif coffee_order.lower() == 'latte':
        return {
            'message': "got it here, recipe",
            'ingredient': ['1/3 espresso', '2/3 steamed milk'],
            'status': 'complete',
            'protocol': protocol
        }
    else :
        return {
            'message': "there is no order in my cafe",
            'ingredient': [],
            'status': 'fail',
            'protocol': protocol
        }