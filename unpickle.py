import pickle 
import os 
import re

path="AlphaFoldResults"
directories = []

# Gather all directory names to construct paths for unpickling and matching 

for dirs in os.listdir(path): 
    directories.append(dirs)
    
# json_pathnames = []

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
            
        
            # json_pathnames.append(new_pathname)


        
    


# from collections import Counter

# def most_common():
#     infile = open("shapecolour.p",'rb')
#     new_list = pickle.load(infile) 
#     infile.close()
    
#     dict_counter = Counter((item['shape'], item['colour']) for item in new_list)
#     shape, colour = dict_counter.most_common(1)[0][0][0], dict_counter.most_common(1)[0][0][1]
    
#     return {'shape': shape, 'colour': colour}

# if __name__ == "__main__": 
#     print(most_common())

