import re 
#filename = "AlphaFoldResults/Hsp16.9_and_Hsp17.5_1/result_model_1.json"

# path="AlphaFoldResults"
# directories = []

# # Gather all directory names to construct paths for unpickling and matching 

# for dirs in os.listdir(path): 
#     directories.append(dirs)

# for d in directories: 
#     new_path = path + '/' + d + '/'
#     for files in os.listdir(new_path): 
#         new_pathname = new_path + files
#         f = open(new_pathname, 'r')
#         print(f.read())


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
        
print(plddt_array)
