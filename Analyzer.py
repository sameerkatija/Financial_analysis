import pandas as pd
from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.cell.cell import WriteOnlyCell
from openpyxl.utils.dataframe import dataframe_to_rows
from itertools import islice
from GrowthRatios import *
from StabilityRatios import * 
from ValuationRations import *
from InventoryRatios import *
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import sys


def SharePrice(name):
        try:
            req = Request(
            url=f'https://dps.psx.com.pk/company/{name}', 
            headers={'User-Agent': 'Mozilla/5.0'}
            )
            webpage = urlopen(req).read()
            soup = bs(webpage, 'html.parser')
            divs = soup.find_all('div', {"class": 'quote__close'})
            sharePrice = divs[0].text.replace('Rs.' , '')
            sharePrice = float(sharePrice.replace(',' , ''))
            return sharePrice
        except:
            print('Something went wronge in Share Price')

def Analzer(args):
    for i in range(1, len(args)):
        # Path to the file
        file_path = f'{args[i]}.xlsx'

        # import excel file
        dataFile = load_workbook(file_path)

        # Object of the sheet 
        dataSheet = dataFile.active

        dataFrame = dataSheet.values
        

        # print(dataFrame)
        cols = next(dataFrame)[1:]
        dataFrame = list(dataFrame)
        idx = [r[0] for r in dataFrame]
        dataFrame = (islice(r, 1, None) for r in dataFrame)
        df = pd.DataFrame(dataFrame, index=idx, columns=cols)
        sharePrice = SharePrice(args[i])
        PEV = PERatio(sharePrice, df)
        PBV = PriceToBookValue(sharePrice, df)
        new_df = pd.concat({
            "Sales Growth": SalesGrowth(df),
            "EPS": EPSGrowth(df),
            "Net Profit Growth": NetProfitGrowth(df),
            "Operating Profit Growth": OperatingProfitGrowth(df),
            "OPM": OPM(df),
            "NPM": NPM(df),
            "Tax Ratio": TaxRatio(df),
            "Interest Coverage":InterestCoverage(df),
            "Total Debt": TotalDebt(df),
            "Debt To Equity": DebtToEquity(df),
            "Current Ratio":CurrentRatio(df),
            "Cash Flow From Operating Activities": CFO(df),
            "Net Change in Cash": NetCash(df),
            "cCFO vs cPAT": CCFOVSPAT(df),
            "Net Asset Turnover":NetAssetTurnover(df), 
            "Return on Equity": ReturnOnEquity(df),
            "PE RATIO" : PEV,
            "PEG Ratio": PEGRatio(PEV,df),
            "Earning Yield": EarningYield(PEV),
            "PRICE TO BOOK VALUE": PBV,
            "Graham Formula": GrahamFormula(PEV , PBV),
            "Price To Sale Ratio": PriceToSaleRatio(sharePrice,df),
            "Dividend Yield": DividendYield(sharePrice,df),
            "EV OVER EBITDA": EVOVEREBITDA(sharePrice, df),
            "Inventory TurnOver Rate" :InventoryTurnOver(df) ,
            "Days Receivable Outstanding" : DaysReceivableOutstanding(df),
            "Days Sales of Inventory" : DaysSalesofInventory(df),
            "Days Payable Outstanding": DaysPayableOutstanding(df),
            "Cash Conversion Cycle": CashConversionCycle(df)
            
        }, axis=1).reset_index()
        Ratio = pd.DataFrame(new_df).set_index('index')
        Ratio.index.name = 'Ratios'
        Ratio.T.to_excel(f'{args[i]}_analyzed.xlsx')
        # print(Ratio.T)
