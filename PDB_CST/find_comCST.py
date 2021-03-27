#!/usr/bin/python
# -*- coding: utf-8 -*-


import os,sys,getopt
import numpy
import math
from math import sqrt, acos

list = ['LEU_LEU', 'ALA_ILE', 'ARG_ILE', 'PRO_PRO', 'MET_LEU', 'MET_VAL', 'ARG_VAL', 'PHE_MET', 'ARG_PRO', 'HIS_LEU', 'PHE_PRO', 'ILE_LEU', 'ILE_ALA', 'VAL_PRO', 'ILE_VAL', 'TYR_PRO', 'LEU_PRO', 'ASN_ILE', 'ASN_PHE', 'PHE_ILE', 'PHE_THR', 'ALA_LEU', 'PHE_LEU', 'TYR_PHE', 'SER_ILE', 'GLN_ALA', 'GLN_LEU', 'TYR_LEU', 'ILE_PRO', 'LYS_PRO', 'VAL_ALA', 'GLY_ALA', 'LYS_ILE', 'ALA_PRO', 'TYR_ILE', 'MET_ILE', 'ALA_GLU', 'ARG_ALA', 'GLN_VAL', 'ASN_VAL', 'HIS_ILE', 'VAL_LEU', 'SER_ALA', 'ARG_LEU', 'LEU_ALA', 'VAL_VAL', 'PHE_VAL', 'TYR_VAL', 'GLN_ILE', 'ALA_ALA', 'SER_PRO', 'ASN_LEU', 'LYS_SER', 'GLN_MET']
#PCT = open('PDB_cst.txt', 'r')
for i in range(0,53):
    P = list[i].split('_')[0]
    N = list[i].split('_')[1]
    #print(P,N)
    PCT = open('PDB_cst.txt', 'r')
    WT = open(list[i] + '.txt', 'w')
    for li in PCT:
        #print(li.split()[1])
        if li.split()[1] == P and li.split()[2] == N:
            print(li)
            WT.write(li)