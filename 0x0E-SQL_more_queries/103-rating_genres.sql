-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Records are ordered by descending rating.
SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS z
       INNER JOIN `tv_show_genres` AS y
       ON y.`genre_id` = z.`id`

       INNER JOIN `tv_show_ratings` AS s
       ON s.`show_id` = y.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;
