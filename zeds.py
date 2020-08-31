#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 31 Aug 2020

@author: tomstafford

python3 script for finding/loading zeds pages

looks in the file shopping.csv for items and either searches for them or, if there is a url, loads that page

you can then click "add to basket"

conda environment environment.yml will ensure you have the right library versions etc but it doesn't rely on anything fancy so it should work ok

Not licensed, endorsed, the responsibility of, etc Zeds in any way!

Do it the old fashioned way at
https://store.zedswholefoods.co.uk/

"""
import pandas as pd #dataframes -for loading the csv file
import webbrowser as wb # - for webpage magic


def getitem(thing):
	"""open a browser tab for item (either the url or the search page)"""

	if thing[:4]=='http':
		#if it is a URL
		searchstring=thing

	else:	
		#if it isn't
		searchstring='https://store.zedswholefoods.co.uk/?s=carrots&post_type=product&dgwt_wcas=1'

		newsearch =thing


		searchstring = searchstring.replace('carrots',newsearch)

	#open a tab!
	wb.open(searchstring)


df=pd.read_csv('shopping.csv') #load the list of shopping items from the file

#go through the list line by line and open a tab
for i,row in df.iterrows():
	if pd.isnull(row['url']):
		getitem(row['item'])
	else:
		getitem(row['url'])


