import pandas as pd

def AverageInventory(lst):
    StoresandSpares = lst.loc['Stores and Spares']
    StockinTrade = lst.loc['Stock in Trade']
    Inventory = StoresandSpares + StockinTrade
    AverageInventory = []
    
    for i in range(0, len(Inventory) - 1):
        AverageInventory.append(((Inventory.iloc[i] + Inventory.iloc[i +1]) / 2))
    return AverageInventory

def InventoryTurnOver(lst):
    try:
        averageInventory = AverageInventory(lst)
        COGS = lst.loc['COGS']
        inventoryTurnOver = round(COGS[:len(averageInventory)] / averageInventory,2)
        three_year_avg = round(inventoryTurnOver.iloc[0:3].mean(),2)
        five_year_avg =  round(inventoryTurnOver.iloc[0:5].mean(),2)
        status = 'GOOD' if three_year_avg > five_year_avg else 'BAD'
        ser = pd.Series([three_year_avg, five_year_avg,status], index=['3 Year Avg','5 Year Avg', 'Status',], name = 'Inventory TurnOver Rate')
        return ser
    except:
        print('Something Went Wrong in Inventory TurnOver Rate')
# def calculateDaysReceivableOutstanding(lst):
    quickAssets = lst.loc['Quick Assets']
    averageQuickAssets = []
    for i in range(0, len(quickAssets) - 1):
                averageQuickAssets.append(((quickAssets.iloc[i] + quickAssets.iloc[i +1]) / 2))
    
    Sales = lst.loc['Sales']
    daysReceivableOutstanding = round((averageQuickAssets/Sales[:len(averageQuickAssets)]) * 365 ,2)
    return daysReceivableOutstanding

def DaysReceivableOutstanding(lst):
    try:
        daysReceivableOutstanding = lst.loc['Average Collection Period']
        three_year_avg = round(daysReceivableOutstanding.iloc[0:3].mean(),2)
        five_year_avg =  round(daysReceivableOutstanding.iloc[0:5].mean(),2)
        status = 'GOOD' if three_year_avg < five_year_avg else 'BAD'
        ser = pd.Series([three_year_avg, five_year_avg,status], index=['3 Year Avg','5 Year Avg', 'Status',], name = 'Days Receivable Outstanding')
        return ser
    except:
        print('Something Went Wrong in Days Receivable Outstanding')

# def CalculateDaysSalesofInventory(lst):
    averageInventory = AverageInventory(lst)
    COGS = lst.loc['COGS']
    daysSalesofInventory = round((averageInventory/COGS[:len(averageInventory)]) * 365 ,2)
    return daysSalesofInventory

    
def DaysSalesofInventory(lst):
    try:
        daysSalesofInventory = lst.loc['Days sales Inventory']
        three_year_avg = round(daysSalesofInventory.iloc[0:3].mean(),2)
        five_year_avg =  round(daysSalesofInventory.iloc[0:5].mean(),2)
        status = 'GOOD' if three_year_avg < five_year_avg else 'BAD'
        ser = pd.Series([three_year_avg, five_year_avg,status], index=['3 Year Avg','5 Year Avg', 'Status',], name = 'Days Sales of Inventory')
        return ser
    except:
        print('Something Went Wrong in Days Sales of Inventory')

def CalculateDaysPayableOutstanding(lst):
    tradesPayables = lst.loc['Trades Payables']
    averagePayables = []
    for i in range(0, len(tradesPayables) - 1):
                averagePayables.append(((tradesPayables.iloc[i] + tradesPayables.iloc[i +1]) / 2))
    
    COGS = lst.loc['COGS']
    daysPayableOutstanding = round((averagePayables/COGS[:len(averagePayables)]) * 365 ,2)
    return daysPayableOutstanding

def DaysPayableOutstanding(lst):
    try:
        daysPayableOutstanding = CalculateDaysPayableOutstanding(lst)
        three_year_avg = round(daysPayableOutstanding.iloc[0:3].mean(),2)
        five_year_avg =  round(daysPayableOutstanding.iloc[0:5].mean(),2)
        status = 'GOOD' if three_year_avg > five_year_avg else 'BAD'
        ser = pd.Series([three_year_avg, five_year_avg,status], index=['3 Year Avg','5 Year Avg', 'Status',], name = 'Days Payable Outstanding')
        return ser
    except:
        print('Something Went Wrong in Days Payable Outstanding')

def CashConversionCycle(lst):
    try:
        daysPayableOutstanding = CalculateDaysPayableOutstanding(lst)
        daysSalesofInventory = lst.loc['Days sales Inventory']
        daysReceivableOutstanding = lst.loc['Average Collection Period']
        CCC = (daysSalesofInventory + daysReceivableOutstanding) - daysPayableOutstanding
        three_year_avg = round(CCC.iloc[0:3].mean(),2)
        five_year_avg =  round(CCC.iloc[0:5].mean(),2)
        status = 'GOOD' if three_year_avg < five_year_avg else 'BAD'
        ser = pd.Series([three_year_avg, five_year_avg,status], index=['3 Year Avg','5 Year Avg', 'Status',], name = 'Cash Conversion Cycle')
        return ser
    except:
        print("Something Went Wrong in Cash Conversion Cycle")