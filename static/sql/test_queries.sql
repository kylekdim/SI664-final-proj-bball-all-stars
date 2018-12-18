#test queries SQL

SELECT als.all_star_id, als.player_record_id, pr.first_name, pr.last_name
FROM all_star als
LEFT JOIN player_record pr
ON als.player_record_id = pr.player_record_id
WHERE als.player_record_id = 101;