### sends birthday emails according to csv list ###

import email
import pandas as pd 
import random as rd 
import smtplib
import datetime as dt  
my_email = input(f"input your gmail address :")      
my_password = input(f"input your password for {my_email} :")
now = dt.datetime.now() 
today = now.day
month_index = now.month

def send_mail(letter,tomail) :
    with smtplib.SMTP("smtp.gmail.com",port=587) as connector: 
        connector.starttls() 
        connector.login(user=my_email,password=my_password)
        connector.sendmail(
            from_addr= my_email,
            to_addrs= tomail ,
            msg=f"Subject:Happy Birthday! \n\n {letter}" 
        )

data = pd.read_csv("birthdays.csv",index_col=False)
mydf = pd.DataFrame(data)
#print(data)
for  index,row in mydf.iterrows():
    if row["month"] == month_index and row["day"] == today:
        l_index = rd.randint(1,3)
        path = f"letter_templates/letter_{l_index}.txt"
        with open(path,"r") as letter :
            letter_index = letter.read() 
        letter_index = letter_index.replace("[NAME]",row["name"])
        print(letter_index)
        send_mail(letter_index,row["email"])
    

        
