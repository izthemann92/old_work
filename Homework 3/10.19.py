# # Name: Blake Mann
# # PSID: 1832387

class ItemToPurchase:

    # Parameter Constructor
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # Implement the method
    def print_item_cost(self):
        # print the output in a specifed format
        string = '{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price,
                                            (self.item_quantity * self.item_price))
        cost = self.item_quantity * self.item_price
        return string, cost

    # Implement the method print_item_description
    def print_item_description(self):
        string = '{}: {}, %d oz.'.format(self.item_name, self.item_description, self.item_quantity)
        print(string)
        return string


# Declare the class ShoppingCart
class ShoppingCart:

    # Parameter Constructor
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    # Implement method to add item in the shopping cart
    def add_item(self):
        print('ADD ITEM TO CART')
        # prompt the name and description of item,price and Quentity
        item_name = str(input('Enter the item name:'))
        print()
        item_description = str(input('Enter the item description:'))
        print()
        item_price = int(input('Enter the item price:'))
        print()
        item_quantity = int(input('Enter the item quantity:'))
        print()

        # Append the above values in to the list
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

    # Implement the method to delete the item in the cart
    def remove_item(self):
        print('REMOVE ITEM FROM CART')

        # prompt the item to remove the list
        string = str(input('Enter name of item to remove:'))
        print()
        i = 0

        # Using for-loop to iterate every item
        for item in self.cart_items:
            # If item found delete in the list
            if (item.item_name == string):
                del self.cart_items[i]
                # set the flag value to true
                # break from the list
                flag = True
                break

            # Otherwiese set value to false
            else:
                flag = False
            i += 1

        # IF the value not found
        if (flag == False):
            # print the message
            print('Item not found in cart. Nothing removed.')

    # Implement the method modifyitem to chane the Quantity
    def modify_item(self):
        print('CHANGE ITEM QUANTITY')

        # Prompt the input item
        name = str(input('Enter the item name:'))
        print()

        # Using for-loop to iterate every item
        for item in self.cart_items:
            # If item found update Quantity in the list
            if (item.item_name == name):
                quantity = int(input('Enter the new quantity:'))
                print()
                item.item_quantity = quantity
                # set the flag value to true
                # break from the list
                flag = True
                break

            # Otherwiese set value to false
            else:
                flag = False

        # IF the value not found
        if (flag == False):
            # print the message
            print('Item not found in cart. Nothing modified.')
        print()

    # implement method to compute total number of items in the cart
    def get_num_items_in_cart(self):
        num = 0
        # Using for-loop to iterate the cart
        for item in self.cart_items:
            # ADD the Quantities
            num = num + item.item_quantity


        return num

    # Implement the method
    def get_cost_of_cart(self):
        tcost = 0
        cost = 0


        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)
            tcost += cost

        # return the value
        return tcost

    # Implement the method to print the total
    def print_total(self):
        tcost = self.get_cost_of_cart()
        if (tcost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            self.output_cart()

    # Implement the method to print_descriptions
    def print_descriptions(self):
        print('OUTPUT ITEMS\' DESCRIPTIONS')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date), end='\n')
        print('\nItem Descriptions')

        for item in self.cart_items:
            print('{}: {}'.format(item.item_name, item.item_description))

    # Implement the method output_cart()
    def output_cart(self):
        print('OUTPUT SHOPPING CART')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('Number of Items:', self.get_num_items_in_cart())
        print()
        tc = 0
        for item in self.cart_items:
            print('{} {} @ ${} = ${}'.format(item.item_name, item.item_quantity,
                                             item.item_price, (item.item_quantity * item.item_price)))
            tc += (item.item_quantity * item.item_price)

        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        print()

        print('Total: ${}'.format(tc))


# Implement the method print_menu
def print_menu(customer_Cart):
    # declare the string menu
    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            'i - Output items\' descriptions\n'
            'o - Output shopping cart\n'
            'q - Quit\n')

    option = ''
    # Using while loop
    # to iterate until user enters q

    while option != 'q':
        print(menu)

        # Prompt the Command
        option = input('Choose an option:')
        print()

        # repeat the loop until user enters a,i,r,c,q commands
        while (option != 'a' and option != 'o' and option != 'i' and option != 'r'
               and option != 'c' and option != 'q'):
            option = input('Choose an option:')
            print()

        # If the input command is a
        if option == 'a':
            # call the method to the add elements to the cart
            customer_Cart.add_item()

        # If the input command is o
        if option == 'o':
            # call the method to the display the elements in the cart
            customer_Cart.output_cart()

        # If the input command is i
        if option == 'i':
            # call the method to the display the elements in the cart
            customer_Cart.print_descriptions()

        # If the input command is i
        if option == 'r':
            customer_Cart.remove_item()
        if option == 'c':
            customer_Cart.modify_item()


def main():
    # Type main section of code here
    # prompt and read the customers name
    customer_name = str(input('Enter customer\'s name:'))
    print()

    # prompt the date
    current_date = str(input('Enter today\'s date:'))
    print('\n')

    # print the name and date
    print('Customer name:', customer_name, end='\n')
    print('Today\'s date:', current_date, end='\n')

    # call the class with the parameters
    newCart = ShoppingCart(customer_name, current_date)

    # print the details.
    print_menu(newCart)


if __name__ == '__main__':
    main()