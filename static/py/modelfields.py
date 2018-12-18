#all star fields

fk = person_record, league

all_star_id
person_record 
year
conference
league 
games_played
minutes 
points 
rebounds
assists
steals 
blocks 
turnovers 
ft_attempted
ft_made
three_attempted 
three_made

'all_star_id', 'person_record', 'year', 'conference', 'league', 'games_played', 'minutes', 'points', 'rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'ft_attempted', 'ft_made', 'three_attempted', 'three_made'

#league

league_id 
league_abbrev 
league_name

'league_id', 'league_abbrev', 'league_name'

#team

team_id
league
team_abbrev
name

'team_id', 'league', 'team_abbrev', 'name'

#person record

person_record_id 
person_id_long
first_name 
middle_name
last_name
full_given_name
name_suffix
nickname
pos
height
weight
college 
birthdate
birth_city 
birth_state
birth_country 
high_school 
hs_city 
hs_state 
hs_country 
death_date
race 

'person_record_id', 'person_id_long', 'first_name', 'middle_name', 'last_name', 'full_given_name', 'name_suffix', 'nickname', 'pos', 'height', 'weight', 'college', 'birthdate', 'birth_city', 'birth_state', 'birth_country', 'high_school', 'hs_city', 'hs_state', 'hs_country', 'death_date', 'race' 


#team align
team_align_id
person_record
year
stint
team
league
games_played
minutes
points
assists

'team_align_id', 'person_record', 'year', 'stint', 'team', 'league', 'games_played', 'minutes', 'points', 'assists'


# Coach(models.Model):
coach_id 
person_record 
year 
team 
league 
won
lost

'coach_id', 'person_record', 'year', 'team', 'league', 'won', 'lost'



#TeamStat(models.Model):
    
team_stat_id
team 
year 
home_won 
home_lost 
away_won
away_lost 
neut_won 
neut_lost
won 
lost
games 

'team_stat_id', 'team', 'year', 'home_won', 'home_lost', 'away_won', 'away_lost', 'neut_won', 'neut_lost', 'won', 'lost', 'games' 




