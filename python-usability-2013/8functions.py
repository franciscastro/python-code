
# Function without a return value
def detail_printer ( value_to_print1, value_to_print2, value_to_print3 ) :
    print ( "\nThe first input of the user is: " + value_to_print1 )
    print ( "The second input of the user is: " + value_to_print2 )
    print ( "The third input of the user is: " + value_to_print3 )

# Function with a return value
def average_computer ( value1, value2, value3 ) :
    average_computed = ( float( value1 ) + float( value2 ) + float( value3 ) ) / 3
    return average_computed


# Receive values from the user
input1 = input( "Enter a number: " )
input2 = input( "Enter a number: " )
input3 = input( "Enter a number: " )

"""
Here, I call the detail_printer function and pass to it the variables above.

Note that since detail_printer does not return any value,
the function call is not assigned to a variable
"""
detail_printer( input1, input2, input3 )

"""
Here, I call the average_computer function and pass to it the variables above.

Note that since average_computer returns a value,
the function call is assigned to a variable.

The variable to which average_computer is assigned receives the value
which average_computer returns.
"""
answer = average_computer( input1, input2, input3 )

# Print the value of the variable answer which it recevied from average_computer
print ( "\nThe computed average is: " + str( answer ) )
