data = {"b":20, "a":35}
num = data["b"]
data["b"] = (-num)
print (data)

data["c"] = 40
print (data)

data['b'] = None
print (data)

keys = list (data.keys())
keys.sort()
for key in keys:
    print(key, data[key])
print (data)


