# Store a person’s name, and include some whitespace characters 
# at the beginning and end of the name. 
# Make sure you use each character combination, "\t" and "\n", at 
# least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, 
# lstrip(), rstrip(), and strip().

name = " jesús "

print("Stripping Names. \n\toriginal: "+'"'+name+'"'
      +"\n\tlstrip(): "+'"'+name.lstrip()+'"'
      +"\n\trstrip(): "+'"'+name.rstrip()+'"'
      +"\n\tstrip(): "+'"'+name.strip()+'"')