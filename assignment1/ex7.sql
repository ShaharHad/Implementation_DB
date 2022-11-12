select distinct count(CustomerId) as customer_amount from invoices
where InvoiceId in (select InvoiceId from invoice_items
where TrackId in (select TrackId from tracks
    where MediaTypeId=(select MediaTypeId from media_types
    where Name='Purchased AAC audio file')))




