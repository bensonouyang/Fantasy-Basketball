#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def main():
    data = pd.read_csv('stats.csv')
    del data['Unnamed: 0']

    # Players that have gotten traded are placed in a different row with stats from their time on that specific team

    TradedPlayers = []

    # Placing players that were traded in a list called TradedPlayers
    for i in range(len(data) - 1):
        temp = data.loc[i+1].Player
        if (temp == data.loc[i].Player) & (temp not in TradedPlayers):
            TradedPlayers.append(temp)
    
    # Dataframe containing players that weren't traded
    Nontraded_DF = data[data["Player"].isin(TradedPlayers) == False]
    
    # Dataframe containing players that were traded and stats for each team they were on
    Traded_DF = data[data["Player"].isin(TradedPlayers)]
    
    # Dataframe containing total stats of players that were traded
    TradedTot_DF = Traded_DF[Traded_DF['Tm'] == 'TOT']
    
    # Combined Dataframe of traded and non traded players
    Combined_DF = Nontraded_DF.append(TradedTot_DF).reset_index()

    del Combined_DF['index']
    
    # Missing data can be replaced with 0's, usually bench players 
    Combined_DF = Combined_DF.fillna(0)

    Combined_DF.to_csv("cleandata.csv")


    
if __name__=='__main__':
    main()

