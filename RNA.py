import colorama
from colorama import Fore, Back, Style
colorama.init()

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

    def splice(self):
        # remove anything in transcibed rna string that starts with GU, ending with AG
        s = self.rna_string
        # regex is (GU)([A-Z])+?(?=AG)(AG)
        s = re.sub('(GU)([A-Z])+?(?=AG)(AG)', '', s)
        # print("s==rna? : " + s==self.rna_string )  
        self.splice_string = s
        return self.splice_string

    def RNA_TO_AA(self):
        # use splice string
        self.rna_string = self.splice_string
        # find all substrings of AUG,...,UGA|UGG|UAA
        #  reminder | is or in regex
        r = re.compile(r"(AUG)([A-Z]{3})+?(?=UGA|UAA|UAG)(UGA|UAA|UAG)")
        for match in r.finditer(self.rna_string):
            self.amino_acids.append(match.group(0))
        # return list of amino acids
        return self.amino_acids
    def aa_names(self):
        print(Fore.LIGHTGREEN_EX)
        n=3
        names={
            "UUU":"Phenylalanine","UCU":"Serine","UAU":"Tyrosine","UGU":"Cysteine",
            "UUC":"Phenylalanine","UCC":"Serine","UAC":"Tyrosine","UGC":"Cysteine",
            "UUA":"Leucine"      ,"UCA":"Serine","UAA":"Stop"    ,"UGA":"Stop",
            "UUG":"Leucine"      ,"UCG":"Serine","UAG":"Stop"    ,"UGG":"Tryptophan",
            "CUU":"Leucine"     ,"CCU":"Proline","CAU":"Histidine","CGU":"Arginine",
            "CUC":"Leucine"     ,"CCC":"Proline","CAC":"Histidine","CGC":"Arginine",
            "CUA":"Leucine"     ,"CCA":"Proline","CAA":"Glutamine","CGA":"Arginine",     
            "CUG":"Leucine"     ,"CCG":"Proline","CAG":"Glutamine","CGG":"Arginine",
            "AUU":"Isoleucine","ACU":"Threonine","AAU":"Asparagine","AGU":"Serine",
            "AUC":"Isoleucine","ACC":"Threonine","AAC":"Asparagine","AGC":"Serine",
            "AUA":"Isoleucine","ACA":"Threonine","AAA":"Lysine"    ,"AGA":"Arginine",  
            "AUG":"Methionine","ACG":"Threonine","AAG":"Lysine"    ,"AGG":"Arginine",
            "GUU":"Valine"      ,"GCU":"Alanine","GAU":"Aspartate" ,"GGU":"Glycine",
            "GUC":"Valine"      ,"GCC":"Alanine","GAC":"Aspartate" ,"GGC":"Glycine",
            "GUA":"Valine"      ,"GCA":"Alanine","GAA":"Glutamate" ,"GGA":"Glycine",
            "GUG":"Valine"      ,"GCG":"Alanine","GAG":"Glutamate" ,"GGG":"Glycine"}
        c = 1
        for sequence in self.amino_acids:
           new_sequence=[sequence[i:i+n] for i in range(0, len(sequence), n)]
           print("\t" + Fore.WHITE + str(c) + " : " + Fore.LIGHTGREEN_EX, end='')
           c=c+1
           for codon in new_sequence:
               if names[codon]!="Stop":
                   print(names[codon],end=" ")
               else:
                   continue
           print("\n\t")
        print(Style.RESET_ALL)
               
        
                
                
            




            
