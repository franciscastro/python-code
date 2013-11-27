# Class definition
class Person :

    # Initialization
    def __init__ ( self, name ) :
        self.name = name
        self.cash1 = 0
        self.cash2 = 0
        self.cash3 = 0

    # Function for receiving money (user input)
    def receive_money ( self ) :
        self.cash1 = float( input ( "Enter cash: " ) )
        self.cash2 = float( input ( "Enter cash: " ) )
        self.cash3 = float( input ( "Enter cash: " ) )

    # Function for computing average; returns computed average
    def compute_average ( self ) :
        average = ( self.cash1 + self.cash2 + self.cash3 )/3
        return average

# Instantiating an object of class Person
p1 = Person( "Obi-Wan Kenobi" )

# Accessing the attributes of p1, which holds an instance of class Person
print( p1.name )
print( p1.cash1 )

# Calling the receive_money method of Person through p1
p1.receive_money()

print( "\nMoney I have: " + str( p1.cash1 ) + ", " + str( p1.cash2 ) + ", " + str( p1.cash3 ) )

# Calling the compute_average method of Person through p1
ave = p1.compute_average()

print( "\nThe average amount is: " + str( ave )  )
