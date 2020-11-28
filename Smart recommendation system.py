
from tkinter import *              #impoter la bibliotheque de céation des interfaces sous python
from tkinter.ttk import Combobox   #pour creer les combobox
import webbrowser                  #pour ouvrir un browser

#la méthode qui decrit la fonctionnemet de l'interface
def open_web():
    #lien entre l'interface et la sortie
    select1 = combo1.get()
    select2 = combo2.get()

    #Choix de la collection et la méthode de recommandation
    if select1 == list1[0] and select2 == list2[0]:
        webbrowser.open_new("https://colab.research.google.com/drive/1wt39sr3PvYRsrOFc2KKJKNh7FoO8ekmp#scrollTo=IbfKZXLW5oxG")
    elif select1 == list1[1] and select2 == list2[0]:
        webbrowser.open_new("https://colab.research.google.com/drive/1c7Waq3ddNliVV__rzGob_iAwhKQpbD3Z#scrollTo=8sZNZOzik4AF")
    elif select1 == list1[2] and select2 == list2[0]:
        webbrowser.open_new("https://colab.research.google.com/drive/19zzr0shMplvKdRcE2MQICTT9CTCrlHCs#scrollTo=5LNng_I-bHWb")
    elif select1 == list1[3] and select2 == list2[0]:
        webbrowser.open_new("https://colab.research.google.com/drive/177VSfFiNb66PYWRnxP23UeOUmZOF3Cl6#scrollTo=qgsNMdhuogO1")
    elif select1 == list1[0] and select2 == list2[1]:
        webbrowser.open_new("https://colab.research.google.com/drive/1Hus_iTmHNOjgd6JmVua1iqnFuMd4eVSi#scrollTo=KTXS2Jcy1lBh")
    elif select1 == list1[1] and select2 == list2[1]:
        webbrowser.open_new("https://colab.research.google.com/drive/1ErOaDT_-xTn3-1YASZA-nRRnzy9NPvAu#scrollTo=CN2ZnrwVWKBf")
    elif select1 == list1[2] and select2 == list2[1]:
        webbrowser.open_new("https://colab.research.google.com/drive/1fzH6BW1HEtbfkcUtofJVqPpfNED24HsH#scrollTo=vTU6MgMTRn0p")
    elif select1 == list1[3] and select2 == list2[1]:
        webbrowser.open_new("https://colab.research.google.com/drive/1Ti67NEblKItr-KEEVI8dHwxfi2Y9yXeh#scrollTo=Sraxgm4YRczT")
    elif select1 == list1[0] and select2 == list2[2]:
        webbrowser.open_new("https://colab.research.google.com/drive/1AL7BWvYA_VPC-L-h_IIuj9kgbTCXPWe-#scrollTo=2M_jiW2ukMJq")
    elif select1 == list1[1] and select2 == list2[2]:
        webbrowser.open_new("https://colab.research.google.com/drive/14au8wyQ3LEtx92dgc1vEQQmn4j2EJ0cw#scrollTo=9gSNqgWODKWD")
    elif select1 == list1[2] and select2 == list2[2]:
        webbrowser.open_new("https://colab.research.google.com/drive/14ouNuTAeh_w2u10WAreFi107ERtLX9FN#scrollTo=jnnDibviv_UB")
    elif select1 == list1[3] and select2 == list2[2]:
        webbrowser.open_new("https://colab.research.google.com/drive/1ZVENY5D6uT-Tbi4tShsbMcFA5q5-xGrL#scrollTo=IbEjMX4v3b8f")

    else:
        print('error')  #sinon une erreur qui s'affiche


window = Tk()                                #creer une fenetre
window.title("Smart recommendation system")  #le titre de fenetre
window.config(background="#cd5b45")          #couleur de l'interface
title = Label(window, text='Recommendation System', font=("Arial", 40), bg="#cd5b45", fg='white')  #creer une label dans la fenetre
title.pack(expand='yes')

#creer une deuxiéme label dans la fenetre
sous_title1 = Label(window, text='Choose The Method of Recommendation', font=("Arial", 25), bg="#cd5b45", fg='white')
sous_title1.pack(expand='yes')

#creer une liste de methode de recommandation
list1 = list(["Matrix Factorization", "Matrix Factorization with bias", "Deep Matrix Factorization", "Neural collaboratif filtring"])

#creer un combobox pour les méthodes de recommandation
combo1 = Combobox(window, values=list1)
combo1.set("Method of Recommendation system")
combo1.pack()

#creer une autre label pour choisir la collection de données
sous_title1 = Label(window, text='Choose The Collection', font=("Arial", 25), bg="#cd5b45", fg='white')
sous_title1.pack(expand='yes')

#creer une deuxiéme liste pour les collections
list2 = list(["MovieLens", "Epinion", "Netflix"])

#creer un combobox pour les collections
combo2 = Combobox(window, values=list2)
combo2.set("The Collection")
combo2.pack()

#lien entre l'nterface crée (partie graphique) et sa fonctionnement (dans la methode "open web")
combo1.bind("<<comboboxSelected>>", open_web)
combo2.bind("<<comboboxSelected>>", open_web)
frame = Frame(window, bg='#8d8d82')

#Aller vers la méthode "open web"
button = Button(frame, text='Result', font=("Arial", 25), bg='#8b8378', fg='white', command=open_web)
button.pack()
frame.pack(expand='yes')

#Affichage de l'interface
window.mainloop()
