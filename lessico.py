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
domande.append({"domanda": "melting down materials is cheaper than electrolysis", "risposta": "aluminium"})
domande.append({"domanda": "scarsity makes recycling desiderable. justify the cost of removing insulation from electric wires. Brass and bronze", "risposta": "copper"})
domande.append({"domanda": "sorting is critical, there are difference between clear and coloured materials used in bottles and jars", "risposta": "glass"})
domande.append({"domanda": "need to sort waste carefully, some types can be melted down, many cannot", "risposta": "plastic"})
domande.append({"domanda": "tyres are primary source of recyclabe material. Can be reused whole in certain application", "risposta": "rubber"})
domande.append({"domanda": "scrap can be sorted easily by magnetism. If the material is galvanised, the zin is fully recyclaible. Stainless steel can by recycled", "risposta": "steel"})
domande.append({"domanda": "hardwood and softwood can be reused but the process can be costly", "risposta": "timber"})
domande.append({"domanda": "a type of steel not needing a protective cloating and it doesn't rust", "risposta": "stainless steel"})
domande.append({"domanda": "metal used to make brass and galvanised coatting on steel", "risposta": "zinc"})
domande.append({"domanda": "predominant material in steel", "risposta": "iron"})
domande.append({"domanda": "alloy made from copper and thin", "risposta": "bronze"})
domande.append({"domanda": "dense and poisonous metal", "risposta": "lead"})
domande.append({"domanda": "rocks from which metal can be extracted", "risposta": "ore"})
domande.append({"domanda": "timber from pine", "risposta": "softwood"})
domande.append({"domanda": "timber from deciduous", "risposta": "hardwood"})
domande.append({"domanda": "combinations of materials (plurale)", "risposta": "compounds"})
domande.append({"domanda": "rare or complex", "risposta": "exotic"})
domande.append({"domanda": "iron and steel", "risposta": "ferrous"})
domande.append({"domanda": "minerals transformed by heat (plurale)", "risposta": "ceramics"})
domande.append({"domanda": "mixture of metals", "risposta": "alloy"})
domande.append({"domanda": "materials that are not metals", "risposta": "non-metallic"})
domande.append({"domanda": "plastic materials (plurale)", "risposta": "polymers"})
domande.append({"domanda": "pneumatic envelopes in contact with the road surface (plurale)", "risposta": "tyres"})
domande.append({"domanda": "pads pressed against discs to induce deceleration (plurale)", "risposta": "brake pads"})
domande.append({"domanda": "protective barriers capable of resisting gunshots", "risposta": "bullet-resistant armour"})
domande.append({"domanda": "flexible bands used in transmission systems (plurale)", "risposta": "drive belts"})
domande.append({"domanda": "sheets insterted between parts to prevent gas or fluid leakage (plurale)", "risposta": "sealing gaskets"})

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
