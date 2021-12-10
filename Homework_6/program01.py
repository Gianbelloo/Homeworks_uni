# -*- coding: utf-8 -*-
''' 
Il sindaco si una città deve pianificare un nuovo quartiere.  Voi fate
parte dello studio di architetti che deve progettare il quartiere.  Vi
viene fornito un file che contiene divisi in righe, le informazioni
che descrivono in pianta le fasce East-West (E-W) di palazzi, ciascuno
descritto da larghezza, altezza, colore da usare in pianta.

I palazzi devono essere disposti in pianta rettangolare
in modo che:
  - tutto intorno al quartiere ci sia una strada di larghezza minima
    indicata.
  - in direzione E-W (orizzontale) ci siano le strade principali,
    dritte e della stessa larghezza minima, a separare una fascia di
    palazzi E-W dalla successiva.  Ciascuna fascia E-W di palazzi può
    contenere un numero variabile di palazzi.  Se una fascia contiene
    un solo palazzo verrà disposto al centro della fascia.
  - in direzione North-South (N-S), tra ciascuna coppia di palazzi
    consecutivi, ci dev'essere almeno lo spazio per una strada
    secondaria, della stessa larghezza minima delle altre.

Vi viene chiesto di calcolare la dimensione minima dell'appezzamento
che conterrà i palazzi.  Ed inoltre di costruire la mappa che li
mostra in pianta.

Il vostro studio di architetti ha deciso di disporre i palazzi in modo
che siano **equispaziati** in direzione E-W, e di fare in modo che
ciascuna fascia E-W di palazzi sia distante dalla seguente dello
spazio minimo necessario alle strade principali.

Per rendere il quartiere più vario, il vostro studio ha deciso che i
palazzi, invece di essere allineati con il bordo delle strade
principali, devono avere se possibile un giardino davanti (a S) ed uno
dietro (a N) di uguale profondità.  Allo stesso modo, dove possibile,
lo spazio tra le strade secondarie ed i palazzi deve essere
distribuito uniformemente in modo che tutti possano avere un giardino
ad E ed uno a W di uguali dimensioni.  Solo i palazzi che si
affacciano sulle strade sul lato sinistro e destro della mappa non
hanno giardino su quel lato.

Vi viene fornito un file txt che contiene i dati che indicano quali
palazzi mettere in mappa.  Il file contiene su ciascuna riga, seguiti
da 1 virgola e/o 0 o più spazi o tab, gruppi di 5 valori interi che
rappresentano per ciascun palazzo:
  - larghezza
  - altezza
  - canale R del colore
  - canale G del colore
  - canale B del colore

Ciascuna riga contiene almeno un gruppo di 5 interi positivi relativi
ad un palazzo da disegnare. Per ciascun palazzo dovete disegnare un
rettangolo del colore indicato e di dimensioni indicate

Realizzate la funzione ex(file_dati, file_png, spaziatura) che:
  - legge i dati dal file file_dati
  - costruisce una immagine in formato PNG della mappa e la salva nel
    file file_png
  - ritorna le dimensioni larghezza,altezza dell'immagine della mappa

La mappa deve avere sfondo nero e visualizzare tutti i palazzi come segue:
  - l'argomento spaziatura indica il numero di pixel da usare per lo
    spazio necessario alle strade esterne, principali e secondarie,
    ovvero la spaziatura minima in orizzontale tra i rettangoli ed in
    verticale tra le righe di palazzi
  - ciascun palazzo è rappresentato da un rettangolo descritto da una
    quintupla del file
  - i palazzi descritti su ciascuna riga del file devono essere
    disegnati, centrati verticalmente, su una fascia in direzione
    E-W della mappa
  - i palazzi della stessa fascia devono essere equidistanti
    orizzontalmente l'uno dall'altro con una **distanza minima di
    'spaziatura' pixel tra un palazzo ed il seguente** in modo che tutti
    i primi palazzi si trovino sul bordo della strada verticale di
    sinistra e tutti gli ultimi palazzi di trovino sul bordo della
    strada di destra
    NOTA se la fascia contiene un solo palazzo dovrà essere disegnato
    centrato in orizzontale
  - ciascuna fascia di palazzi si trova ad una distanza minima in
    verticale dalla seguente per far spazio alla strada principale
    NOTE la distanza in verticale va calcolata tra i due palazzi più
    alti delle due fasce consecutive. 
    Il palazzo più grosso della prima riga si trova appoggiato al
    bordo della strada principale E-W superiore. 
    Il palazzo più grosso dell'ultima riga si trova appoggiato al
    bordo della strada principale E-W inferiore 
  - l'immagine ha le dimensioni minime possibili, quindi:
     - esiste almeno un palazzo della prima/ultima fascia a
       'spaziatura' pixel dal bordo superiore/inferiore
     - esiste almeno una fascia che ha il primo ed ultimo palazzo a
       'spaziatura' pixel dal bordo sinistro/destro
     - esiste almeno una fascia che non ha giardini ad E ed O

    NOTA: nel disegnare i palazzi potete assumere che le coordinate
        saranno sempre intere (se non lo sono avete fatto un errore).
    NOTA: Larghezza e altezza dei rettangoli sono tutti multipli di due.
'''
import images

def ex(file_dati, file_png, spaziatura):
    with open(file_dati, encoding = "utf8") as f:
        dati = f.read()
    
    dati_quintuple = []
    dati = "".join([c if c.isdigit() or c == "\n" else ' ' for c in dati]) #leva le cose che non servono
    dati_puliti = dati.splitlines()#divide in righe
    
    def gestione_dati(dati):
        for i in range(len(dati_puliti)):
            dati_puliti[i] = dati_puliti[i].split()
            dati_puliti[i] = [int(numero) for numero in dati_puliti[i]]
            dati_quintuple.append(elabora_quintuple(dati_puliti[i]))
        return dati_quintuple
    
    def elabora_quintuple(dati_puliti):#serve ad ottenere le quintuple
        riga_quintupla = []
        for i in range(0,len(dati_puliti),5):
            riga_quintupla.append(dati_puliti[i:i+5])
        return riga_quintupla
            
    def calcola_dimensioni(dati,spaziatura):
        dati_elaborati = gestione_dati(dati)
        larghezze_totali = []
        altezze_totali = [spaziatura]
        for i in range(len(dati_elaborati)):
            somma_larghezze = [spaziatura]#temporanei sulla riga
            altezze_riga = []#temporaneo sulla riga
            for b,palazzo in enumerate(dati_elaborati[i]):
                somma_larghezze.append(palazzo[0]+spaziatura)
                altezze_riga.append(palazzo[1])
            altezze_totali.append(max(altezze_riga)+spaziatura)
            larghezze_totali.append(sum(somma_larghezze))
        larghezza_immagine = max(larghezze_totali)
        altezza_immagine = sum(altezze_totali)
        return larghezza_immagine,altezza_immagine,altezze_totali,dati_elaborati
    
    def immagine(altezza_larghezza):
        larghezza = altezza_larghezza[0]
        altezza = altezza_larghezza[1]
        immagine_nera = [[(0,0,0)] *larghezza for _ in range(altezza)]
        return immagine_nera
    
    def funzione_principale(largh_alt_list_quint,spaziatura):
        imm_sfondo = immagine(largh_alt_list_quint[:2])
        larghezza_sfondo = largh_alt_list_quint[0]
        lista_altezze = largh_alt_list_quint[2]
        lista_altezze.pop(0)
        quintuple = largh_alt_list_quint[3]
        centro_orizzontale = spaziatura # centro sta al bordo
        for riga in range(len(quintuple)):#prendo ogni riga                
            centro_verticale = spaziatura
            centro_orizzontale += (lista_altezze[riga]-spaziatura)/2
            if len(quintuple[riga]) > 1:
                distanziamento = funz_distanziamento(larghezza_sfondo,spaziatura,quintuple[riga])
                for b,palazzo in enumerate(quintuple[riga]):
                    colore = palazzo[2:]
                    centro_verticale += palazzo[0]/2
                    x1 = int(centro_verticale-palazzo[0]/2)
                    x2 = int(centro_verticale+palazzo[0]/2)
                    y1 = int(centro_orizzontale-palazzo[1]/2)
                    y2 = int(centro_orizzontale+palazzo[1]/2)
                    disegna_rettangolo(imm_sfondo, x1,y1, x2,y2, colore)
                    centro_verticale += palazzo[0]/2 + distanziamento
            else:
                singolo_palazzo(quintuple[riga][0],larghezza_sfondo,centro_orizzontale,imm_sfondo)
            centro_orizzontale += (lista_altezze[riga]-spaziatura)/2+spaziatura
        return imm_sfondo
    
    def disegna_rettangolo(img, x1,y1, x2,y2, colore):#x1 y1 angolo in alto sinistro, x2y2 angolo in basso destro
            for x in range(x1, x2):
                for y in range(y1, y2):
                        img[y][x] = colore
    
    def funz_distanziamento(larghezza_sfondo,spaziatura,riga):
        tot_larg_palazzi = 0
        for i,palazzo in enumerate(riga):
            tot_larg_palazzi += palazzo[0]
        distanziamento = (larghezza_sfondo-(2*spaziatura)-tot_larg_palazzi)/(len(riga)-1)
        return distanziamento
    
    def singolo_palazzo(palazzo,larghezza_sfondo,centro_orizzontale,imm_sfondo):
        colore = palazzo[2:]
        centro_singolo = 0
        centro_singolo = larghezza_sfondo/2
        x1 = int(centro_singolo-palazzo[0]/2)
        x2 = int(centro_singolo+palazzo[0]/2)
        y1 = int(centro_orizzontale-palazzo[1]/2)
        y2 = int(centro_orizzontale+palazzo[1]/2)
        disegna_rettangolo(imm_sfondo, x1,y1, x2,y2, colore)
        
    largh_alt_list_quint = calcola_dimensioni(dati_puliti,int(spaziatura))
    immagine_finale = funzione_principale(largh_alt_list_quint,int(spaziatura))
    images.save(immagine_finale,file_png)
    return largh_alt_list_quint[:2]
    # inserisci qui il tuo codice
    pass

if __name__ == '__main__':
    # inserisci qui i tuoi test personali per debuggare
    pass
