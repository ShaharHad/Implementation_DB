select t.name, t.AlbumId from(
    select artists.Name, a.AlbumId, count(a.AlbumId) as tracks_amount from artists
    inner join albums a on artists.ArtistId = a.ArtistId
    inner join tracks t on a.AlbumId = t.AlbumId
    group by a.AlbumId) as t
order by tracks_amount desc
limit 1
