#Andrea Angiolillo Matr. 761678
#Corrado Ballabio  Matr. 764452



#METODO DI CALCOLO DELLE MATRICI SPARSE CON LA LIBRERIA SCIPY
import scipy
import numpy
import scipy.io
from Tkinter import Tk
from tkFileDialog import askopenfilename
import psutil
import time
from scipy import linalg
import scipy.sparse.linalg
import os 


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
#Sparse Direct Solvers
    A = A.tocsc() #coo_matrix.tocsc()Return a copy of this matrix in Compressed Sparse Column format -> questo mi serve per passare la matrice in un formato adatto per linalg
    start = time.time() #Start Time
    x = scipy.sparse.linalg.spsolve(A, b, use_umfpack=True) #risolvo
    print "Sparse Direct Solvers {" 
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