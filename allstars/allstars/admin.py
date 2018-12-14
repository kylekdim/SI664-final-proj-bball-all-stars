from django.contrib import admin

import allstars.models as models

# Register your models here.

@admin.register(models.AllStar)
class AllStarAdmin(admin.ModelAdmin):
	fields = [
		'person_record',
		'year',
		'conference',
		'league',
		'games_played',
		'minutes',
		'points',
		'rebounds',
		'assists',
		'steals',
		'blocks',
		'turnovers',
		'ft_attempted',
		'ft_made',
		'three_attempted',
		'three_made'
	]

	list_display = [
		'year',
		'conference',
		'league',
		'games_played',
		'minutes',
		'points',
		'rebounds',
		'assists',
		'steals',
		'blocks',
		'turnovers',
		'ft_attempted',
		'ft_made',
		'three_attempted',
		'three_made'
	]

	list_filter = [
		'year',
		'conference',
		'league',
		]

# admin.site.register(models.AllStar)


@admin.register(models.Coach)
class CoachAdmin(admin.ModelAdmin):
	fields = ['person_record', 'year', 'team', 'league', 'won', 'lost']
	list_display = ['person_record', 'year', 'team']
	ordering = ['person_record', 'year', 'team', 'won', 'lost']

# admin.site.register(models.Coach)


@admin.register(models.TeamAlign)
class TeamAlignAdmin(admin.ModelAdmin):
	fields = [ 
    	'person_record',
    	'year',
    	'stint',
    	'team',
    	'league',
    	'games_played',
    	'minutes',
    	'points',
    	'assists'
	]

	list_display = [
    	'person_record',
    	'year',
    	'stint',
    	'team',
    	'league',
    	'games_played',
    	'minutes',
    	'points',
    	'assists'
	]

	list_filter = [
		'person_record',
		'year',
		'team',
		'league'
	]

# admin.site.register(models.TeamAlign)


@admin.register(models.League)
class LeagueAdmin(admin.ModelAdmin):
	fields = [
		'league_abbrev',
		'league_name'
	]

	list_display = [
		'league_abbrev',
		'league_name'
	]

	list_filter = [
		'league_abbrev'
	]

# admin.site.register(models.League)


@admin.register(models.PersonRecord)
class PersonRecordAdmin(admin.ModelAdmin):
	fields = [
		'person_record_id',
    	'person_id_long',
    	'first_name',
    	'middle_name',
    	'last_name',
    	'full_given_name',
    	'name_suffix',
    	'nickname',
    	'pos',
    	'height',
    	'weight',
    	'college',
    	'birthdate',
    	'birth_city',
    	'birth_state',
    	'birth_country',
    	'high_school',
    	'hs_city',
    	'hs_state',
    	'hs_country',
    	'death_date',
    	'race'
    ]
	list_display = ['first_name', 'last_name', 'person_id_long']
	ordering = ['last_name', 'birthdate']

# admin.site.register(models.PersonRecord)


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
	fields = ['league', 'team_abbrev', 'name']
	list_display = ['league', 'team_abbrev', 'name']
	ordering = ['league', 'team_abbrev', 'name']

# admin.site.register(models.Team)


@admin.register(models.TeamStat)
class TeamStatAdmin(admin.ModelAdmin):
	fields = ['team', 'year', 'home_won', 'home_lost', 'away_won', 'away_lost', 'neut_won', 'neut_lost', 'won', 'lost', 'games']
	list_display = ['team', 'year', 'home_won', 'home_lost', 'away_won', 'away_lost', 'neut_won', 'neut_lost', 'won', 'lost', 'games']
	ordering = ['team', 'year', 'won', 'lost']

# admin.site.register(models.TeamStat)
