SELECT BillingCountry, sum(Total) AS TotalSales FROM invoices
GROUP BY BillingCountry;

SELECT strftime('%Y', InvoiceDate) AS YEAR, SUM(Total) AS TotalSales FROM invoices 
GROUP BY strftime('%Y', InvoiceDate);

SELECT BillingState, sum(total) FROM invoices
WHERE BillingCountry = 'USA' AND InvoiceDate >= '2010-01-01'
GROUP BY BillingState;

SELECT BillingCountry, max(Total) FROM invoices
WHERE BillingCountry = 'Germany' OR BillingCountry = 'France'
GROUP BY BillingCountry;