# plddt-visualisation

Creating scripts to enable user to unpickle a results_model file from AlphaFold Results and visualise the plddt array values against the amino acids in the relaxed model results. 

**combine.py** 
Script with the entire product. Need to abstract some of the code in order to progress to matching plddt values with amino acids in relaxed model results. 

**unpickle.py** 
Section of combine.py that handles unpickling the result model file from each protein target.  

**plddt_values.py**
Section of combine.py that takes the unpickled file and returns an array of the plddt values and it's count 

**pdb_reader.py** 
Section of combine.py that will read the pdb file into a data frame and access the b_factor values (that appear to be unique to the amino acids in the file?).



