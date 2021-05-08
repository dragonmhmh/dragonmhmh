# recherche du nombre de villes avec un pdc>10
import pandas
#ouverture du fichier csv
info_stations=pandas.read_csv('irve-tesla-supercharger-20181130.csv', sep=';')

nb_stat_pdc_sup_10 = ?
# on lit tous les pdc
for ligne in range(len(info_stations)):
    #lecture d'un pdc d'une ligne de la collection
    pdc = info_stations.loc[ligne,'nbre_pdc']
    # si pdc >= 10 alors on ajoute 1 au compteur de nbre de stations
    if ?:
        #on incrémente de 1 le compteur de stations
        nb_stat_pdc_sup_10 = ?
print(?)
