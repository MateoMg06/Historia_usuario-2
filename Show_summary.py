
# Show summary with total quantity per product

def show_summary(sales_list, total_amount):
    print("SUMMARY")

    if sales_list == []:
        print("No sales")
        print("Total", 0)
    else:
        product_totals = {}

        for sale in sales_list:
            name = sale["name"]
            quantity = sale["quantity"]
            prices = sale["price"]

            if name in product_totals:
                product_totals[name] = product_totals[name] + quantity
            else:
                product_totals[name] = quantity

        for name in product_totals:
            print("Product", name)
            print("Total quantity", product_totals[name])

        print("Total", total_amount)
        print("unitary price " , prices )