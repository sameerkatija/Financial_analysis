# Financial Ratios Formulas
import pandas as pd


def SalesGrowth(lst):
    try:
        lst = lst.loc['SALES']
        one_year_cagr = round((((lst.iloc[0] / lst.iloc[1])**(1/1)) -1) * 100,2)
        five_year_cagr = round((((lst.iloc[0] / lst.iloc[4])**(1/5)) -1) * 100,2)
        status = 'Good' if one_year_cagr > 15 else ('Average' if one_year_cagr > 5 and one_year_cagr < 15 else 'BAD' )
        five_year_status = 'Good' if five_year_cagr > 15 else ('Average' if five_year_cagr > 5 and five_year_cagr < 15 else 'BAD' )
        ser = pd.Series([one_year_cagr, five_year_cagr,status,five_year_status], index=['1 Year Avg', '5 Year Avg', 'Status', '5 Year Status'], name = 'Sales Growth')
        return ser
    except:
        print('Something went wronge')

def OperatingProfitGrowth(lst):
    try:
        lst = lst.loc['EBIT']
        one_year_cagr = round((((lst.iloc[0] / lst.iloc[1])**(1/1)) -1) * 100,2)
        five_year_cagr = round((((lst.iloc[0] / lst.iloc[4])**(1/5)) -1) * 100,2)
        status = 'Good' if one_year_cagr > 15 else ('Average' if one_year_cagr > 5 and one_year_cagr < 15 else 'BAD' )
        five_year_status = 'Good' if five_year_cagr > 15 else ('Average' if five_year_cagr > 5 and five_year_cagr < 15 else 'BAD' )
        ser = pd.Series([one_year_cagr, five_year_cagr,status,five_year_status], index=['1 Year Avg', '5 Year Avg', 'Status', '5 Year Status'] , name = 'Operating Profit Growth')
        return ser
    except:
        print('Something went wronge')

def NetProfitGrowth(lst):
    try:
        lst = lst.loc['PAT']
        one_year_cagr = round((((lst.iloc[0] / lst.iloc[1])**(1/1)) -1) * 100,2)
        five_year_cagr = round((((lst.iloc[0] / lst.iloc[4])**(1/5)) -1) * 100,2)
        status = 'Good' if one_year_cagr > 15 else ('Average' if one_year_cagr > 5 and one_year_cagr < 15 else 'BAD' )
        five_year_status = 'Good' if five_year_cagr > 15 else ('Average' if five_year_cagr > 0 and five_year_cagr < 15 else 'BAD' )
        ser = pd.Series([one_year_cagr, five_year_cagr,status,five_year_status], index=['1 Year Avg', '5 Year Avg', 'Status', '5 Year Status'], 
        name = 'Net Profit Growth')
        return ser
    except:
        print('Something went wronge')

def EPSGrowth(lst):
    try:
        lst = lst.loc['EPS']
        three_year_avg = lst.iloc[:3].mean()
        five_year_avg = lst.iloc[:5].mean()
        status = 'Good' if three_year_avg > five_year_avg  else 'BAD'
        ser = pd.Series([three_year_avg, five_year_avg, status], index=['3 Year Avg', '5 Year Avg', 'Status'], name = 'EPS')
        return ser
    except:
        print('Something went wronge')
