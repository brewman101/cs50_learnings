# Cool application working to find capitals in strings

# camel case program

new_camel_case=""
camel_case=input("camelCase: ")

for _ in range(len(camel_case)):
    if camel_case[_].isupper() is True:
        new_camel_case=new_camel_case + "_" + camel_case[_]
    else:
        new_camel_case=new_camel_case + camel_case[_]

new_camel_case=new_camel_case.lower()
print(new_camel_case)