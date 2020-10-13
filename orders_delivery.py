def max_cost(n, m, arr):
    """
    :param n: Total number of products
    :param m: Products to deliver: m <= n
    :param arr: Array of tuples (prod_cost, del_fee)
    :return: Subset size m with max total cost
    """

    # Get the first m items

    total = 0
    min_del_fee = float("inf")
    products = []

    for i in range(m):

        cost, del_fee = arr[i]
        products.append(cost)
        total += cost

        if del_fee < min_del_fee:
            min_del_fee = del_fee

    total += m * min_del_fee

    for i in range(m + 1, n):
        cost, del_fee = arr[i]

        if del_fee >= min_del_fee:
            min_price_product = float("inf")

            for product in products:
                if product < cost and product < min_price_product:
                    min_price_product = product

            # remove min price product from products so far and add new product
            products.remove(min_price_product)
            products.append(cost)

            # update the cost
            total = total - min_price_product + cost

        else:
            # calculate delivery fees
            new_total_del_fee = m * del_fee
            prev_total_del_fee = m * min_del_fee

            # get new total cost with new del fee
            cost_with_new_del_fee = total - prev_total_del_fee + new_total_del_fee

            # check if adding the new product will increase the total so far
            min_price_product = float("inf")

            for product in products:
                if product < cost and product < min_price_product:
                    min_price_product = product

            # compare it with the previous total
            if cost_with_new_del_fee - min_price_product + cost > total:
                total = cost_with_new_del_fee - min_price_product + cost
                products.remove(min_price_product)
                products.append(cost)
                min_del_fee = del_fee

    return total, products


if __name__ == '__main__':
    arr = [(20, 10), (80, 9), (40, 14), (60, 10), (50, 12), (80, 9), (83, 1), (82, 2), (80, 9), (81, 3)]
    tot, prods = max_cost(10, 3, arr)









