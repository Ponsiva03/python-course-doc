from langchain.llms import * 
import openai 
import os
import re
import time
import pandas as pd
from tkinter import *
import tkinter.messagebox


openai.api_key =  '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'

df = pd.DataFrame()

j = input ('Enter the folder name (where your test file resides) : ')
entries = os.listdir(j+'/')

file_name = []
grantor = []
grantee = []


for i in entries:
  file1 = open(r"E:\Annotation files\test 5\\"+i,encoding="utf8" )
  a = file1.read()
  #a = re.sub('\W+',' ', a )
  #a = re.sub(r'[?||(|)|".|!|@]|:',r'',a)
  file_name.append(i)
  
  response_grantor = openai.Completion.create(
      engine = "text-davinci-003" ,
      prompt = f'find the Grantor in my text{a}',
      temperature = 1.0,
      max_tokens = 200
  ) 
  grantor.append(response_grantor.choices[0].text)

  response_grantee = openai.Completion.create(
      engine = "text-davinci-003" ,
      prompt = f'find the Grantee in my text{a}',
      temperature = 1.0,
      max_tokens = 200
  ) 
  grantee.append(response_grantee.choices[0].text)

  print('File Name is '+ i)       
  print(response_grantor.choices[0].text) 
  print(response_grantee.choices[0].text)
  time.sleep(2)
  print('-------------------------------------------') 

df['File Name'] = file_name
df['Grantor'] = grantor
df['Grantee'] = grantee

df.to_csv('test data 2.csv')

tkinter.messagebox.showinfo("Welcome to Text Extraction Tool.",  "Process Successfully Executed")