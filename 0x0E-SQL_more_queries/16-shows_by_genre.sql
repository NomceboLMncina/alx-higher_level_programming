-- Lists all shows and genres linked to the show from the
-- database hbtn_0d_tvshows.
-- Records are ordered by ascending show title and genre name.
SELECT r.`title`, z.`name`
  FROM `tv_shows` AS r
       LEFT JOIN `tv_show_genres` AS y
       ON r.`id` = y.`show_id`

       LEFT JOIN `tv_genres` AS z
       ON y.`genre_id` = z.`id`
 ORDER BY r.`title`, z.`name`;
