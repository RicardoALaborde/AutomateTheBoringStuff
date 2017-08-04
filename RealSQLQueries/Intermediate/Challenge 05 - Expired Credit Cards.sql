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

IF OBJECT_ID('tempdb.dbo.#Orders') IS NOT NULL
BEGIN
	DROP TABLE #Orders
END

SELECT DISTINCT
	b.CreditCardID
	,b.CardType
	,EOMONTH(CAST(CAST(b.ExpYear as varchar) + '-' + CAST(b.ExpMonth as varchar) + '-01' as date)) as ExpirationDate
	,FIRST_VALUE(a.OrderDate) OVER(PARTITION BY b.CreditCardID ORDER BY a.OrderDate desc) LastOrderDate
	,SUM(CASE WHEN a.OrderDate <= EOMONTH(CAST(CAST(b.ExpYear as varchar) + '-' + CAST(b.ExpMonth as varchar) + '-01' as date)) THEN 1 ELSE 0 END) OVER(PARTITION BY b.CreditCardID) Before
	,SUM(CASE WHEN a.OrderDate > EOMONTH(CAST(CAST(b.ExpYear as varchar) + '-' + CAST(b.ExpMonth as varchar) + '-01' as date)) THEN 1 ELSE 0 END) OVER(PARTITION BY b.CreditCardID) 'After'
INTO #Orders
FROM AdventureWorks2012.Sales.SalesOrderHeader a
INNER JOIN AdventureWorks2012.Sales.CreditCard b ON a.CreditCardID = b.CreditCardID
--Solution to first part--
SELECT * FROM #Orders

--Solution to Second part--
SELECT 
	CardType
	,SUM(BeforeSales) as Before
	,SUM(AfterSales) as 'After'
FROM #Orders
GROUP BY CardType