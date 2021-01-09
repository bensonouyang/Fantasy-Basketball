#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

def main():
    
    data = pd.read_csv('cleandata.csv')
    # Column for Average Fantasy Points calculated based on columns based on different weights placed on different statline
    # The weights are based off users inputs
    
    fgm = int(input("Enter weights for field goals made: "))
    fga = int(input("Enter weights for field goals attempted: "))
    ftm = int(input("Enter weights for free throws made: "))
    fta = int(input("Enter weights for free throws attempted: "))
    threemade = int(input("Enter weights for 3 pointers made: "))
    threemiss = int(input("Enter weights for 3 pointers missed: "))
    reb = int(input("Enter weights for rebounds: "))
    ast = int(input("Enter weights for assists: "))
    stl = int(input("Enter weights for steals: "))
    blk = int(input("Enter weights for blocks: "))
    to = int(input("Enter weights for turnovers: "))
    pts = int(input("Enter weights for points: "))
    
    data['AFP'] = fgm*data['FG'] - fta*data['FGA'] + ftm*data['FT'] - ftm*data['FTA'] 
    + threemade*data['3P'] - threemiss*(data['3PA'] - data['3P']) + reb*data['TRB'] + ast*data['AST']
    + stl*data['STL'] + blk*data['BLK'] - to*data['TOV'] + pts*data['PTS']
    
    
    position = input("Enter position for list of top fantasy player (PG, SG, SF, PF, C): ")
    
    while(position != "stop"):
        if((position == "PG") or (position == "SG") or (position == "SF") or (position == "PF") or (position == "C")):
            df = data[(data['Pos'] == position) & (data['AFP'] > np.mean(data['AFP']))]
            print(df[['Player', 'AFP']].sort_values(by = 'AFP', ascending = False).head(30))
        position = input("Enter another position or type stop to cancel program: ")

    

if __name__=='__main__':
    main()


# In[ ]:




