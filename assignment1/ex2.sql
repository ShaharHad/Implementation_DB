select name from (select name, max(count)
                  from (select (count(AlbumId)) as count, Name
                        from (select artists.ArtistId, AlbumId, artists.Name
                              from artists
                                       inner join albums a on artists.ArtistId = a.ArtistId)
                        group by ArtistId))
