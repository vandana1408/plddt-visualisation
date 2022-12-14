import pickle 
import os 
import re

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
            f = open(pathname, "rb")
            data = pickle.load(f)
            new_pathname = pathname.replace('pkl', 'txt')
            f1 = open(new_pathname, "w")
            f1.write(str(data))
            f1.close()
            
            
            
    

