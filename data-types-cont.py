#string

s = "I am a sting."
print(type(s))	# will say str

#Boolean

yes = True	#Boolean true
print(type(yes))

no = False	#Boolean False 
print(type(no))

#List -- ordered and interchangeable

alpha_list = ["a", "b", "c"]	#list initialization
print(type(alpha_list))			#will say tuple
print(type(alpha_list[0]))		#will say string
alpha_list.append("d")			#will add "d" to the list end
print(alpha_list)				#will print list

#tuple -- ordered and unchangeable

alpha_tuple = ("a", "b", "c")	#tuple initialization
print(type(alpha_tuple))		#will say tuple

try:							#attempt following
	alpha_tuple[2] = "d"		#wont work and will raise TypeError
except TypeError:				#when we get typeerror
	print("We can't add elements to tuples!")	#print this message
print(alpha_tuple)			#will print tuple