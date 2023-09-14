import math

DEFAULT_DOG_ORDER_CONFIG = {
    'small': 10,
    'medium': 20,
    'large': 30,
}


def get_order_amount(dogs, leftover_amount, dog_order_config=DEFAULT_DOG_ORDER_CONFIG):
    total = 0
    for dog_type, number_of_dogs in dogs.items():
        if dog_type not in dog_order_config:
            raise Exception('Unknown dog type found')
        total += dog_order_config[dog_type] * number_of_dogs

    total -= leftover_amount
    total = max(total, 0)
    total *= 1.2
    total = math.ceil(total)
    return total
