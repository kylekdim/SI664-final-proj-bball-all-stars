from allstars.models import *
from rest_framework import response, serializers, status

class LeagueSerializer(serializers.ModelSerializer):

	class Meta:
		model = League
		fields = ('league_id', 'league_abbrev', 'league_name')

class TeamSerializer(serializers.ModelSerializer):

	class Meta:
		model = Team
		fields = ('team_id', 'league', 'team_abbrev', 'name')

class TeamStatSerializer(serializers.ModelSerializer):
	team = TeamSerializer(many=False, read_only=True)
	class Meta:
		model = TeamStat
		fields = ('team_stat_id', 'team', 'year', 'home_won', 'home_lost', 'away_won', 'away_lost', 'neut_won', 'neut_lost', 'won', 'lost', 'games')

class TeamAlignSerializer(serializers.ModelSerializer):
	#person_record = PersonRecordSerializer(many=False, read_only=True)
	team = TeamSerializer(many=False, read_only=True)
	league = LeagueSerializer(many=False, read_only=True)


	class Meta:
		model = TeamAlign
		fields = ('team_align_id', 'person_record', 'year', 'stint', 'team', 'league', 'games_played', 'minutes', 'points', 'assists')


class CoachSerializer(serializers.ModelSerializer):
	#person_record = PersonRecordSerializer(many=False, read_only=True)
	team = TeamSerializer(many=False, read_only=True)
	league = LeagueSerializer(many=False, read_only=True)

	class Meta:
		model = Coach
		fields = ('coach_id', 'person_record', 'year', 'team', 'league', 'won', 'lost')

class PersonRecordSerializer(serializers.ModelSerializer):
	person_id_long = serializers.CharField(
		allow_blank=False,
		max_length=10
	)
	first_name = serializers.CharField(
		allow_blank=True
	)
	middle_name = serializers.CharField(
		allow_blank=True
	)
	last_name = serializers.CharField(
		allow_blank=False
	)
	full_given_name = serializers.CharField(
		allow_blank=True
	)
	name_suffix = serializers.CharField(
		allow_blank=True
	)
	nickname = serializers.CharField(
		allow_blank=True
	)
	pos = serializers.CharField(
		allow_blank=True
	)
	height = serializers.IntegerField(
		allow_null=True
	)
	weight = serializers.IntegerField(
		allow_null=True
	)
	college = serializers.CharField(
		allow_blank=True
	)
	birthdate = serializers.CharField(
		allow_blank=True
	)

	birth_city = serializers.CharField(
		allow_blank=True
	)

	birth_state = serializers.CharField(
		allow_blank=True
	)

	birth_country = serializers.CharField(
		allow_blank=True
	) 

	high_school = serializers.CharField(
		allow_blank=True
	)

	hs_city = serializers.CharField(
		allow_blank=True
	)

	hs_state = serializers.CharField(
		allow_blank=True
	)

	hs_country = serializers.CharField(
		allow_blank=True
	)

	death_date = serializers.CharField(
		allow_blank=True
	)

	race = serializers.CharField(
		allow_blank=True
	)


	team_align = TeamAlignSerializer(
		source='team_align_set', # Note use of _set
		many=True,
		read_only=True
	)

	team_ids = serializers.PrimaryKeyRelatedField(
		many=True,
		write_only=True,
		queryset=Team.objects.all(),
		source='team_align'
	)

	coach = CoachSerializer(
		source='coach_set',
		many=True,
		read_only=True
	)

	class Meta:
		model = PersonRecord
		fields = ('person_record_id', 'person_id_long', 'first_name', 'middle_name', 'last_name', 'full_given_name', 'name_suffix', 'nickname', 'pos', 'height', 'weight', 'college', 'birthdate', 'birth_city', 'birth_state', 'birth_country', 'high_school', 'hs_city', 'hs_state', 'hs_country', 'death_date', 'race', 'team_align', 'team_ids', 'coach')

	def create(self, validated_data):
		"""
		This method persists a new HeritageSite instance as well as adds all related
		countries/areas to the heritage_site_jurisdiction table.  It does so by first
		removing (validated_data.pop('heritage_site_jurisdiction')) from the validated
		data before the new HeritageSite instance is saved to the database. It then loops
		over the heritage_site_jurisdiction array in order to extract each country_area_id
		element and add entries to junction/associative heritage_site_jurisdiction table.
		:param validated_data:
		:return: site
		"""

		# print(validated_data)

		teams_coach = validated_data.pop('coach')
		teams_player = validated_data.pop('team_align')
		person = PersonRecord.objects.create(**validated_data)

		if teams_coach is not None:
			for team in teams_coach:
				coach.objects.create(
					person_record_id=person.person_record_id,
					team_id=teams_coach.team_id
				)

		if teams_player is not None:
			for team in teams_player:
				team_align.objects.create(
					person_record_id=person.person_record_id,
					team_id=teams_coach.team_id
				)


		return person

	def update(self, instance, validated_data):
		# site_id = validated_data.pop('heritage_site_id')
		person_record_id = instance.person_record_id
		new_teams_coach = validated_data.pop('coach')
		new_teams_player = validated_data.pop('team_align')


		instance.person_id_long = validated_data.get(
			'person_id_long',
			instance.person_id_long
		)

		instance.first_name = validated_data.get(
			'first_name',
			instance.first_name
		)
		 
		instance.middle_name = validated_data.get(
			'middle_name',
			instance.middle_name
		)
		
		instance.last_name = validated_data.get(
			'last_name',
			instance.last_name
		)
		
		instance.full_given_name = validated_data.get(
			'full_given_name',
			instance.full_given_name
		)
		
		instance.name_suffix = validated_data.get(
			'name_suffix',
			instance.name_suffix
		)
		
		instance.nickname = validated_data.get(
			'nickname',
			instance.nickname
		)
		
		instance.pos = validated_data.get(
			'pos',
			instance.pos
		)
		
		instance.height = validated_data.get(
			'height',
			instance.height
		)
		
		instance.weight = validated_data.get(
			'weight',
			instance.weight
		)
		
		instance.college = validated_data.get(
			'college',
			instance.college
		)
		
		instance.birthdate = validated_data.get(
			'birthdate',
			instance.birthdate
		)
		
		instance.birth_city = validated_data.get(
			'birth_city',
			instance.birth_city
		)
		
		instance.birth_state = validated_data.get(
			'birth_state',
			instance.birth_state
		)
		
		instance.birth_country = validated_data.get(
			'birth_country',
			instance.birth_country
		)
		
		instance.high_school = validated_data.get(
			'high_school',
			instance.high_school
		)
		
		instance.hs_city = validated_data.get(
			'hs_city',
			instance.hs_city
		)
		
		instance.hs_state = validated_data.get(
			'hs_state',
			instance.hs_state
		)
		
		instance.hs_country = validated_data.get(
			'hs_country',
			instance.hs_country
		)
		
		instance.death_date = validated_data.get(
			'death_date',
			instance.death_date
		)
		
		instance.race = validated_data.get(
			'race',
			instance.race
		)
		
		instance.save()

		return instance




class AllStarSerializer(serializers.ModelSerializer):
	person_record = PersonRecordSerializer(many=False, read_only=True)
	league = LeagueSerializer(many=False, read_only=True)

	class Meta:
		model = AllStar
		fields = ('all_star_id', 'person_record', 'year', 'conference', 'league', 'games_played', 'minutes', 'points', 'rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'ft_attempted', 'ft_made', 'three_attempted', 'three_made')








