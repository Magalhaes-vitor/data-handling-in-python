import datetime
import pandas as pd

D1 = datetime.datetime.now() - datetime.timedelta(days=1)
Download = r'https://www4.bcb.gov.br/Download/fechamento' + '/' + D1.strftime("%Y%m%d") + '.csv'
read = pd.read_table(Download)
name_csv = 'Cotação Diaria ' + (datetime.datetime.now().strftime("%Y%m%d"))  + '.cvs'
read.to_csv(name_csv)

print(name_csv)