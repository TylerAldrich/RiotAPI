LoLAPI
===

riot.py is a simple python wrapper for the new Riot Games API.

This module requires a Riot API Key and the Requests python module.

Learn more about Requests from here: http://requests.readthedocs.org/en/latest/


This module provides some convenience functionality. You are able to make all API calls by just providing the summoner name, instead of having to call get_summoner_by_name and getting the ID from the returned JSON.

An example of using the module:

```
from riot import LoLAPI

key = "<YOUR API KEY>"
api = LoLAPI(key)

# Get summonor info by id
print api.get_summoner_by_id(20385910)

# Get multiple summoners info
print api.get_summoners_by_id([20385910, 21684331])

# Get summoner info by name
print api.get_summoner_by_name("N1nj4l3m0n")

# Get rune pages for a summoner by id
print api.get_rune_pages_by_id(20385910)

# Get rune pages for a summoner by name
print api.get_rune_pages_by_summoner("N1nj4l3m0n")

# Get mastery info by summoner id
print api.get_masteries_by_id(20385910)

# Get mastery info by summoner name
print api.get_masteries_by_summoner("N1nj4l3m0n")

# Get teams info by summoner id
print api.get_teams_for_id(20385910)

# Get teams info by summoner name
print api.get_teams_for_summoner("N1nj4l3m0n")

# Get ranked stats by summoner id
print api.get_ranked_stats_by_id(20385910)

# You can get ranked stats for normals/ranked with an ID or Summoner name,
# and can specify season=3, season=4, or nothing (defaults to all seasons)
print api.get_normal_stats_by_id(20385910, season=3)

# Gets normal stats for given summoner name
print api.get_normal_stats_by_summoner("N1nj4l3m0n")

# Gets ranked stats for given summoner name
print api.get_ranked_stats_by_summoner("N1nj4l3m0n")

# Gets league data by summoner id
print api.get_league_data_by_id(20385910)

# Gets league data by summoner name
print api.get_league_data_by_summoner("N1nj4l3m0n")

# Gets all recent games by summoner id
print api.get_recent_games_by_id(20385910)

# Gets all recent games by summoner name
print api.get_recent_games_by_summoner("N1nj4l3m0n")

# Gets all champions
print api.get_all_champions()

# Gets all current free champions
print api.get_free_champions()

```
