# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse
import datetime


class AllStar(models.Model):
    all_star_id = models.AutoField(primary_key=True)
    person_record = models.ForeignKey('PersonRecord', on_delete=models.PROTECT)
    year = models.IntegerField()
    conference = models.CharField(max_length=20, blank=True, null=True)
    league = models.ForeignKey('League', on_delete=models.PROTECT)
    games_played = models.IntegerField(blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    rebounds = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    steals = models.IntegerField(blank=True, null=True)
    blocks = models.IntegerField(blank=True, null=True)
    turnovers = models.IntegerField(blank=True, null=True)
    ft_attempted = models.IntegerField(blank=True, null=True)
    ft_made = models.IntegerField(blank=True, null=True)
    three_attempted = models.IntegerField(blank=True, null=True)
    three_made = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_star'
        ordering = ['person_record__last_name', 'person_record__first_name', 'league__league_name']
        verbose_name = 'Basketball All Star Records'
        verbose_name_plural = 'Basketball All Star Records'

    def __str__(self):
        return self.person_record.first_name + self.person_record.last_name

    def get_absolute_url(self):
        return reverse('all_star_detail', args=[str(self.id)])


class League(models.Model):
    league_id = models.AutoField(primary_key=True)
    league_abbrev = models.CharField(unique=True, max_length=10)
    league_name = models.CharField(db_column='League_name', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'league'
        ordering = ['league_name']
        verbose_name = "Men's Professional Basketball League"
        verbose_name_plural = "Men's Professional Basketball Leagues"

    def __str__(self):
        return self.league_name

    #def get_absolute_url(self):
        #return reverse('', args=[str(self.id)])


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    league = models.ForeignKey(League, on_delete=models.PROTECT)
    team_abbrev = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'team'
        ordering = ['name']
        verbose_name = "Men's Professional Basketball Team"
        verbose_name_plural = "Men's Professional Basketball Teams"

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
        #return reverse('', args=[str(self.id)])


class PersonRecord(models.Model):
    person_record_id = models.AutoField(primary_key=True)
    person_id_long = models.CharField(unique=True, max_length=10)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    full_given_name = models.CharField(max_length=100, blank=True, null=True)
    name_suffix = models.CharField(max_length=5, blank=True, null=True)
    nickname = models.CharField(max_length=30, blank=True, null=True)
    pos = models.CharField(max_length=10, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    college = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    birth_city = models.CharField(max_length=50, blank=True, null=True)
    birth_state = models.CharField(max_length=20, blank=True, null=True)
    birth_country = models.CharField(max_length=50, blank=True, null=True)
    high_school = models.CharField(max_length=50, blank=True, null=True)
    hs_city = models.CharField(max_length=50, blank=True, null=True)
    hs_state = models.CharField(max_length=20, blank=True, null=True)
    hs_country = models.CharField(max_length=30, blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    race = models.CharField(max_length=3, blank=True, null=True)

    # Intermediate model (team -> team_align <- person_record)
    teams_as_player = models.ManyToManyField(
        Team,
        through='TeamAlign',
        blank=True,
        related_name='player_on_team'
    )

    # Intermediate model (team -> coach <- person_record)
    teams_as_coach = models.ManyToManyField(
        Team,
        through='Coach',
        blank=True,
        related_name='coach_on_team',
    )

    class Meta:
        managed = False
        db_table = 'person_record'
        ordering = ['last_name','first_name']
        verbose_name = "Men's Professional Basketball Player/Coach"
        verbose_name_plural = "Men's Professional Basketball Players/Coaches"

    def __str__(self):
        return self.first_name + self.last_name

    #def get_absolute_url(self):
        #return reverse('', args=[str(self.id)])

    @property
    def team_names_player(self):
        sort_order = ['team_align__team__team_name']
        teams = self.teams_as_player.select_related('team_align').order_by(*sort_order)

        names = []
        for team in teams:
            name = team.team_align.team_name
            if name not in names:
                names.append(name)

        return ', '.join(names)

    @property
    def team_names_coach(self):
        sort_order = ['coach__team__team_name']
        teams = self.teams_as_coach.select_related('coach').order_by(*sort_order)

        names = []
        for team in teams:
            name = team.team_align.team_name
            if name not in names:
                names.append(name)

        return ', '.join(names)


class TeamAlign(models.Model):
    team_align_id = models.AutoField(primary_key=True)
    person_record = models.ForeignKey(PersonRecord, on_delete=models.CASCADE)
    year = models.IntegerField()
    stint = models.IntegerField(blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    games_played = models.IntegerField(blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_align'
        ordering = ['team__name']
        verbose_name = "Men's Professional Basketball Player/Team Alignment"
        verbose_name_plural = "Men's Professional Basketball Player/Team Alignment"

    def __str__(self):
        return self.person_record.first_name + self.person_record.last_name

    #def get_absolute_url(self):
        #return reverse('', args=[str(self.id)])


class Coach(models.Model):
    coach_id = models.AutoField(primary_key=True)
    person_record = models.ForeignKey('PersonRecord', on_delete=models.PROTECT)
    year = models.IntegerField()
    team = models.ForeignKey('Team', on_delete=models.PROTECT)
    league = models.ForeignKey('League', on_delete=models.PROTECT)
    won = models.IntegerField(blank=True, null=True)
    lost = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coach'
        ordering = ['person_record__last_name', 'person_record__first_name']
        verbose_name = "Men's Professional Basketball Coach/Team Alignment"
        verbose_name_plural = "Men's Professional Basketball Coach/Team Alignment"

    def __str__(self):
        return self.person_record.first_name + self.person_record.last_name

    #def get_absolute_url(self):
        #return reverse('', args=[str(self.id)])


class TeamStat(models.Model):
    team_stat_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    year = models.IntegerField()
    home_won = models.IntegerField()
    home_lost = models.IntegerField()
    away_won = models.IntegerField()
    away_lost = models.IntegerField()
    neut_won = models.IntegerField()
    neut_lost = models.IntegerField()
    won = models.IntegerField()
    lost = models.IntegerField()
    games = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_stat'
        ordering = ['year', 'team__name']
        verbose_name = "Men's Professional Basketball Team Stats"
        verbose_name_plural = "Men's Professional Basketball Team Stats"

    def __str__(self):
        return str(self.team_stat_id)

    #def get_absolute_url(self):
        #return reverse('', args=[str(self.id)])
