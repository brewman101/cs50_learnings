import re
quote = "There's no only one thing I hate more than lying: skim milk.  Which is water that's lying about being milk. - Ron Swanson"
#print(re.search("milk", quote))
#print(len(re.findall("milk", quote)))
print(re.split("milk", quote))