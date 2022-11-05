select FirstName, LastName from(
    select  c.FirstName, c.LastName, sum(t.Quantity * t.UnitPrice) as total_price from (
        select InvoiceId, TrackId, UnitPrice, Quantity from invoice_items
        where TrackId in
        (    select TrackId from tracks
            where GenreId =
                (select GenreId from genres
                where Name = 'Classical')
        )) as t
    inner join invoices on invoices.InvoiceId == t.InvoiceId
    inner join customers c on c.CustomerId = invoices.CustomerId
    group by c.CustomerId)
order by total_price desc
limit 1





