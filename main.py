def shipping():
    cost_of_shipping = int(input('cost: '))
    item_weight = 0

    while item_weight != cost_of_shipping:
        weight = int(input('weight: '))

        if cost_of_shipping > item_weight:
            total_cost = weight * cost_of_shipping
            print(f'cost of shipping is ${total_cost} Shippment will be placed soon')
        elif cost_of_shipping <= item_weight:
            print(f'Sorry cost cannot be 0')
        break
    return shipping()


print(shipping())
