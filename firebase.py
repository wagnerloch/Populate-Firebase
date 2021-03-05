import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate(
    'credentials.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

#Abre arquivo com os códigos a serem inseridos
f = open('codes.txt', 'r')

vetor = []

#Adiciona os códigos num vetor
#Esta parte é opcional, apenas para ter um controle de quantos % já foram inseridos
for line in f:
    numero = line.splitlines()[0]
    vetor.append(numero)

#Exibe a quantidade de dados
print(len(vetor))

i = 0

#Percorre o vetor inserindo no Firebase e exibindo o progresso atual
for cnh in vetor:
    cnh_atual = db.collection('cnhs').document(cnh)
    cnh_atual.set({
        'cnh': cnh
    })
    print((100*i)/len(vetor))
    i = i+1
