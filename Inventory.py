
from Register_product import register_sale
from Show_summary import show_summary


def main(): 
    total_amount = 0

    sale = register_sale()
    total_amount = sale["subtotal"]

    show_summary([sale], total_amount)


main()