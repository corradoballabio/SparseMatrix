#Andrea Angiolillo Matr. 761678
#Corrado Ballabio  Matr. 764452


import time
import os 
from Tkinter import Tk
from tkFileDialog import askopenfilename
import numpy
import scipy
import psutil
import scipy.io
from scikits import umfpack
from scipy import linalg


if __name__ == '__main__':
    
    process = psutil.Process(os.getpid()) #
####################################################################################################################
#SELEZIONO LA MATRICE SPARSA
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file   
    A =scipy.io.mmread(filename)#prendo la matrice sparsa
####################################################################################################################
#CALCOLO xe E b
    print "Dimensioni della matrice A" 
    print A.shape
    print "\n"
    xe = numpy.ones(A.shape[1])#genero xe di soli 1
    print "xe:"
    print xe
    print "\n"
    b = A * xe #calcolo b
    print "b:"
    print b
    print "\n"
####################################################################################################################    
#scikit-umfpack
    A = A.tocsc() #coo_matrix.tocsc()Return a copy of this matrix in Compressed Sparse Column format -> Questo mi serve per adattare la matrice alla libreria
    start = time.time() #Start Time
    x = umfpack.spsolve(A, b)
    print "scikit-umfpack {"
    print "\n"
    print "Memory (kiloBytes):"
    print process.memory_info().rss # Stampo la memoria utilizzata per il calcolo della soluzione del sistema  -> kiloBytes
    print "\n"
    end = time.time() #Stop Time
    time = end - start
    error = linalg.norm(x-xe)/linalg.norm(xe) #calcolo l'errore
    print "Time:"
    print time 
    print "\n"
    print "Error:"
    print error
    print "\n"
    print "}"
    
   