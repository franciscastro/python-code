list_of_stuff = []

stuff1 = input( "Enter item: " )
stuff2 = input( "Enter item: " )

list_of_stuff.append( stuff1 )
list_of_stuff.append( stuff2 )

if ( len( list_of_stuff ) > 2 ) :
    print( "I have more than two items." )
elif ( len( list_of_stuff ) == 2 ) :
    print( "I have exactly two items." )
else :
    print( "I have less than two items:" )

for item in list_of_stuff :
    print( item )
