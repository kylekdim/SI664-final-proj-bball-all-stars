SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS player_award, player_award_record, league, all_star, team, team_stat, player_record, player_align;
SET FOREIGN_KEY_CHECKS=1;

--
-- 2.x league table
--
CREATE TABLE IF NOT EXISTS league (
  league_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  league_abbrev VARCHAR(10) NOT NULL UNIQUE,
  League_name VARCHAR(50) NOT NULL UNIQUE,
  PRIMARY KEY (league_id)
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT IGNORE INTO league (league_abbrev, league_name) VALUES
  ('NBA', 'National Basketball Association'), ('ABL1', 'American Basketball League'), ('ABA', 'American Basketball Association'), ('NBL', 'National Basketball League'), ('PBLA', 'Professional Basketball League of America'); 


-- 
-- Create Temp Tables to Create Foreign Keys
--


--
-- 3.x temporary team table
--

CREATE TEMPORARY TABLE temp_team (
  team_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  league_abbrev VARCHAR(10) NOT NULL,
  team_abbrev VARCHAR (10) NOT NULL,
  name VARCHAR(100) NOT NULL,
  arena VARCHAR(100),
  PRIMARY KEY (team_id)
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'team_dedup.csv'
INTO TABLE temp_team
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ',' ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES
  (league_abbrev, team_abbrev, name, arena);

CREATE TABLE IF NOT EXISTS team (
  team_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  league_id INTEGER NOT NULL,
  team_abbrev VARCHAR (10) NOT NULL,
  name VARCHAR(100) NOT NULL,
  arena VARCHAR(100),
  PRIMARY KEY (team_id),
  FOREIGN KEY (league_id) REFERENCES league(league_id)
  ON DELETE CASCADE ON UPDATE CASCADE
  )
  ENGINE=InnoDB
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;

INSERT IGNORE INTO team
(
  team_id,
  league_id,
  team_abbrev,
  name,
  arena
)
SELECT tt.team_id, l.league_id, tt.team_abbrev, tt.name, tt.arena
FROM temp_team tt
  LEFT JOIN league l
  ON TRIM(tt.league_abbrev) = TRIM(l.league_abbrev)
WHERE tt.name IS NOT NULL
ORDER BY tt.name DESC;

--
-- 2.x team_stat table
--

CREATE TABLE IF NOT EXISTS team_stat (
  team_stat_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  team_abbrev VARCHAR(10) NOT NULL,
  year INTEGER NOT NULL,
  home_won INTEGER NOT NULL,
  home_lost INTEGER NOT NULL,
  away_won INTEGER NOT NULL,
  away_lost INTEGER NOT NULL,
  neut_won INTEGER NOT NULL,
  neut_lost INTEGER NOT NULL,
  won INTEGER NOT NULL,
  lost INTEGER NOT NULL,
  games INTEGER NOT NULL,
  PRIMARY KEY (team_stat_id)
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'team_stat_cleaned.csv'
INTO TABLE team_stat
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ',' ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES
  (team_abbrev, year, home_won, home_lost, away_won, away_lost, neut_won, neut_lost, won, lost, games);

--
-- 2.x player_record table
--

CREATE TABLE IF NOT EXISTS player_record (
  player_record_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  player_id_long VARCHAR(10) NOT NULL UNIQUE,
  first_name VARCHAR(30),
  middle_name VARCHAR(30),
  last_name VARCHAR(30) NOT NULL,
  full_given_name VARCHAR(100),
  name_suffix VARCHAR(5),
  nickname VARCHAR(30),
  pos VARCHAR(10),
  height INTEGER,
  weight INTEGER,
  college VARCHAR(50),
  birthdate VARCHAR(20),
  birth_city VARCHAR(50),
  high_school VARCHAR(50),
  hs_city VARCHAR(50),
  hs_state VARCHAR(20),
  hs_country VARCHAR(30),
  death_date VARCHAR(20),
  race VARCHAR(3),
  PRIMARY KEY (player_record_id)
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'basketball_master_cleaned.csv'
INTO TABLE player_record
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ',' ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES
  (player_id_long, first_name, middle_name, last_name, full_given_name, name_suffix, nickname, pos, height, weight, college, birthdate, birth_city, high_school, hs_city, hs_state, hs_country, death_date, race);

--
-- 2.x all_star table
--

CREATE TABLE IF NOT EXISTS all_star (
  all_star_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  player_id_long VARCHAR(10) NOT NULL,
  last_name VARCHAR(30) NOT NULL,
  first_name VARCHAR(30) NOT NULL,
  year INTEGER NOT NULL,
  games_played INTEGER NOT NULL,
  minutes INTEGER NOT NULL,
  points INTEGER,
  rebounds INTEGER,
  assists INTEGER,
  steals INTEGER,
  blocks INTEGER,
  turnovers INTEGER,
  ft_attempted INTEGER,
  ft_made INTEGER,
  three_attempted INTEGER,
  three_made INTEGER,
  PRIMARY KEY (all_star_id)
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'all_star_cleaned.csv'
INTO TABLE all_star
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ',' ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES
  (player_id_long, last_name, first_name, year, games_played, minutes, points, rebounds, assists, steals, blocks, turnovers, ft_attempted, ft_made, three_attempted, three_made);
