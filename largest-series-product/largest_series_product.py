def largest_product(series, size):
    if size == 0:
        return 1
    elif (size < 0) | (size > len(series)) | ((series.isnumeric()) == False):
        raise ValueError("Error")
    
    products = []
    for i in range(len(series)-size + 1):
        product = 1
        for j in range(i, i+size):
            product *= int(series[j])
        products.append(product)

    return max(products)