import time
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import pandas as pd

def Scrapper(args):
    for tick in range(1, len(args)):
        req = Request(
        url=f'https://sarmaaya.pk/ajax/widgets/all_financials.php?symbol={args[tick]}', 
        headers={'User-Agent': 'Mozilla/5.0'}
        )
        webpage = urlopen(req).read()
        soup = bs(webpage, 'html.parser')
        tables = soup.find_all('table')
        table_Col_rows = tables[0].findChildren(['tr'])
        cols = [th.text for th in table_Col_rows[0].findChildren(['th'])]

        idx = {}

        for k in range(0,len(tables)):
            td = tables[k].findChildren(['td'])
            for i in range(0,len(td) - 1,len(cols)):
                idx[td[i].text] = [0 if td[j].text == '-' else float(td[j].text.replace(",", ''))  for j in range(i+1, i+len(cols))]

        # print(idx)
        df = pd.DataFrame(idx)
        df = df.T
        df.columns =cols[1:]
        if df.iloc[1].cumsum().iloc[0] == 0:
            df = df.drop(df.columns[0], axis=1)
        df.to_excel(f'{args[tick]}.xlsx')
        delay = 5
        time.sleep(delay)






