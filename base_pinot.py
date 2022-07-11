import pandas as pd

pinot_read = pd.read_csv('analise_jucema/dados_jucema/pinot_ativos.csv', 
                        names=['bairro_empresa', 'cnpj','codigo_atividade', 'descricao_atividade', 'extincao_empresa', 'filial', 'inicio_atividades', 
                        'municipio_empresa', 'natureza', 'porte', 'razao_social', 'NIRE', 'secao_atividade', 'setor', 'situacao_siarco', 
                        'status_siarco', 'termino_atividades', 'uf_empresa', 'uf_junta'], 
                        encoding= 'latin-1', delimiter= ',')
df_pinot = pinot_read.drop(index=0, axis=0)

porte = df_pinot['porte']
qtd_porte = porte.value_counts()
 
cnpj = df_pinot['cnpj']
cnpj_bs_dpc = cnpj.value_counts()
cnpj_dpc = cnpj_bs_dpc.value_counts()
exp_cnpj_dpc = cnpj_bs_dpc.drop_duplicates()

nire = df_pinot['NIRE']
nire_bs_dpc = nire.value_counts()
nire_dpc = nire_bs_dpc.value_counts()
exp_nire_dpc = nire_bs_dpc.drop_duplicates()                #EXEMPLOS DE DUPLICADOS


print(qtd_porte)                                      #CONTA AS EMPRESAS ATIVAS POR PORTE
# print(cnpj_bs_dpc.head(965))                          
# print(cnpj_bs_dpc)
# print(cnpj_dpc)                                         #1974 valoes dplicados
# print('')
# print(nire_bs_dpc)
# print(nire_dpc)
# print(nire_bs_dpc.head(500))
print()














#'bairro_empresa', 'cnpj','codigo_atividade', 'descricao_atividade', 'extincao_empresa', 'filial', 'inicio_atividades', 
#'municipio_empresa', 'natureza', 'porte', 'razao_social', 'registro_siarco', 'secao_atividade', 'setor', 'situacao_siarco', 
#'status_siarco', 'termino_atividades', 'uf_empresa', 'uf_junta'