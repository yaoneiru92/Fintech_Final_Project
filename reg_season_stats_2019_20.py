# Module 'reg_season_stats_2019_20'

## This module pulls and merges regular season stats for teams who made the 2019-20 Playoffs

import pandas as pd

# Playoff team dictionary with respective ids
playoff_teams = {
    "Dallas Mavericks":"1610612742",
    "LA Clippers":"1610612746",
    "Utah Jazz":"1610612762",
    "LA Lakers":"1610612747",
    "Milwaukee Bucks":"1610612749",
    "Miami Heat":"1610612748",
    "Boston Celtics":"1610612738",
    "Toronto Raptors":"1610612761",
    "Houston Rockets":"1610612745",
    "Denver Nuggets":"1610612743",
    "Orlando Magic":"1610612753",
    "Portland Trail Blazers":"1610612757",
    "Brooklyn Nets":"1610612751",
    "Oklahoma City Thunder":"1610612760",
    "Indiana Pacers":"1610612754",
    "Philadelphia 76ers":"1610612755",
}

from nba_api.stats.endpoints import teamyearbyyearstats

### --------------------------------------------------------------------------------------------------------------------------------------------------------
# # WARNING: this code should work but I did not get a chance to fully test it because of read time error

# # Iterate through dictionary 
# for key in playoff_teams:
#     # Create empty dataframe to hold regular season stats for playoff teams
#     reg_season_stats = []

#     data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
#                                                    per_mode_simple = "PerGame",
#                                                    season_type_all_star = "Regular Season",
#                                                    team_id=playoff_teams[key])
#     data = data.get_data_frames()[0]
#     data = data[data.YEAR == '2019-20']

#     reg_season_stats.append(data)

#     return reg_season_stats
### --------------------------------------------------------------------------------------------------------------------------------------------------------

# Alternative: copy and paste long version of loop

## Dallas Mavericks - DAL
DAL_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612742")
DAL_data = DAL_data.get_data_frames()[0]
DAL_data = DAL_data[DAL_data.YEAR == '2019-20']

## LA Clippers - LAC
LAC_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612746")
LAC_data = LAC_data.get_data_frames()[0]
LAC_data = LAC_data[LAC_data.YEAR == '2019-20']

## Utah Jazz - UTA
UTA_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612762")
UTA_data = UTA_data.get_data_frames()[0]
UTA_data = UTA_data[UTA_data.YEAR == '2019-20']

## LA Lakers - LAL
LAL_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612747")
LAL_data = LAL_data.get_data_frames()[0]
LAL_data = LAL_data[LAL_data.YEAR == '2019-20']

## Milwaukee Bucks - MIL
MIL_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612749")
MIL_data = MIL_data.get_data_frames()[0]
MIL_data = MIL_data[MIL_data.YEAR == '2019-20']

## Miami Heat - MIA
MIA_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612748")
MIA_data = MIA_data.get_data_frames()[0]
MIA_data = MIA_data[MIA_data.YEAR == '2019-20']

## Boston Celtics - BOS
BOS_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612738")
BOS_data = BOS_data.get_data_frames()[0]
BOS_data = BOS_data[BOS_data.YEAR == '2019-20']

## Toronto Raptors - TOR
TOR_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612761")
TOR_data = TOR_data.get_data_frames()[0]
TOR_data = TOR_data[TOR_data.YEAR == '2019-20']

## Houston Rockets - HOU
HOU_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612745")
HOU_data = HOU_data.get_data_frames()[0]
HOU_data = HOU_data[HOU_data.YEAR == '2019-20']

## Denver Nuggets - DEN
DEN_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612743")
DEN_data = DEN_data.get_data_frames()[0]
DEN_data = DEN_data[DEN_data.YEAR == '2019-20']

## Orlando Magic - ORL
ORL_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612753")
ORL_data = ORL_data.get_data_frames()[0]
ORL_data = ORL_data[ORL_data.YEAR == '2019-20']

## Portland Trail Blazers - POR
POR_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612757")
POR_data = POR_data.get_data_frames()[0]
POR_data = POR_data[POR_data.YEAR == '2019-20']

## Brooklyn Nets - BKN
BKN_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612751")
BKN_data = BKN_data.get_data_frames()[0]
BKN_data = BKN_data[BKN_data.YEAR == '2019-20']

## Oklahoma City Thunder - OKC
OKC_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612760")
OKC_data = OKC_data.get_data_frames()[0]
OKC_data = OKC_data[OKC_data.YEAR == '2019-20']

## Indiana Pacers - IND
IND_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612754")
IND_data = IND_data.get_data_frames()[0]
IND_data = IND_data[IND_data.YEAR == '2019-20']

## Philadelphia 76ers - PHI
PHI_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612755")
PHI_data = PHI_data.get_data_frames()[0]
PHI_data = PHI_data[PHI_data.YEAR == '2019-20']

data_frames = [DAL_data, 
               LAC_data, 
               UTA_data, 
               LAL_data, 
               MIL_data, 
               MIA_data, 
               BOS_data, 
               TOR_data, 
               HOU_data, 
               DEN_data, 
               ORL_data, 
               POR_data, 
               BKN_data, 
               OKC_data, 
               IND_data, 
               PHI_data
               ]

reg_season_1920_stats = pd.concat(data_frames)

# Output main df to csv
reg_season_1920_stats.to_csv('csv_files/reg_season_1920_stats.csv')