import re
'''
RNA CLASS. All methods (like convert dna to rna) are here.
'''
class RNA():

    def __init__(self, dna_string=""):
        self.dna_string = dna_string
        self.rna_string = ""
        self.amino_acids = []
    
    def change_dna_string(self, new_string):
        self.dna_string = new_string

    def DNA_to_RNA(self):
        table = {
            'T' : 'A',
            't' : 'A',
            'G' : 'C',
            'g' : 'C',
            'C' : 'G',
            'c' : 'G',
            'A' : 'U',
            'a' : 'U',
        }

        s = ""
        for i in self.dna_string:
            s += table[i]
            
        # add a space after every 3 to make life easier in regex
        s = ''.join([s[i:i + 3] for i in range(0, len(s), 3)])
        self.rna_string = s
        return self.rna_string

    def RNA_TO_AA(self):
        # find all substrings of AUG,...,UGA|UGG|UAA
        #  reminder | is or in regex
        r = re.compile(r"(AUG)([A-Z]{3})+?(?=UGA|UAA|UAG)(UGA|UAA|UAG)")
        for match in r.finditer(self.rna_string):
            self.amino_acids.append(match.group(0))
        # return list of amino acids
        return self.amino_acids
