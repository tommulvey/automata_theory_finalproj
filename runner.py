# custom classes import
from RNA import RNA
from WebDriver import WebDriver
# std libraries import
import os, sys, time
import colorama
from colorama import Fore, Back, Style
colorama.init()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

DRIVER = WebDriver()
RNA = RNA()

# RANDOMLY GET DNA STRAND FROM WEBSITE
cls()
DRIVER.click_reset()
dna = DRIVER.get_textarea()
print("DNA >> \n\t" + Fore.BLUE + dna + Style.RESET_ALL + "\n-----------------------------\n")
RNA.change_dna_string(dna)

# MAKE RNA FROM DNA
print("RNA UNSPLICED >> \n\t" + Fore.CYAN + RNA.DNA_to_RNA() + Style.RESET_ALL + "\n-----------------------------\n")


# SPLICE THE RNA
print("RNA SPLICED  >> \n\t" + Fore.LIGHTMAGENTA_EX + RNA.splice() + Style.RESET_ALL + "\n-----------------------------\n")


# CONVERT TO AA AND SHOW CONVERSIONS
print("AMINO ACIDS >> \n\t") #  + '\n\t'.join(RNA.RNA_TO_AA()) + "\n-----------------------------\n")
c=1
for i in RNA.RNA_TO_AA():
    print("\n\t" + str(c) + ": " + Fore.YELLOW + str(i) + Style.RESET_ALL  )
    c=c+1
print("\n-----------------------------\n")


print("AMINO ACIDS CONVERTED>>\n")
Amino_Acids=RNA.aa_names()
print("\n-----------------------------\n")
