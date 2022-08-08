import re 
import json

#filename = "AlphaFoldResults/Hsp16.9_and_Hsp17.5_1/result_model_1.json"

f = open("AlphaFoldResults/Hsp16.9_and_Hsp17.5_1/result_model_1.txt", "r")
contents = f.readlines()

for count, string in enumerate(contents): 
    if 'plddt' in string: 
        new_contents = contents[count:]

delete = re.search(r'(.*\[).*\)(.*)', str(new_contents))
# print(f"group 1 = {delete.group(1)} \ngroup 2 = {delete.group(2)}")

plddt_vals = str(new_contents).replace(delete.group(1), '').replace(delete.group(2), '').replace('])', '')
plddt_array = []

for items in plddt_vals.split(','): 
    val = re.sub('[^0-9.]*', '', items)
    if val != '': 
        plddt_array.append(val)
        
print(len(plddt_array))
