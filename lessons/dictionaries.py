"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int] 

# Initialize to an empty dictionary 

schools = dict()

# Set a key-value pairing in the dictionary 

schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

#Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key value pair from a dictionary 
# by its key
schools.pop("Duke")

# test for the exisence of a key

is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# update/ resassign a key-value pair 

schools["UNC"] = 20000
schools["NCSU"] = schools["NCSU"] + 100

# print(schools["UNCC"])
# Example looping over the keys of a dict

for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
