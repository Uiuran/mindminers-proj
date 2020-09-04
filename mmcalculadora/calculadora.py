import pandas as pd
import numpy as np

class IRCalculadora:

    def __init__(self, data_path):
        '''
        Calculadora de importo de renda para empresa Mind-Miners.
        
        Parametros:
          -dataset: deve ser caminho a um csv com dados relacionais de compra e venda, na
          Bolsa, com as seguintes features/amostra:

            - Data-da-Operação:  data no formato year-month-day.
            - Operação: Compra ou Venda.
            - Ação: nome das ações.
            - Preço: valor da ação no momento da operação.
            - Quantidade: quantidade de ações.
            - Taxa de corretagem: valor de corretagem
        '''
        self.data_path=data_path
        self._load_data()

    def __call__(self):
        self._validate_data()
        self._calculate()
        return self

    def load_dataset(self,path_dataset):
         self.data_path=path_dataset
         self._load_data()

    def _load_data(self):
        self.data = pd.read_csv(self.data_path)

    def _validate_data(self):
        '''
           Limpa NA (valores nulos) e converte as datas para o tipo correto (datetime)
        '''
        self.data['Data da operação']=pd.to_datetime(self.data['Data da operação'])
        if self.data.isna().sum().all == 0:
            pass
        else: 
            self.data.dropna(axis=0,how='any',inplace=True)

    def _calculate(self):
        '''
        Calcula o sumário mensal de operações em um DataFrame, acessável pelo atributo summary, com seguintes colunas:

        - mes, valor total compra, valor total venda, Imposto Devido, RAbr(Renda Absoluta Bruta), RAliq (Renda Absoluta Liquida), Prejuizo Absoluto
        
        '''
        QM = dict()
        PM = dict()
        RA = dict()
        RAm = dict()
        P = dict()
        IR = dict()
        result = pd.DataFrame(columns=['mes','valor total compra','valor total venda','Imposto Devido','RAbr','RAliq','Prejuizo Absoluto'])
        periodo = self.data['Data da operação'].dt.to_period("M") 

        for k,df in self.data.groupby(periodo):
            mes=k.__str__()
            QM[mes] = 0
            PM[mes] = 0
            RA[mes] = []
            RAm[mes] = 0
            P[mes] = 0
            IR[mes] = 0        
            total_compra=0
            total_venda=0
    
            for ind in df.index:                
                if df.loc[ind]['Operação'] == 'Compra':            
                    PM[mes]=(PM[mes]*QM[mes]+df.loc[ind]['Preço']*df.loc[ind]['Quantidade']+df.loc[ind]['Taxa de corretagem'])/(QM[mes]+df.loc[ind]['Quantidade'])
                    QM[mes]=QM[mes]+df.loc[ind]['Quantidade']
                    total_compra = total_compra + df.loc[ind]['Preço']*df.loc[ind]['Quantidade']
                elif df.loc[ind]['Operação'] == 'Venda':
                    RA[mes].append((df.loc[ind]['Data da operação'],(df.loc[ind]['Preço']-PM[mes])*df.loc[ind]['Quantidade']-df.loc[ind]['Taxa de corretagem']))
                    if RA[mes][-1][1] < 0:
                        P[mes] = P[mes]+RA[mes][-1][1]
                    else:
                        P[mes] = P[mes]-np.min([RA[mes][-1][1],P[mes]])
                    QM[mes]=QM[mes]-df.loc[ind]['Quantidade']
                    total_venda = total_venda + df.loc[ind]['Preço']*df.loc[ind]['Quantidade'] 

            RAm[mes] = np.sum([a[1] for a in RA[mes]])
            IR[mes] = (RAm[mes]-np.min([RAm[mes],P[mes]]))*0.15

            result=result.append({'mes':mes,
                             'valor total compra':total_compra,
                             'valor total venda':total_venda,
                             'Imposto Devido':IR[mes],
                             'RAbr':RAm[mes],
                             'RAliq':RAm[mes]-IR[mes],
                             'Prejuizo Absoluto':P[mes]},ignore_index=True)
        self.summary=result        

