import os
import pandas as pd

#read and setup CSV files
m_pull_df=pd.read_csv("PFT\m_pull.csv")
m_pullup_table = m_pull_df.set_index("rep", drop = False)

#Recieve total pulls from user
pullup=int(input("How many pullups?:  "))
years=int(input("What is your age?:  "))

#Recieve users age
if years < 17:
    print("You are too young to serve")
elif years >= 17:
    print("You are {} years old".format(years))
else:
    print("You entered an invalid input. Please try again.")
years = str(years)


#Lookup Male Pullups
m_pull = m_pullup_table.loc[m_pullup_table["rep"] == pullup, years].values[0]

print(m_pull)


