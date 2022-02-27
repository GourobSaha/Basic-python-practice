# String Slicing = Create a substring by extracting elements from another string
# indexing[] or slice()

# indexing[]
name2 = "Gourob Saha"
first_name = name2[:6]
last_name = name2[7:]
no_name = name2[1:4:9]
reversed_name = name2[::-1]

print(first_name)
print(last_name)
print(no_name)
print(reversed_name)

# slice()
website1 = "http://google.com"
website2 = "http://gourob_saha.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])
