# -*- coding: utf-8 -*-
"""

@author: CollegeBoreal
"""

def exo_03(2,4,6,8):
  # Selectionner une liste de nombre pairs uniquement
  pairs =[x*x for x in (2,4,6,8)]
  return sorted(pairs)

def main():
  print( exo_03( [ 3, 5, 7, 9, 98, 13, 24, 56, 17, 9, 8 ] ) )

if __name__== "__main__":
  main()
