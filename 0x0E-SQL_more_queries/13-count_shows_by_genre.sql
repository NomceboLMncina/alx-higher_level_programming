-- Lists all genres from the database hbtn_0d_tvshows along with the number of
-- shows linked to each.
-- Does not display genres without linked shows.
-- Records are ordered by descending number of shows linked.
SELECT z.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS z
       INNER JOIN `tv_show_genres` AS r
       ON z.`id` = r.`genre_id`
 GROUP BY z.`name`
 ORDER BY `number_of_shows` DESC;

