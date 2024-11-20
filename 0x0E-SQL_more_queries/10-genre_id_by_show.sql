-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked.
-- Records are sorted by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT y.`title`, z.`genre_id`
  FROM `tv_shows` AS y
        INNER JOIN `tv_show_genres` AS z
	ON y.`id` = z.`show_id`
 ORDER BY y.`title`, z.`genre_id`;

