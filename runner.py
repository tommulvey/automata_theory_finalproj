# custom classes import
from RNA import RNA
from WebDriver import WebDriver
# std libraries import
import os, sys, time



DRIVER = WebDriver()
RNA = RNA()

for i in range(1):
    DRIVER.click_reset()
    dna = DRIVER.get_textarea()
    print("DNA : " + dna + "\n-------------------")
    RNA.change_dna_string(dna)
    print("RNA : " + RNA.DNA_to_RNA() + "\n-------------------")
    