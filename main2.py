dict1 = {"attack": 1}
dict2 = {"attack": 2}

print(dict1["attack"])

dict1.update(
    {key: dict1[key] + dict2[key] if key in dict2 else dict1[key] for key in dict1}
)
"""
this line will add a key to the new dictionary fo that key does not exist
may be useful for adding functionality or special skills based on equipment

dict1.update({key: dict2[key] for key in dict2 if key not in dict1})
"""
print(dict1["attack"])
