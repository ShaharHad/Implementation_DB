select sum(price) as total_price
    from (select (UnitPrice * Quantity) as price, strftime('%Y', InvoiceDate) as year
                        from invoices
                                 inner join invoice_items
                        where invoices.InvoiceId == invoice_items.InvoiceLineId
                          and year == '2010')
