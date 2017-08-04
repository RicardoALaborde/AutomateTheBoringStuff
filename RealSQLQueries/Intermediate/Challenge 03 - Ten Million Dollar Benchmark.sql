/***********************************************************************
		Challenge Question 3: Ten Million Dollar Benchmark
		Difficulty  : Intermediate
		Instructions: Ten Million Dollars of revenue is a common benchmark for Adventure Works. For each
					  fiscal year (2007 and 2008), find the first dates when the cumulative running 
					  revenue total hit $10,000,000.

		Notes       : For Adventure Works, the fiscal year spans July through 
					  June.
					  Tax and freight will not be considered with revenue.

		Output      :
			|**********|*************|********|************|
			|FiscalYear|OrderDate    |FYOrder#|RunningTotal|
			|----------|-------------|--------|------------|
			|2007      |2006-09-08   |894     |10000512.48 |
			|----------|-------------|--------|------------|
			|2008      |2007-09-01   |2420    |10002328.07 |
			|**********|*************|********|************|
		
		Book    : Real SQL Queries - 50 Challenges, Practice for Reporting and Analysis
		Author  : Brian Cohen, Neil Pepi, and Neerja Mishra
		Database: AdventureWorks for SQL Server 2012
		
Script Author: Ricardo Laborde
************************************************************************/


SELECT 
	Fiscal_Year,OrderDate,OrderNumber,RunningTotalSales
FROM (
	SELECT 
		*
		,ROW_NUMBER()OVER(PARTITION BY Fiscal_Year ORDER BY OrderDate) rn
	FROM (
		SELECT
			CASE WHEN DatePart(Month, OrderDate) >= 7 THEN YEAR(OrderDate) + 1
				 ELSE YEAR(OrderDate) END AS Fiscal_Year
			,OrderDate
			,SubTotal	
			,SUM(SubTotal) OVER(PARTITION BY CASE WHEN DatePart(Month, OrderDate) >= 7 THEN YEAR(OrderDate) + 1 ELSE YEAR(OrderDate) END ORDER BY OrderDate ROWS UNBOUNDED PRECEDING) as RunningTotalSales
			,ROW_NUMBER()OVER(PARTITION BY CASE WHEN DatePart(Month, OrderDate) >= 7 THEN YEAR(OrderDate) + 1 ELSE YEAR(OrderDate) END ORDER BY OrderDate) as OrderNumber
			,SalesOrderID
		FROM AdventureWorks2012.Sales.SalesOrderHeader
		WHERE OrderDate BETWEEN '07-01-2006' AND '06-30-2008'
	)a
	WHERE RunningTotalSales >= 10000000
)a
WHERE rn = 1