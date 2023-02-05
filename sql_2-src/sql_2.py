# brute force to get the password digest containing bungle- as the start and end with '='

# strings with 1st char being any digit between 1 and 9 is evaluated as true, other strings are false
# password='gibberish'='' -> false='' -> false=false -> true
# password='gibberish'='more gibberish' -> false='more gibberish' -> false=false -> true
