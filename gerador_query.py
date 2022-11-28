nome_tabela = 'jogo'

colunas_tabela_lista = """NuRodada
NuJogo
DtJogo
CdEstadio
CdArbitro
CdBandeirinha1
CdBandeirinha2
CdEquipeCasa
CdEquipeVisitante
NuGolsCasa
NuGolsVisitante""".split()

colunas_tabela = ','.join(colunas_tabela_lista)

valores_lista = ['10', '4', '\'2022-08-07\'', '1', '1', '2', '3', '1', '2', '2', '4']

valores = ','.join(valores_lista)

print(f"""insert into {nome_tabela} ({colunas_tabela})
values({valores});""")