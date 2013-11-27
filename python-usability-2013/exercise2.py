# Function to compute total
def get_total ( item1, item2, item3, item4, item5 ) :

    # Compute the total of items
    total_items = float(item1) + float(item2) + float(item3) + float(item4) + float(item5)

    return total_items

# Function to compute tax
def compute_tax ( tax, total ) :

    tax = float( tax ) / 100
    
    # Compute the total of items with tax
    total_items_with_tax = total + ( total * tax )

    return total_items_with_tax

# Function to compute tip
def compute_tip ( tip, total_with_tax ) :

    tip = float( tip ) / 100

    # Compute the total of items with tip
    total_items_with_tip = total_with_tax + ( total_with_tax * tip )

    return total_items_with_tip

# Function to display all details
def display_details ( total_items, total_with_tax, total_with_tip ) :

    # Display all details
    print ( "\nTotal of items: " + str( total_items ) )
    print ( "Total of items with tax: " + str( total_with_tax ) )
    print ( "Total to be paid with tip: " + str( total_with_tip ) )

# Function to check payment
def check_payment ( payment, amount_to_pay ) :

    if float( payment ) < amount_to_pay :
        print ( "\nYou don\'t have enough cash." )
    elif float ( payment ) == amount_to_pay :
        print ( "\nThank you for giving the exact amount." )
    else :
        change = int ( payment ) - amount_to_pay
        print ( "\nYou paid: " + str( payment ) )
        print ( "Your change is: " + str( format(change, '.3f') ) )

"""---------------------------------------------------------------------"""

# Get values for items
item_1 = input( "Item 1: " )
item_2 = input( "Item 2: " )
item_3 = input( "Item 3: " )
item_4 = input( "Item 4: " )
item_5 = input( "Item 5: " )

total_items = get_total ( item_1, item_2, item_3, item_4, item_5 )

# Get the tax
tax = input( "\nEnter tax: " )
total_with_tax = compute_tax ( tax, total_items )

# Get the tip
tip = input( "\nEnter tip: " )
total_with_tip = compute_tip ( tip, total_with_tax )

# Display all details
display_details ( total_items, total_with_tax, total_with_tip )

# Get payment
payment = input( "\nEnter payment: " )
check_payment( payment, total_with_tip )
