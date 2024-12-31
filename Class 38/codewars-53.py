def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ""
    stock = {category: 0 for category in categories}
    for book in stocklist:
        category, amount = book.split()
        if category[0] in stock:
            stock[category[0]] += int(amount)
    return " - ".join(f"({category} : {amount})" for category, amount in stock.items())        