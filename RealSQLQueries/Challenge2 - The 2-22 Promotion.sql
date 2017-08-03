/***********************************************************************
		Challenge Question 2: The 2/22 Promotion
		Difficulty  : Intermediate
		Instructions: A marketing manager devised the "2/22" promotion, 
					  in which orders subtotaling at least $2,000 ship 
					  for $0.22. The strategy assumes that freight losses 
					  will be offset by gains from higher value orders. 
					  According to the marketing manager, orders between 
					  $1,700 and $2,000 will likely boost to $2,000 as customers 
					  feel compelled to take advantage of bargain freight pricing.
					  
					  You are asked to test the 2/22 promotion for hypothetical 
					  profitability based on the marketing manager's assumption about 
					  customer behavior. Examine orders shipped to California during 
					  fiscal year 2008 for net gains or losses under the promotion.					  
		Notes       : For Adventure Works, the fiscal year spans July through 
					  June.
					  Tax should not be considered.
		
		Book    : Real SQL Queries - 50 Challenges, Practice for Reporting and Analysis
		Author  : Brian Cohen, Neil Pepi, and Neerja Mishra
		Database: AdventureWorks for SQL Server 2012
		
Script Author: Ricardo Laborde

************************************************************************/


/********PART 1**********/
--------------------------
/* Create the table      */
IF OBJECT_ID('tempdb..#data') IS NOT NULL
	BEGIN
		DROP TABLE #data
	END

DECLARE @FiscalYear varchar(4)
SET @FiscalYear = '2008'
SET @FiscalYear = CAST(@FiscalYear as int) - 1

SELECT
	a.SalesOrderID,
	c.Name as ShipToState,
	a.OrderDate,
	a.Subtotal,
	a.Freight,
	PotentialPromoEffect = 
		 CASE WHEN a.SubTotal < 2000 AND a.SubTotal >= 1700 THEN
			'Increase order to $2,000 and pay $0.22 freight'
		 WHEN a.SubTotal >= 2000 THEN
			'No order change and pay $0.22 freight'
		 ELSE
			'No order change and pay historical freight'
		 END,
	PotentialGain = CASE WHEN a.SubTotal >= 1700 AND a.SubTotal < 2000 THEN 2000 - a.SubTotal ELSE 0 END,
	PotentialFreightLoss = CASE WHEN a.SubTotal >= 1700 THEN 0.22 ELSE a.Freight END - a.Freight,
	NetGainLoss = CASE WHEN a.SubTotal >= 1700 AND a.SubTotal < 2000 THEN 2000 - a.SubTotal ELSE 0 END 
				+ CASE WHEN a.SubTotal >= 1700 THEN 0.22 ELSE a.Freight END 
				- a.Freight
INTO #data
FROM Sales.SalesOrderHeader a
INNER JOIN Person.Address b ON a.BillToAddressID = b.AddressID
INNER JOIN Person.StateProvince c ON b.StateProvinceID = c.StateProvinceID
WHERE c.Name = 'California'
AND a.OrderDate BETWEEN '7-1-'+ @FiscalYear AND DATEADD(month,12,'7-1-' + @FiscalYear )

SELECT * FROM #data

/**********PART 2**************/
--------------------------------
/* Aggregate data from Part 1 */
SELECT 
	PotentialPromoEffect,
	SUM(PotentialGain) as PotentialGain,
	SUM(PotentialFreightLoss) as PotentialFreightLoss,
	SUM(NetGainLoss) as NetGainLoss
FROM #data
GROUP BY PotentialPromoEffect