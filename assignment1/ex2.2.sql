select sum(UnitPrice) from invoice_items
inner join invoices on invoices.InvoiceId = invoice_items.InvoiceId
where strftime('%Y',invoices.InvoiceDate) = ?