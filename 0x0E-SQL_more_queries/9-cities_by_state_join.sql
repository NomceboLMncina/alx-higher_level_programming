-- Lists all cities in the database hbtn_0d_usa.
-- Records are sorted in order of ascending cities.id.
SELECT x.`id`, x.`name`, y.`name`
  FROM `cities` AS x
       INNER JOIN `states` AS y
       ON x.`state_id` = y.`id`
 ORDER BY x.`id`;
