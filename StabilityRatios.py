import pandas as pd
def NPM(lst):
    try:
        SALES = lst.loc['SALES']
        PAT = lst.loc['PAT']
        lst = ((PAT/SALES) * 100).round(2)
        three_year_avg = round(lst.iloc[:3].mean(),2)
        five_year_avg = round(lst.iloc[:5].mean(),2)
        one_year_cagr = lst.iloc[0]
        status = 'Good' if one_year_cagr > 8 else ('Average' if one_year_cagr > 3 and one_year_cagr < 8 else 'BAD' )
        five_year_status = 'Good' if five_year_avg > 8 else ('Average' if five_year_avg > 3 and five_year_avg < 8 else 'BAD' )
        ser = pd.Series([one_year_cagr,three_year_avg, five_year_avg,status,five_year_status], index=['1 Year Avg','3 Year Avg', '5 Year Avg', 'Status', '5 Year Status'], name = 'NPM')
        return ser
    except:
        print('Something went wronge')

def OPM(lst):
    try:
        SALES = lst.loc['SALES']
        EBIT = lst.loc['EBIT']
        lst = ((EBIT/SALES) * 100).round(2)
        three_year_avg = round(lst.iloc[:3].mean(),2)
        five_year_avg = round(lst.iloc[:5].mean(),2)
        one_year_cagr = lst.iloc[0]
        status = 'Good' if one_year_cagr > 12 else ('Average' if one_year_cagr > 5 and one_year_cagr < 12 else 'BAD' )
        five_year_status = 'Good' if five_year_avg > 12 else ('Average' if five_year_avg > 5 and five_year_avg < 12 else 'BAD' )
        ser = pd.Series([one_year_cagr,three_year_avg, five_year_avg,status,five_year_status], index=['1 Year Avg','3 Year Avg', '5 Year Avg', 'Status', '5 Year Status'], name = 'OPM')
        return ser
    except:
        print('Something went wronge')

def TaxRatio(lst):
    try:
        EBT = lst.loc['EBT']
        TAX = lst.loc['TAX']
        lst = (TAX/EBT * 100).round(2)
        three_year_avg = round(lst.iloc[:3].mean(),2)
        five_year_avg = round(lst.iloc[:5].mean(),2)
        one_year_cagr = lst.iloc[0]
        status = 'Good' if one_year_cagr > 28 else 'BAD'
        five_year_status = 'Good' if five_year_avg > 28 else 'BAD'
        ser = pd.Series([one_year_cagr,three_year_avg, five_year_avg,status,five_year_status], index=['1 Year Avg','3 Year Avg', '5 Year Avg', 'Status', '5 Year Status'], name = 'Tax Ratio')
        return ser
    except:
        print('Something went wronge')

def InterestCoverage(lst):
    # print(lst.loc['EBIT'] / lst.loc['Finance Charges'])
    try:
        EBIT = lst.loc['EBIT']
        FinanceCharges = lst.loc['Finance Charges']
        lst = (EBIT/FinanceCharges).round(2)
        three_year_avg = round(lst.iloc[:3].mean(),2)
        five_year_avg = round(lst.iloc[:5].mean(),2)
        one_year_cagr = lst.iloc[0]
        status = 'Good' if one_year_cagr > 5 else ('Average' if one_year_cagr > 2.5 and one_year_cagr < 5 else 'BAD' )
        five_year_status = 'Good' if five_year_avg > 5 else ('Average' if five_year_avg > 2.5 and five_year_avg < 5 else 'BAD' )
        ser = pd.Series([one_year_cagr,three_year_avg, five_year_avg,status,five_year_status], index=['1 Year Avg','3 Year Avg', '5 Year Avg', 'Status', '5 Year Status'], name = 'Interest Coverage')
        return ser

    except:
        print('Something went wronge')

def TotalDebtCalculate(lst):
    try:
        LTDebt = lst.loc['Interest Bearing Long Term Liability'].fillna(0)
        LTCapitalLeases= lst.loc['Non Interest Bearing Long Term Liability'].fillna(0)
        STDebt = lst.loc['Interest Bearing Short Term Liability'].fillna(0)
        STCapitalLeases = lst.loc['Non Interest Bearing Short Term Liability'].fillna(0)
        TotalDebt = STDebt + STCapitalLeases + LTDebt + LTCapitalLeases
        return TotalDebt
    except:
        print('Something went wronge')  

def TotalDebt(lst):
    try:

        TotalDebt = TotalDebtCalculate(lst)
        three_year_avg = TotalDebt.iloc[0:3].mean()
        five_year_avg =  TotalDebt.iloc[0:5].mean()
        status = 'Good' if three_year_avg < five_year_avg else 'BAD'
        ser = pd.Series([three_year_avg, five_year_avg,status], index=['3 Year Avg','5 Year Avg', 'Status',], name = 'Total Debt')
        return ser
    except:
        print('Something went wronge')

def DebtToEquity(lst):
    try:
        TotalDebt = TotalDebtCalculate(lst)
        TotalEquity = lst.loc['Shareholder Equity'].fillna(0)
        lst = TotalDebt/TotalEquity
        three_year_avg = lst.iloc[0:3].mean().round(2)
        five_year_avg =  lst.iloc[0:5].mean().round(2)
        one_year_cagr = lst.iloc[0].round(2)
        status = 'Good' if one_year_cagr < 0.5 else ('Average' if one_year_cagr > 0.5 and one_year_cagr < 1 else 'BAD' )
        five_year_status = 'Good' if five_year_avg < 0.5 else ('Average' if five_year_avg > 0.5 and five_year_avg < 1 else 'BAD' )
        ser = pd.Series([one_year_cagr,three_year_avg, five_year_avg,status,five_year_status], index=['1 Year Avg','3 Year Avg', '5 Year Avg', 'Status', '5 Year Status'], name = 'Debt to Equity')
        return ser
        return 
    except: 
        print('Something went wronge')

def CurrentRatio(lst):
    try:
        TotalCurrentAssets = lst.loc['Current Assets'].fillna(0)
        TotalCurrentLiabilities = lst.loc['Current Liabilities'].fillna(0)
        lst = TotalCurrentAssets/TotalCurrentLiabilities
        three_year_avg = lst.iloc[0:3].mean().round(2)
        five_year_avg =  lst.iloc[0:5].mean().round(2)
        one_year_cagr = lst.iloc[0].round(2)
        status = 'Good' if one_year_cagr > 1.5 else ('Average' if one_year_cagr > 0.8 and one_year_cagr < 1.5 else 'BAD' )
        five_year_status = 'Good' if five_year_avg > 1.5 else ('Average' if five_year_avg > 0.8 and five_year_avg < 1.5 else 'BAD' )
        ser = pd.Series([one_year_cagr,three_year_avg, five_year_avg,status,five_year_status], index=['1 Year Avg','3 Year Avg', '5 Year Avg', 'Status', '5 Year Status'], name = 'Current Ratio')
        return ser
    except: 
        print('Something went wronge')

def CFO(lst):
    try:

        cfo = lst.loc['Cash From operating Activities'].fillna(0)
        three_year_avg = cfo.iloc[0:3].mean()
        five_year_avg =  cfo.iloc[0:5].mean()
        status = 'Good' if three_year_avg > five_year_avg else 'BAD'
        ser = pd.Series([three_year_avg, five_year_avg,status], index=['3 Year Avg','5 Year Avg', 'Status',], name = 'Cash From operating Activities')
        return ser
    except:
        print('Something went wronge')

def NetCash(lst):
    try:
        netCash = lst.loc['Net Change'].fillna(0)
        three_year_avg = netCash.iloc[0:3].mean()
        five_year_avg =  netCash.iloc[0:5].mean()
        one_year_cagr = netCash.iloc[0]
        status = 'Good' if one_year_cagr > 0 else 'BAD'
        ser = pd.Series([one_year_cagr, three_year_avg, five_year_avg,status], index=['1 Year Avg','3 Year Avg','5 Year Avg', 'Status',], name = 'Net Change in Cash')
        return ser
    except:
        print('Something went wronge')

def CCFOVSPAT(lst):
    try:
        CCFO = lst.loc['Cash From operating Activities'].cumsum()
        PAT = lst.loc['PAT'].cumsum()
        three_year_avg = CCFO.iloc[4]
        five_year_avg = PAT.iloc[4]
        status = 'Good' if CCFO.iloc[4] > PAT.iloc[4] else 'BAD'
        ser = pd.Series([three_year_avg, five_year_avg,status], index=['3 Year Avg','5 Year Avg', 'Status',], name = 'cCFO vs cPAT')
        return ser
    except:
        print('Something went wronge')

def NetAssetTurnover(lst):
    try:
        NFAT = lst.loc['Total Assets Turnover'].fillna(0)
        three_year_avg = NFAT.iloc[0:3].mean()
        five_year_avg =  NFAT.iloc[0:5].mean()
        status = 'Good' if three_year_avg > five_year_avg else 'BAD'
        ser = pd.Series([three_year_avg, five_year_avg,status], index=['3 Year Avg','5 Year Avg', 'Status',], name = 'Net Asset Turnover')
        return ser
    except:
        print('Something went wronge')

def ReturnOnEquity(lst):
    try:
        lst = lst.loc['PAT'].fillna(0) / lst.loc['Shareholder Equity'].fillna(0)
        three_year_avg = lst.iloc[0:3].mean()
        five_year_avg =  lst.iloc[0:5].mean()
        one_year_cagr = (lst.iloc[0] * 100).round(2)
        status = 'Good' if one_year_cagr > 20 else 'BAD'
        ser = pd.Series([one_year_cagr, three_year_avg, five_year_avg,status], index=['1 Year Avg','3 Year Avg','5 Year Avg', 'Status',], name = 'Net Asset Turnover')
        return ser
    except:
        print('Something went wronge')

#cCFO = 67,079,800,000	
# cPAT = 53,793,690,000
# 1. Good ROE : 20% and More
# 2. Bad ROE :20% and Less

# https://sarmaaya.pk/ajax/widgets/all_financials.php?symbol=SYS