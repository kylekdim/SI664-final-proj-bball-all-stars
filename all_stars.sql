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
  ('NBA', 'National Basketball Association'), ('ABA', 'American Basketball Association'); 

--
-- 2.x team table
--

CREATE TABLE IF NOT EXISTS team (
  team_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
  league_id VARCHAR(10) NOT NULL,
  team_abbrev VARCHAR (10) NOT NULL,
  name VARCHAR(100) NOT NULL,
  arena VARCHAR(100),
  PRIMARY KEY (team_id)
)
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE 'team_dedup.csv'
INTO TABLE team
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ',' ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES
  (league_id, team_abbrev, name, arena);

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

