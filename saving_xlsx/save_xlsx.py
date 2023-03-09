import datetime
import pandas as pd

D1 = datetime.datetime.now() - datetime.timedelta(days=1)
Download = r'https://www4.bcb.gov.br/Download/fechamento' + '/' + D1.strftime("%Y%m%d") + '.csv'
read = pd.read_table(Download, sep=';', names=['Cod Moeda','Tipo','Moeda','Taxa Compra','Taxa Venda','Paridade Compra','Paridade Venda'])
name_file = 'Cotação Diaria ' + (datetime.datetime.now().strftime("%Y%m%d"))  + '.xlsx'
read.to_excel(name_file, index=False)

print(name_file)
