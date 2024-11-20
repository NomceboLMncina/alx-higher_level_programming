-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- Records are ordered by ascending genre name.
SELECT z.`name`
  FROM `tv_genres` AS z
       INNER JOIN `tv_show_genres` AS y
       ON z.`id` = y.`genre_id`

       INNER JOIN `tv_shows` AS r
       ON r.`id` = y.`show_id`
       WHERE r.`title` = "Dexter"
 ORDER BY z.`name`;
