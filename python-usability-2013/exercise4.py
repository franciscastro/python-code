class Product :

    def __init__ ( self, name, price, quantity ) :
        self.name = name
        self.price = price
        self.quantity = quantity

class Cash_Register :

    def __init__ ( self, tax ) :
        self.item_list = []
        self.tax = ( tax / 100 )

    def add_item ( self, item ) :
        self.item_list.append( item )

    def compute_total ( self ) :
        total = 0
        for item in self.item_list :
            total += ( item.price * item.quantity )
        return total

    def compute_total_plus_tax ( self, total ) :
        total_with_tax = ( total * self.tax ) + total
        return total_with_tax

    def display_item_summary ( self ) :
        for item in self.item_list :
            print( "Product: " + item.name )
            print( "Price: " + str( item.price ) )
            print( "Quantity: " + str( item.quantity ) )
            print( "Product total: " + str( item.price * item.quantity ) + "\n" )

    # Function to check payment
    def check_payment ( self, payment, amount_to_pay ) :

        if float( payment ) < amount_to_pay :
            print ( "\nYou don\'t have enough cash." )
        elif float ( payment ) == amount_to_pay :
            print ( "\nThank you for giving the exact amount." )
        else :
            change = int ( payment ) - amount_to_pay
            print ( "\nYou paid: " + str( payment ) )
            print ( "Your change is: " + str( format(change, '.3f') ) )

"""-----------------------------------------------------------------------------------"""

reg_tax = float( input( "Enter tax for the transaction: " ) )

# Instantiate Cash_Register object
reg = Cash_Register( reg_tax )

# Loop for receiving Product objects into the Cash_Register object
answer = ( input ( "\nEnter item? (Y/N): " ) ).lower()
while ( answer == "y" ) :
    item_name = input( "Item name: " )
    item_price = float( input( "Item price: " ) )
    item_quantity = int( input( "Quantity: " ) )

    #Instantiate Product object
    prod = Product( item_name, item_price, item_quantity )

    #Add item to cash register
    reg.add_item( prod )

    answer = ( input ( "\nEnter item? (Y/N): " ) ).lower()
else :
    print( "\nCash register has recorded " + str( len( reg.item_list ) ) + " items.\n\nItem summary:" )
    reg.display_item_summary()

print ( "\nTotal amount of items recorded: " + str( reg.compute_total() ) )
print ( "\nTotal amount of items with tax: " + str( reg.compute_total_plus_tax( reg.compute_total() ) ) )

payment = float( input( "\nEnter cash amount for payment: " ) )
reg.check_payment( payment, reg.compute_total_plus_tax( reg.compute_total() ) )
