import pickle 
import os 
import re

def plddt_array(pathname): 
    f = open(pathname, "r")
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
            
    return plddt_array 

def unpickle(pathname): 
    f = open(pathname, "rb")        
    data = pickle.load(f)
    new_pathname = pathname.replace('pkl', 'txt')
    f1 = open(new_pathname, "w")
    f1.write(str(data))
    f1.close()
    
    return new_pathname
    

path="AlphaFoldResults"
directories = []

# Gather all directory names to construct paths for unpickling and matching 
for dirs in os.listdir(path): 
    directories.append(dirs)
    
# unpickle with all pathnames 
for d in directories:
    new_path = path + '/' + d + '/'
    for files in os.listdir(new_path): 
        if re.match("result_model_[0-9].pkl", files): 
            pathname = new_path + files
            unpickled_model = unpickle(pathname)
            plddt_values = plddt_array(unpickled_model)
            print(unpickled_model, len(plddt_values))            
            
           
