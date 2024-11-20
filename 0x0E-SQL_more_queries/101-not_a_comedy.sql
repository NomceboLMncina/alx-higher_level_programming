-- Lists all shows without the comedy genre in the database hbtn_0d_tvshows.
-- Records are ordered by ascending show title.
SELECT DISTINCT `title`
  FROM `tv_shows` AS r
       LEFT JOIN `tv_show_genres` AS y
       ON y.`show_id` = r.`id`

       LEFT JOIN `tv_genres` AS z
       ON z.`id` = y.`genre_id`
       WHERE r.`title` NOT IN
             (SELECT `title`
                FROM `tv_shows` AS r
	             INNER JOIN `tv_show_genres` AS y
		     ON y.`show_id` = r.`id`

		     INNER JOIN `tv_genres` AS z
		     ON z.`id` = y.`genre_id`
		     WHERE z.`name` = "Comedy")
 ORDER BY `title`;
