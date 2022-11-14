select count(distinct CustomerId) as customers_count
from(select i.CustomerId
    from tracks
    inner join invoice_items ii on tracks.TrackId = ii.TrackId
    inner join invoices i on i.InvoiceId = ii.InvoiceId
    where tracks.UnitPrice = (SELECT max(UnitPrice) FROM tracks))



