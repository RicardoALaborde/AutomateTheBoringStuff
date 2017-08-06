/***********************************************************************
		Challenge Question 6: Print Catalog
		Difficulty  : Beginner
		Instructions: Adventure Works will feature one product for the 
					  cover of its print catalog. Help select a list 
					  of products for consideration.
					  Your list should contain products which meet all 
					  of the following conditions:
						- Finished goods
						- List price at least $1,500
						- At least 150 in inventory
						- Currently available for sale
		Output      : Your output should contain the following columns:
						- ProductID
						- Product Name
						- Color
						- ListPrice
						- Inventory Quantity
		
		Book    : Real SQL Queries - 50 Challenges, Practice for Reporting and Analysis
		Author  : Brian Cohen, Neil Pepi, and Neerja Mishra
		Database: AdventureWorks for SQL Server 2012
		
Script Author: Ricardo Laborde
************************************************************************/

SELECT
	a.ProductID
	,a.Name
	,a.Color
	,a.ListPrice
	,b.Qty
FROM AdventureWorks2012.Production.Product a
INNER JOIN (SELECT ProductID,SUM(Quantity)Qty FROM AdventureWorks2012.Production.ProductInventory b GROUP BY ProductID)b ON a.ProductID = b.ProductID
where a.ListPrice >= 1500
AND a.FinishedGoodsFlag = 1
AND a.SellEndDate IS NULL
AND b.Qty >= 150