/***********************************************************************
		Challenge Question 4: Upsell Tuesdays
		Difficulty  : Beginner
		Instructions: Tuesdays are "upsell" days for sales people at Adventure Works.
					  Management wants to compare sales from Tuesday to other days of
					  the week to see if the initiative is working. Help monitor the
					  upsell initiative by creating a query to calculate average revenue 
					  per order by day of week in 2008.
					  			  
		Notes       : Dates are based on OrderDate
					  Tax and freight should not be considered.
					  Exclude online orders
	
		Book    : Real SQL Queries - 50 Challenges, Practice for Reporting and Analysis
		Author  : Brian Cohen, Neil Pepi, and Neerja Mishra
		Database: AdventureWorks for SQL Server 2012
		
Script Author: Ricardo Laborde

************************************************************************/


DECLARE @Year varchar(4);
SET @Year = '2008'

SELECT 
	DATENAME(WEEKDAY,OrderDate) as 'Day Of Week',
	COUNT(SalesOrderID) as 'Orders',
	SUM(SubTotal) as 'Total Revenue',
	SUM(SubTotal)/COUNT(*) as 'Average Revenue per Order'
FROM 
	AdventureWorks2012.Sales.SalesOrderHeader
WHERE
	OnlineOrderFlag = 0
AND
	YEAR(OrderDate) = @Year
GROUP BY
	DATENAME(WEEKDAY,OrderDate)