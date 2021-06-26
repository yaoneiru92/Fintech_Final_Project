# Module 'reg_season_stats_2020_21'

## This module pulls and merges regular season stats for teams who made the 2020-21 Playoffs

import pandas as pd

# Playoff team dictionary with respective ids
playoff_teams = {
    "Dallas Mavericks":"",
    "LA Clippers":"1610612746",
    "Utah Jazz":"1610612762",
    "LA Lakers":"1610612747",
    "Milwaukee Bucks":"1610612749",
    "Miami Heat":"1610612748",
    "Boston Celtics":"1610612738",
    "Washington Wizards":"1610612764",
    "New York Knicks":"1610612752",
    "Denver Nuggets":"1610612743",
    "Atlanta Hawks":"1610612737",
    "Portland Trail Blazers":"1610612757",
    "Brooklyn Nets":"1610612751",
    "Memphis Grizzlies":"1610612763",
    "Phoenix Suns":"1610612756",
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
#     data = data[data.YEAR == '2020-21']

#     reg_season_stats.append(data)

#     return reg_season_stats
### --------------------------------------------------------------------------------------------------------------------------------------------------------

## Dallas Mavericks - DAL
DAL_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612742")
DAL_data = DAL_data.get_data_frames()[0]
DAL_data = DAL_data[DAL_data.YEAR == '2020-21']

## LA Clippers - LAC
LAC_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612746")
LAC_data = LAC_data.get_data_frames()[0]
LAC_data = LAC_data[LAC_data.YEAR == '2020-21']

## Utah Jazz - UTA
UTA_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612762")
UTA_data = UTA_data.get_data_frames()[0]
UTA_data = UTA_data[UTA_data.YEAR == '2020-21']

## LA Lakers - LAL
LAL_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612747")
LAL_data = LAL_data.get_data_frames()[0]
LAL_data = LAL_data[LAL_data.YEAR == '2020-21']

## Milwaukee Bucks - MIL
MIL_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612749")
MIL_data = MIL_data.get_data_frames()[0]
MIL_data = MIL_data[MIL_data.YEAR == '2020-21']

## Miami Heat - MIA
MIA_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612748")
MIA_data = MIA_data.get_data_frames()[0]
MIA_data = MIA_data[MIA_data.YEAR == '2020-21']

## Boston Celtics - BOS
BOS_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612738")
BOS_data = BOS_data.get_data_frames()[0]
BOS_data = BOS_data[BOS_data.YEAR == '2020-21']

## Washington Wizards - WAS
WAS_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612764")
WAS_data = WAS_data.get_data_frames()[0]
WAS_data = WAS_data[WAS_data.YEAR == '2020-21']

## New York Knicks - NYK
NYK_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612752")
NYK_data = NYK_data.get_data_frames()[0]
NYK_data = NYK_data[NYK_data.YEAR == '2020-21']

## Denver Nuggets - DEN
DEN_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612743")
DEN_data = DEN_data.get_data_frames()[0]
DEN_data = DEN_data[DEN_data.YEAR == '2020-21']

## Atlanta Hawks - ATL
ATL_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612737")
ATL_data = ATL_data.get_data_frames()[0]
ATL_data = ATL_data[ATL_data.YEAR == '2020-21']

## Portland Trail Blazers - POR
POR_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612757")
POR_data = POR_data.get_data_frames()[0]
POR_data = POR_data[POR_data.YEAR == '2020-21']

## Brooklyn Nets - BKN
BKN_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612751")
BKN_data = BKN_data.get_data_frames()[0]
BKN_data = BKN_data[BKN_data.YEAR == '2020-21']

## Memphis Grizzlies
MEM_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612763")
MEM_data = MEM_data.get_data_frames()[0]
MEM_data = MEM_data[MEM_data.YEAR == '2020-21']

## Phoenix Suns - PHX
PHX_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612756")
PHX_data = PHX_data.get_data_frames()[0]
PHX_data = PHX_data[PHX_data.YEAR == '2020-21']

## Philadelphia 76ers - PHI
PHI_data = teamyearbyyearstats.TeamYearByYearStats(league_id="00",
                                                   per_mode_simple = "PerGame",
                                                   season_type_all_star = "Regular Season",
                                                   team_id="1610612755")
PHI_data = PHI_data.get_data_frames()[0]
PHI_data = PHI_data[PHI_data.YEAR == '2020-21']

data_frames = [DAL_data, 
               LAC_data, 
               UTA_data, 
               LAL_data, 
               MIL_data, 
               MIA_data, 
               BOS_data, 
               WAS_data, 
               NYK_data, 
               DEN_data, 
               ATL_data, 
               POR_data, 
               BKN_data, 
               MEM_data, 
               PHX_data, 
               PHI_data
               ]

reg_season_2021_stats = pd.concat(data_frames)

# Output main df to csv
reg_season_2021_stats.to_csv('csv_files/reg_season_2021_stats.csv')