-- Lists all shows in the database hbtn_0d_tvshows without a genre linked.
-- Records are ordered by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT y.`title`, z.`genre_id`
  FROM `tv_shows` AS y
       LEFT JOIN `tv_show_genres` AS z
       ON y.`id` = z.`show_id`
       WHERE z.`genre_id` IS NULL
 ORDER BY y.`title`, z.`genre_id`;
