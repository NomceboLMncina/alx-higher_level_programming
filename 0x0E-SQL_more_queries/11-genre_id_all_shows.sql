-- Lists all shows contained in the database hbtn_0d_tvshows.
-- Displays NULL for shows without genres.
-- Records are ordered by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT y.`title`, z.`genre_id`
  FROM `tv_shows` AS y
       LEFT JOIN `tv_show_genres` AS z
       ON y.`id` = z.`show_id`
 ORDER BY y.`title`, z.`genre_id`;

