from biopandas.pdb import PandasPdb 

with open('AlphaFoldResults/Hsp16.9_and_Hsp17.5_2/relaxed_model_1.pdb', 'r') as f:
    file_contents = f.readlines()

ppdb = PandasPdb()
ppdb.read_pdb_from_list(file_contents)


b_factors = ppdb.df['ATOM']['b_factor'].unique()

print(len(b_factors))

