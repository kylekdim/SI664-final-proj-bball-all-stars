# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllStar(models.Model):
    all_star_id = models.AutoField(primary_key=True)
    person_record = models.ForeignKey('PersonRecord', models.DO_NOTHING)
    year = models.IntegerField()
    conference = models.CharField(max_length=20, blank=True, null=True)
    league = models.ForeignKey('League', models.DO_NOTHING)
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
        ordering = ['player_record__last_name']
        verbose_name = 'Basketball All Star Records'
        verbose_name_plural = 'Basketball All Star Records'

    def __str__(self):
        return self.player_record__first_name + self.player_record__last_name

    def get_absolute_url(self):
        return reverse('country_detail', args=[str(self.id)])


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class League(models.Model):
    league_id = models.AutoField(primary_key=True)
    league_abbrev = models.CharField(unique=True, max_length=10)
    league_name = models.CharField(db_column='League_name', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'league'

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    league = models.ForeignKey(League, models.DO_NOTHING)
    team_abbrev = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'team'


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
    birthdate = models.CharField(max_length=20, blank=True, null=True)
    birth_city = models.CharField(max_length=50, blank=True, null=True)
    birth_state = models.CharField(max_length=20, blank=True, null=True)
    birth_country = models.CharField(max_length=50, blank=True, null=True)
    high_school = models.CharField(max_length=50, blank=True, null=True)
    hs_city = models.CharField(max_length=50, blank=True, null=True)
    hs_state = models.CharField(max_length=20, blank=True, null=True)
    hs_country = models.CharField(max_length=30, blank=True, null=True)
    death_date = models.CharField(max_length=20, blank=True, null=True)
    race = models.CharField(max_length=3, blank=True, null=True)

    # Intermediate model (team -> team_align <- person_record)
    teams_as_player = models.ManyToManyField(
        Team,
        through='TeamAlign',
        related_name='players'
    )

    # Intermediate model (team -> coach <- person_record)
    teams_as_coach = models.ManyToManyField(
        Team,
        through='Coach',
        related_name='coaches'
    )

    class Meta:
        managed = False
        db_table = 'person_record'


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

class Coach(models.Model):
    coach_id = models.AutoField(primary_key=True)
    person_record = models.ForeignKey('PersonRecord', models.DO_NOTHING)
    year = models.IntegerField()
    team = models.ForeignKey('Team', models.DO_NOTHING)
    league = models.ForeignKey('League', models.DO_NOTHING)
    won = models.IntegerField(blank=True, null=True)
    lost = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coach'

class TeamStat(models.Model):
    team_stat_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, models.DO_NOTHING)
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
