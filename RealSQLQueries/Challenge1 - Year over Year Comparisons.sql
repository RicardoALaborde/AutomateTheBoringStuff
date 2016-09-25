/***********************************************************************
		Challenge Question 1: Year over Year Comparisons
		Difficulty  : Intermediate
		Instructions: An executive requests data concerning fiscal
					  quarter sales by salesperson. She'd like to
					  see comparisons from the fiscal quarters of 
					  2008 to the same fiscal quarters of 2007. 

					  For example, suppose sales for salesperson X 
					  totaled $1,000 during Fiscal Year 2008, Fiscal 
					  Quarter 2. If sales for salesperson X totaled $900 
					  in fiscal Year 2007, Fiscal Quarter 2, this reflects 
					  about 11.1% growth between two periods for salesperson X.
		Notes       : For Adventure Works, the fiscal year spans July through 
					  June.
					  Tax and freight will not be considered with revenue.
					  Dates are based on OrderDate
					  Disregard online orders.
		Output      :
			|********|*************|****|**|*******|***************|******|*******|
			|LastName|SalesPersonID|FY  |FQ|FQSales|SalesSameFQLast|Change|%Change|
			|--------|-------------|----|--|-------|---------------|------|-------|
			|X       |1            |2008|2 |1000   |900            |100   |11.1   |
			|********|*************|****|**|*******|***************|******|*******|
		
		Book    : Real SQL Queries - 50 Challenges, Practice for Reporting and Analysis
		Author  : Brian Cohen, Neil Pepi, and Neerja Mishra
		Database: AdventureWorks for SQL Server 2012
		
Script Author: Ricardo Laborde

************************************************************************/
DECLARE @FiscalYear int
SET @FiscalYear = 2008

SELECT DISTINCT
	b.LastName as LastName,
	b.BusinessEntityID as SalesPersonID,
	YEAR(OrderDate) as FY,
	CASE WHEN MONTH(OrderDate) BETWEEN 7 AND 9 THEN 'Q1'
		 WHEN MONTH(OrderDate) BETWEEN 10 AND 12 THEN 'Q2'
		 WHEN MONTH(OrderDate) BETWEEN 1 AND 3 THEN 'Q3'
		 WHEN MONTH(OrderDate) BETWEEN 4 AND 6 THEN 'Q4'
	END as FQ,
	SUM(SubTotal) as FQSales,
	ISNULL(SalesLastYear.FQSales,0) as SalesSameFQLast,
	SUM(SubTotal) - ISNULL(SalesLastYear.FQSales,0) as Change,
	(SUM(SubTotal) - ISNULL(SalesLastYear.FQSales,0))/SUM(SubTotal) * 100 as '%Change'
FROM 
	Sales.SalesOrderHeader a
INNER JOIN
	Sales.vSalesPerson b
		ON
			a.SalesPersonID = b.BusinessEntityID
LEFT JOIN (
	SELECT
		b.BusinessEntityID as SalesPersonID,
		YEAR(OrderDate) as FY,
		CASE WHEN MONTH(OrderDate) BETWEEN 7 AND 9 THEN 'Q1'
			 WHEN MONTH(OrderDate) BETWEEN 10 AND 12 THEN 'Q2'
			 WHEN MONTH(OrderDate) BETWEEN 1 AND 3 THEN 'Q3'
			 WHEN MONTH(OrderDate) BETWEEN 4 AND 6 THEN 'Q4'
		END as FQ,
		SUM(SubTotal) as FQSales
	FROM
		Sales.SalesOrderHeader a
	INNER JOIN
		Sales.vSalesPerson b
			ON
				a.SalesPersonID = b.BusinessEntityID
	WHERE 
		YEAR(OrderDate) = @FiscalYear - 1
	AND OnlineOrderFlag = 0
	GROUP BY
		b.BusinessEntityID,
		YEAR(OrderDate),
		CASE WHEN MONTH(OrderDate) BETWEEN 7 AND 9 THEN 'Q1'
				  WHEN MONTH(OrderDate) BETWEEN 10 AND 12 THEN 'Q2'
				  WHEN MONTH(OrderDate) BETWEEN 1 AND 3 THEN 'Q3'
				  WHEN MONTH(OrderDate) BETWEEN 4 AND 6 THEN 'Q4'
		END
		) SalesLastYear
			ON 
				SalesLastYear.SalesPersonID = b.BusinessEntityID
			AND
				SalesLastYear.FQ = CASE WHEN MONTH(OrderDate) BETWEEN 7 AND 9 THEN 'Q1'
										WHEN MONTH(OrderDate) BETWEEN 10 AND 12 THEN 'Q2'
										WHEN MONTH(OrderDate) BETWEEN 1 AND 3 THEN 'Q3'
										WHEN MONTH(OrderDate) BETWEEN 4 AND 6 THEN 'Q4' END
WHERE 
	YEAR(OrderDate) = @FiscalYear
AND
	OnlineOrderFlag = 0
GROUP BY
	b.LastName,
	b.BusinessEntityID,
	YEAR(OrderDate),
	CASE WHEN MONTH(OrderDate) BETWEEN 7 AND 9 THEN 'Q1'
		 WHEN MONTH(OrderDate) BETWEEN 10 AND 12 THEN 'Q2'
		 WHEN MONTH(OrderDate) BETWEEN 1 AND 3 THEN 'Q3'
		 WHEN MONTH(OrderDate) BETWEEN 4 AND 6 THEN 'Q4'
	END,
	ISNULL(SalesLastYear.FQSales,0)