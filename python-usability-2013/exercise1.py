# Get values for items
item_1 = input( "Item 1: " )
item_2 = input( "Item 2: " )
item_3 = input( "Item 3: " )
item_4 = input( "Item 4: " )
item_5 = input( "Item 5: " )

# Compute the total of items
total_items = float(item_1) + float(item_2) + float(item_3) + float(item_4) + float(item_5)

# Get the tax
tax = input( "Enter tax: " )
tax = float( tax ) / 100

# Compute the total of items with tax
total_items_with_tax = total_items + ( total_items * tax )

# Get the tip
tip = input( "Enter tip: " )
tip = float( tip ) / 100

# Compute the total of items with tip
total_items_with_tip = total_items_with_tax + ( total_items_with_tax * tip )

# Display all details
print ( "Total of items: " + str( total_items ) )
print ( "Total of items with tax: " + str( total_items_with_tax ) )
print ( "Total to be paid with tip: " + str( total_items_with_tip ) )
