from random import random

def mescola(array): 
    # Ci prendiamo la lunghezza dell'array e partiamo dal fondo!
    currentIndex = len(array)
    # Finche' ci sono elementi da mescolare, iteriamo l'array
    while 0 != currentIndex:
      # Prendiamo un indice a caso dell'array, purche' sia compreso tra 0 e la lunghezza dell'array
      randomIndex = int(random() * currentIndex)
      # Riduciamo di un'unita' l'indice corrente
      currentIndex -= 1
      # Una volta che abbiamo preso l'indice casuale, invertiamo l'elemento che stiamo analizzando alla posizione corrente (currentIndex) con quello alla posizione 
      # presa casualmente (randomIndex)
      # Variabile temporanea
      temporaryValue = array[currentIndex]
      # Eseguiamo lo scambio
      array[currentIndex] = array[randomIndex]
      array[randomIndex] = temporaryValue
    
    # Torniamo l'array mescolato a fine ciclo
    return array

domande = []

# WEEK 2
domande.append({"domanda": "Melting down materials is cheaper than electrolysis", "risposta": "aluminium"})
domande.append({"domanda": "Scarsity makes recycling desiderable. Justify the cost of removing insulation from electric wires. Brass and bronze", "risposta": "copper"})
domande.append({"domanda": "Sorting is critical, there are difference between clear and coloured materials used in bottles and jars", "risposta": "glass"})
domande.append({"domanda": "Need to sort waste carefully, some types can be melted down, many cannot", "risposta": "plastic"})
domande.append({"domanda": "Tyres are primary source of recyclabe material. Can be reused whole in certain application", "risposta": "rubber"})
domande.append({"domanda": "Scrap can be sorted easily by magnetism. If the material is galvanised, the zin is fully recyclaible. Stainless steel can by recycled", "risposta": "steel"})
domande.append({"domanda": "Hardwood and softwood can be reused but the process can be costly", "risposta": "timber"})

domande.append({"domanda": "A type of steel not needing a protective cloating and it doesn't rust", "risposta": "stainless steel"})
domande.append({"domanda": "Metal used to make brass and galvanised coatting on steel", "risposta": "zinc"})
domande.append({"domanda": "Predominant material in steel", "risposta": "iron"})
domande.append({"domanda": "Alloy made from copper and thin", "risposta": "bronze"})
domande.append({"domanda": "Dense and poisonous metal", "risposta": "lead"})
domande.append({"domanda": "Rocks from which metal can be extracted", "risposta": "ore"})
domande.append({"domanda": "Timber from pine", "risposta": "softwood"})
domande.append({"domanda": "Timber from deciduous", "risposta": "hardwood"})

domande.append({"domanda": "Combinations of materials", "risposta": "compounds"})
domande.append({"domanda": "Rare or complex", "risposta": "exotic"})
domande.append({"domanda": "Iron and steel", "risposta": "ferrous"})
domande.append({"domanda": "Minerals transformed by heat", "risposta": "ceramics"})
domande.append({"domanda": "Mixture of metals", "risposta": "alloy"})
domande.append({"domanda": "Materials that are not metals", "risposta": "non-metallic"})
domande.append({"domanda": "Plastic materials", "risposta": "polymers"})

# WEEK 3
domande.append({"domanda": "Pneumatic envelopes in contact with the road surface", "risposta": "tyres"})
domande.append({"domanda": "Pads pressed against discs to induce deceleration", "risposta": "brake pads"})
domande.append({"domanda": "Protective barriers capable of resisting gunshots", "risposta": "bullet-resistant armour"})
domande.append({"domanda": "Flexible bands used in transmission systems", "risposta": "drive belts"})
domande.append({"domanda": "Sheets insterted between parts to prevent gas or fluid leakage", "risposta": "sealing gaskets"})

# WEEK 4
domande.append({"domanda": "Removal of material across the full diametre of a hole or using hole-saws fur cutting circumferential kerfs", "risposta": "drilling"})
domande.append({"domanda": "Using oxy fuel (oxygen + combustible gas)", "risposta": "flame-cutting"})
domande.append({"domanda": "Removal of surface layers with multiple cutting wheel passes", "risposta": "milling"})
domande.append({"domanda": "Abrasive cutting removing a kerf of material. Include cutting with toothed blade", "risposta": "sawing"})
domande.append({"domanda": "Makes holes by applying pressure to shear the material", "risposta": "punch"})

domande.append({"domanda": "Cuts a circular piece to remove an intact core of material", "risposta": "hole saw"})
domande.append({"domanda": "Makes straight cuts by applying pressure to shear the material", "risposta": "guillotine"})
domande.append({"domanda": "Has a sharp edges for cutting or milling", "risposta": "toothed blade"})
domande.append({"domanda": "Width of the saw cut", "risposta": "kerf"})
domande.append({"domanda": "Has a hard, rough surface for cutting or grinding", "risposta": "abrasive wheel"})

# WEEK 5
domande.append({"domanda": "Gives a cutaway view of the joint between two panels", "risposta": "cross section"})
domande.append({"domanda": "Gives a view of the whole deck from above", "risposta": "plan"})
domande.append({"domanda": "Gives a simplified representation of a network of air ducts", "risposta": "schematic"})
domande.append({"domanda": "Gives a brief description or a reference to another related drawing", "risposta": "Note"})
domande.append({"domanda": "Gives a view of all the panels from the front", "risposta": "elevation"})
domande.append({"domanda": "Gives a deconstructed view of how the panels are fixed", "risposta": "exploded view"})
domande.append({"domanda": "Gives a detailed written technical description of the panels", "risposta": "specification"})

# WEEK 7
domande.append({"domanda": "Lift / make something go up", "risposta": "raise"})
domande.append({"domanda": "Joining", "risposta": "connecting"})
domande.append({"domanda": "Carried (objects, over a distance)", "risposta": "transported"})
domande.append({"domanda": "Hold something firmly / bear its weight", "risposta": "support"})
domande.append({"domanda": "Fixed", "risposta": "attached"})
domande.append({"domanda": "Climb up", "risposta": "ascend"})
domande.append({"domanda": "Climb down", "risposta": "descend"})
domande.append({"domanda": "Provided with energy / moved by a force", "risposta": "powered"})
domande.append({"domanda": "Driven / have movement directed", "risposta": "controlled"})

domande.append({"domanda": "Standard, usual", "risposta": "conventional"})
domande.append({"domanda": "gets rid of", "risposta": "eliminates"})
domande.append({"domanda": "Better / the best", "risposta": "superior"})
domande.append({"domanda": "Has a low energy consumption", "risposta": "energy-efficient"})
domande.append({"domanda": "Improved", "risposta": "enhanced"})
domande.append({"domanda": "Decreases", "risposta": "reduces"})



domande = mescola(domande)
length = len(domande)
giuste = 0
for domanda in domande:
    print(domanda["domanda"]+": ")
    inserito = input()
    # inserito = input(domanda["domanda"]+": ")
    if inserito == domanda["risposta"]:
        giuste = giuste+1
    else:
        print("la risposta era: ", domanda["risposta"])

print("hai fatto: ",giuste, "/", length, " risposte corrette")
