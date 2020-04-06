import random 
import numpy as np
from math import *


#calculer la distance euclidienne

def dis_ecl(l1,l2):
    somme = 0
    i = 0
    while i< len(l1):
        somme += (l1[i] - l2[i]) * (l1[i] - l2[i])
        i += 1    
    return sqrt(somme)


#initialiser notre matrice par rapport au nombre de classes 
def init_tab_class(nb_class):
    tab_class = []
    i = 0
    while i < nb_class:
        tab_class.append([])
        i += 1
    return tab_class


#calculer le barycentre de vecteur     
def b_centre(data, tab_class, nb_class):
    list_centre = []
    centre = []
    len_liste_class  = 1
    moy = 0
    somme = 0
    i = 0
    for list_class in tab_class:
        i = 0
        
        while i < 4 :
            for indice in list_class:
                
                somme += data[indice][i]
                len_liste_class += 1
            moy = somme / len(list_class)
            
            centre.append(moy)
            
            len_liste_class  = 1
            somme = 0
            moy = 0
            i += 1
        list_centre.append(centre)
        centre = []
    return list_centre


#Algorithme k-means 
def k_means(data,nb_class):
    
    i = 0
    size_data = (data.size/4)
    list_centre = []
    new_centre = []
    tab_class = []
    
    #choisir les centres en random 
    while i < nb_class:
        i_centre = random.randint(0 , (size_data - 1))
        list_centre.append(data[i_centre]) 
        tab_class.append([])
        i += 1
        
    t = 0 
    
    #tester si les centres chamge plus 
    while not(np.array_equal(new_centre,list_centre)):
        
        tab_class = init_tab_class(nb_class) 
        
        if len(new_centre) > 0 :
            list_centre = new_centre
            
        j = 0
        
        while j < size_data:
            
            k = 0
            new_de = 0
            de = 1000
            winner = 0 
            
            while k < nb_class:
                
                new_de = dis_ecl(data[j],list_centre[k])
                
                if (new_de < de):
                    de = new_de
                    winner = k 
                k += 1
                
            tab_class[winner].append(j)
            j += 1
        #calaculer les nouveau centres 
        new_centre = b_centre(data,tab_class, nb_class)
        
        t += 1
            
    return new_centre


