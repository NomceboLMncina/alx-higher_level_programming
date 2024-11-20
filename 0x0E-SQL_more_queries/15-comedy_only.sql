-- Lists all comedy shows in the database hbtn_0d_tvshows.
-- Records are ordered by descending show title.
SELECT r.`title`
  FROM `tv_shows` AS r
       INNER JOIN `tv_show_genres` AS y
       ON r.`id` = y.`show_id`

       INNER JOIN `tv_genres` AS z
       ON z.`id` = y.`genre_id`
       WHERE z.`name` = "Comedy"
 ORDER BY r.`title`;
