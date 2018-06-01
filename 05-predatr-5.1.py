def make_a_barnyard_noise():
	print("moo")


#The return statement
def myfunction(var1):
	var2 = var1 + var2
	return var2


five_var = myfunction(3)

print(myfunction(3))
print(five_var)



#Dictionary Usage - WHAT IS WRONG WITH THE INDENTS?
def uppercase(input_str):
    output_str = ''
    case_switches = {
    'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e':'E', 'f':'F',
    'g':'G', 'h':'H', 'i':'I', 'j':'J', 'k':'K', 'l':'L',
    'm':'M', 'n':'N', 'o':'O', 'p':'P', 'q':'Q', 'r':'R',
    's':'S', 't':'T', 'u':'U', 'v':'V', 'w':'W', 'x':'X',
    'y':'Y', 'z':'Z',
     }

	for letter in input_str:
		if letter in case_switches.keys():
	        output_str = output_str + case_switches[letter]
	    else:
	        output_str = output_str + letter

	return output_str


print(uppercase("ksjfksdhfkjsdfksjdhfkjsdhfdKDJHFKDJHFD")

#Dictionary Usage - WHAT IS WRONG WITH THE INDENTS?


