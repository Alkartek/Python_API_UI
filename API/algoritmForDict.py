result8 = {
    "name": "morpheus",
    "job": "zion resident",
    "updatedAt": "2023-03-15T07:14:43.639Z"
}

def dicte_key(dicte):
    result_key = []
    for key,value in dicte.items():
        if key != "updatedAt":
            result_key.append(key)
    return result_key

def dict_value(dicte):
    result_value = []
    for key,value in dicte.items():
        if "2023"  not in value:
            result_value.append(value)
    return result_value

print(dicte_key(result8))
print(dict_value(result8))