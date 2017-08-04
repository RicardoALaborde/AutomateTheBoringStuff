/***********************************************************************
		Challenge Question 5: Expired Credit Cards
		Difficulty  : Intermediate
		Instructions: The Accounting Department found instances where expired credit cards were
					  used with sales orders. You are asked to examine all credit cards and 
					  report the extent of such activity.
					  
					  Part I: Based on each CreditCardID, find the following:
						- CreditCardType
						- ExpirationDate
						- Last Order Date
						- Number of sales orders with order dates earlier than or equal to 
						  the card's expiration date
						- Number of sales orders with order dates later than the card's
						  expiration date

					  Part II: Based on CreditCardType, summarize data returned from Part I. 
						Your output should include the following columns:
							- CreditCardType
							- Number of sales orders with order dates earlier than or equal to 
							  the card's expiration date.
							- Number of sales orders with order dates later than the card's 
							  expiration date

		Notes       : Adventure Works stores information about a credit card's expiration year
					  and expiration month. Expiration dates pertain to the last day of a card's 
					  expiration month. For example, if the expiration year is 2007 and the 
					  expiration month is "4", the card's expiration date will be April 30, 
					  2007.
	
		Book    : Real SQL Queries - 50 Challenges, Practice for Reporting and Analysis
		Author  : Brian Cohen, Neil Pepi, and Neerja Mishra
		Database: AdventureWorks for SQL Server 2012
		
Script Author: Ricardo Laborde
************************************************************************/


