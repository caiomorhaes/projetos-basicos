from datetime import datetime
#artigos usados de base
artigos = [
{'titulo': 'Applications of Artificial Intelligence in Academic Libraries',
'autores': ['Vijayakumar, S.','Sheshadri,K.N.'],
'data_publicacao': '16/05/2019',
'consultas': 569},
{'titulo': 'Data science in data librarianship: Core competencies of a data librarian',
'autores': ['Semeler, A. R.','Pinto, A. L.','Rozados, H. B. F.'],
'data_publicacao': '26/11/2019',
'consultas': 1004},
{'titulo': 'Data scientist: the sexiest job of the 21st century',
'autores': ['Davenport,T.H.','Patil, D J'],
'data_publicacao': '01/10/2012',
'consultas': 10231},
{'titulo': 'Bibliometria: evolução histórica e questões atuais',
'autores': ['Araújo,C.A.A.'],
'data_publicacao': '10/12/2006',
'consultas': 650}
]

#separando do documento todas as datas desses artigos
#definindo uma key que pega a data de publicação e converte de string para datetime
def chave_data (artigo):
    data = artigo['data_publicacao']
    data_convertida = datetime.strptime (data, '%d/%m/%Y')
    return data_convertida
#agora com os dados de data em datetime, o sorted pode fazer o trabalho e comparar as datas
#entao na variavel, ela recebe o sorted do dicionario artigos usando a key do chave_data (transformar str de data em datetime)
artigos_ordenados = sorted (artigos, key= chave_data)
#printando para visualizar
for artigo in artigos_ordenados:
    print("Data:", artigo['data_publicacao'])
#printando desse jeito eu retiro a data de publicação que apareceria denovo 
    for chave, valor in artigo.items():
        if chave != 'data_publicacao':
            print(f"{chave}: {valor}")
    print("-" * 30)



