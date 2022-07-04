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
      # Una volta che abbiamo preso l'indice casuale, invertiamo l'elemento che stiamo analizzando alla posizione corrente (currentIndex) con quello alla posizione presa casualmente (randomIndex)
      # Variabile temporanea
      temporaryValue = array[currentIndex]
      # Eseguiamo lo scambio
      array[currentIndex] = array[randomIndex]
      array[randomIndex] = temporaryValue
    
    # Torniamo l'array mescolato a fine ciclo
    return array

domande = []
domande.append({"domanda": "Melting down materials is cheaper than electrolysis", "risposta": "aluminium"})
domande.append({"domanda": "Scarsity makes recycling desiderable. justify the cost of removing insulation from electric wires. Brass and bronze", "risposta": "copper"})
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

domande.append({"domanda": "Combinations of materials (plurale)", "risposta": "compounds"})
domande.append({"domanda": "Rare or complex", "risposta": "exotic"})
domande.append({"domanda": "Iron and steel", "risposta": "ferrous"})
domande.append({"domanda": "Minerals transformed by heat (plurale)", "risposta": "ceramics"})
domande.append({"domanda": "Mixture of metals", "risposta": "alloy"})
domande.append({"domanda": "Materials that are not metals", "risposta": "non-metallic"})
domande.append({"domanda": "Plastic materials (plurale)", "risposta": "polymers"})
# WEEK 3
domande.append({"domanda": "Pneumatic envelopes in contact with the road surface (plurale)", "risposta": "tyres"})
domande.append({"domanda": "Pads pressed against discs to induce deceleration (plurale)", "risposta": "brake pads"})
domande.append({"domanda": "Protective barriers capable of resisting gunshots", "risposta": "bullet-resistant armour"})
domande.append({"domanda": "Flexible bands used in transmission systems (plurale)", "risposta": "drive belts"})
domande.append({"domanda": "Sheets insterted between parts to prevent gas or fluid leakage (plurale)", "risposta": "sealing gaskets"})
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
