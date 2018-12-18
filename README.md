# SI664-final-proj-bball-all-stars


## Purpose

Create a fully functional Django database of player/coach/team/all-star records with the Kaggle Men's Basketball dataset.

## Data set

[Men's Basketball Dataset](https://www.kaggle.com/open-source-sports/mens-professional-basketball) from [Kaggle](https://www.kaggle.com/)

## Data model

![AllStars Data Model](https://github.com/kylekdim/SI664-final-proj-bball-all-stars/blob/master/static/img/allstars_model_final.png "AllStars Final Data Model")

Refer to [mwb_models](https://github.com/kylekdim/SI664-Final-Project-Mens-Basketball/tree/master/mwb_models) for the raw mysql model file.

Table Overview (7):
AllStar: A table with each row representing a year that a player(PersonRecord) played on a league's All-Star Team, and accompanying play stats.
League: A table of leagues where each row represents a professional basketball league.
Team: A table of teams where each row represents a professional basketball team, and its name/league details.
TeamAlign: A table with each row representing a year that a person played for a team, and accompanying play stats during that stint.
Coach: A table with each row representing a year that a person coached for a team, and their accompanying play record for that year.
TeamStat: A table with each row representing a year a team played during the regular season, and their teamwide performance and record.
PersonRecord: A table with each row representing a player or coach of a professional basketball league. Many-to-many relationship with Team and/or Coach depending on the individual.

## Package Dependencies

|Package                      | Version  |
|:----------------------------|---------:|
|beautifulsoup4|                 4.6.3   | 
|bs4           |                 0.0.1    |
|certifi        |                2018.8.24|
|chardet        |                3.0.4    |
|coreapi        |               2.3.3    |
|coreschema    |                 0.0.4    |
|decorator      |                4.3.0    |
|defusedxml      |               0.5.0    |
|Django           |              2.1.4    |
|django-allauth    |             0.38.0   |
|django-cors-headers|            2.4.0    |
|django-crispy-forms |           1.7.2    |
|django-filter        |          2.0.0    |
|django-rest-auth      |         0.9.3    |
|django-rest-swagger   |         2.2.0    |
|django-test-without-migrations| 0.6      |
|djangorestframework         |   3.9.0    |
|idna                         |  2.7      |
|ipython-genutils              | 0.2.0    |
|itypes       |                  1.1.0    |
|Jinja2        |                 2.10     |
|jsonschema     |                2.6.0    |
|jupyter-core    |               4.4.0    |
|MarkupSafe       |              1.1.0    |
|mysqlclient       |             1.3.13   |
|nbformat           |            4.4.0    |
|nltk                |           3.3      |
|numpy                |          1.15.1   |
|oauthlib              |         2.1.0    |
|openapi-codec          |        1.3.2    |
|pandas                  |       0.23.4   |
|pip                      |      18.0     |
|plotly                    |     3.4.0    |
|PyJWT                      |    1.7.1    |
|python-dateutil             |   2.7.3    |
|python3-openid  |               3.1.0    |
|pytz             |              2018.5   |
|PyYAML            |             3.13     |
|requests           |            2.19.1   |
|requests-oauthlib   |           1.0.0    |
|retrying             |          1.3.3    |
|selenium              |         3.141.0  |
|setuptools             |        40.2.0   |
|simplejson              |       3.16.0   |
|six                      |      1.11.0   |
|social-auth-app-django    |     3.1.0    |
|social-auth-core           |    2.0.0    |
|traitlets                   |   4.3.2    |
|uritemplate          |          3.0.0    |
|urllib3               |         1.23     |
|virtualenv             |        16.0.0   |
|wheel                   |       0.31.1   |
