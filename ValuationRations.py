import pandas as pd
from numpy import mean


def PERatio(sharePrice, lst):
    try:
        EPS = lst.loc['EPS']
        pe_ratio = round(sharePrice/EPS[0],2)
        status = 'GOOD' if pe_ratio < 10 else ('AVG' if pe_ratio > 10 and pe_ratio < 15 else 'BAD' )
        ser = pd.Series([pe_ratio, status], index=['Ratio', 'Status'], name = 'PE Ratio')
        return ser
    except:
        print('Something went wronge in P/E Ratio')
    
def PEGRatio(PEV, lst):
    try:     
        AverageGrowth = []
        # EBITDA = lst
        EBITDA = lst.loc['EBITDA']
        for i in range(0, len(EBITDA) - 1):
            CAGR = (((EBITDA[i] / EBITDA[i+1]) ** (1)) - 1) * 100
            AverageGrowth.append(round(CAGR,1))
        
        PEG = round(PEV.loc['Ratio'] / round(mean(AverageGrowth),1),2)
        status = 'GOOD' if PEG <= 1 else 'BAD'
        ser = pd.Series([PEG, status], index=['Ratio', 'Status'], name = 'PEG Ratio')
        return ser
    except:
        print('Something went wronge in PEG Ratio')  


def EarningYield(PEV):
    try:
        earningYield =  round((1 / PEV.loc['Ratio']) * 100,2)
        status = 'GOOD' if earningYield > 12 else 'BAD'
        ser = pd.Series([earningYield, status], index=['Ratio', 'Status'], name = 'Earning Yield')
        return ser
    except:
        print('Something went wronge in Earning Yield')

def PriceToBookValue(SharePrice, lst):
    try:
        ShareholderEquity =  lst.loc['Shareholder Equity']
        NumberofShares = lst.loc['Number of Shares']
        BV = ShareholderEquity/NumberofShares
        PBV = round(SharePrice / BV.iloc[0],2)
        status = 'GOOD' if PBV <= 1.5 else 'BAD'
        ser = pd.Series([PBV, status], index=['Ratio', 'Status'], name = 'Price To Book Value')
        return ser
    except:
        print('Something went wronge in Price To Book Value')

def GrahamFormula(PEV , PBV):
    try:
        grahamValue = round(PEV.loc['Ratio'] * PBV.loc['Ratio'],2)
        status = 'GOOD' if grahamValue < 22.5 else 'BAD'
        ser = pd.Series([grahamValue, status], index=['Ratio', 'Status'], name = 'Graham Formula')
        return ser
    except:
        print('Something Went Wrong in GrahamFormula')

def PriceToSaleRatio(sharePrice, lst):
    try:
        salesPerShare = lst.loc['Sales'] / lst.loc['Number of Shares']
        priceToSaleRatio = round(sharePrice / salesPerShare.iloc[0],2)
        status = 'GOOD' if priceToSaleRatio <= 1.5 else ('AVG' if priceToSaleRatio > 1.5 and priceToSaleRatio < 3 else 'BAD' )
        ser = pd.Series([priceToSaleRatio, status], index=['Ratio', 'Status'], name = 'Price To Sale Ratio')
        return ser
    except:
        print('Something Went Wrong in Price to Sale Ratio')

def DividendYield(sharePrice,lst):
    try:
        if lst.loc['Annual Dividend per Share'].iloc[0] > 0:
            dividendYield =  round((lst.loc['Annual Dividend per Share'].iloc[0] / sharePrice) * 100,2)
        else: 
            dividendYield = 0
        status = 'GOOD' if dividendYield >= 4 else 'BAD' 
        ser = pd.Series([dividendYield, status], index=['Ratio', 'Status'], name = 'Dividend Yield')
        return ser
    except:
        print('Something Went Wrong in Dividend Yield')


def EVOVEREBITDA(sharePrice, lst):
    # try:
        MarketCap = lst.loc['Number of Shares'] * sharePrice
        LTDebt = lst.loc['Interest Bearing Long Term Liability'].fillna(0)
        LTCapitalLeases= lst.loc['Non Interest Bearing Long Term Liability'].fillna(0)
        STDebt = lst.loc['Interest Bearing Short Term Liability'].fillna(0)
        STCapitalLeases = lst.loc['* Non Interest Bearing Short Term Liability'].fillna(0)
        totalDebt = STDebt + STCapitalLeases + LTDebt + LTCapitalLeases
        netChange = lst.loc['Cash in Hand and Bank'].fillna(0)
        EV = MarketCap + totalDebt - netChange
        eVOVEREBITDA = round((EV/lst.loc['EBITDA']).iloc[0],2)
        status = 'GOOD' if eVOVEREBITDA < 10 else 'BAD' 
        ser = pd.Series([eVOVEREBITDA, status], index=['Ratio', 'Status'], name = 'EV OVER EBITDA')
        return ser
    # except:
    #     print('Something Went Wrong in EV OVER EBITDA')

