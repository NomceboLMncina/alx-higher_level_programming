-- Lists all genres of the database hbtn_0d_tvshows
-- not linked to the show Dexter.
-- Records are sorted by ascending genre name.
SELECT DISTINCT `name`
  FROM `tv_genres` AS z
       INNER JOIN `tv_show_genres` AS y
       ON z.`id` = y.`genre_id`

       INNER JOIN `tv_shows` AS r
       ON y.`show_id` = r.`id`
       WHERE z.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` AS z
	             INNER JOIN `tv_show_genres` AS y
		     ON z.`id` = y.`genre_id`

		     INNER JOIN `tv_shows` AS r
		     ON y.`show_id` = r.`id`
		     WHERE r.`title` = "Dexter")
 ORDER BY z.`name`;
