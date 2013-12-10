import requests


class HTTPException(Exception):
    pass

class LoLAPI():

    def __init__(self, api_key, region='na'):
        self.region = region
        self.api_key = api_key
        self.key_end = '?api_key=' + self.api_key
        self.base_url = "http://prod.api.pvp.net/api/lol/" + self.region + "/v1.1"
        self.team_base_url = "http://prod.api.pvp.net/api/" + self.region + "/v2.1"

    """ SUMMONER INFO """
    def get_summoner_by_id(self, id):
        url = self.base_url + '/summoner/' + str(id) + self.key_end
        return self.send_req(url)

    def get_summoners_by_id(self, ids):
        ids = map(str, ids)
        url = self.base_url + '/summoner/' + ",".join(ids) + '/name' + self.key_end
        return self.send_req(url)

    def get_summoner_by_name(self, name):
        url = self.base_url + '/summoner/by-name/' + name + self.key_end
        return self.send_req(url)

    def get_rune_pages_by_id(self, id):
        url = self.base_url + '/summoner/' + str(id) + '/runes' + self.key_end
        return self.send_req(url)

    def get_rune_pages_by_summoner(self, summoner):
        json_dict = self.get_summoner_by_name(summoner)
        summoner_id = json_dict['id']
        return self.get_rune_pages_by_id(summoner_id)

    def get_masteries_by_id(self, id):
        url = self.base_url + '/summoner/' + str(id) + '/masteries' + self.key_end
        return self.send_req(url)

    def get_masteries_by_summoner(self, summoner):
        json_dict = self.get_summoner_by_name(summoner)
        summoner_id = json_dict['id']
        return self.get_masteries_by_id(summoner_id)

    """ TEAMS """
    def get_teams_for_id(self, id):
        url = self.team_base_url + '/team/by-summoner/' + str(id) + self.key_end
        return self.send_req(url)

    def get_teams_for_summoner(self, summoner):
        json_dict = self.get_summoner_by_name(summoner)
        summoner_id = json_dict['id']
        return self.get_teams_for_id(summoner_id)

    """ STATS """
    def get_normal_stats_by_id(self, id, season=None):
        url = self.base_url + '/stats/by-summoner/' + str(id) + '/summary'
        if season == 3:
            url += '?season=SEASON3&' + self.key_end[1:]
        elif season == 4:
            url += '?season=SEASON4&' + self.key_end[1:]
        else:
            url += self.key_end
        return self.send_req(url)

    def get_normal_stats_by_summoner(self, summoner, season=None):
        json_dict = self.get_summoner_by_name(summoner)
        summoner_id = json_dict['id']
        return self.get_normal_stats_by_id(summoner_id, season)

    def get_ranked_stats_by_id(self, id, season=None):
        url = self.base_url + '/stats/by-summoner/' + str(id) + '/ranked'
        if season == 3:
            url += '?season=SEASON3&' + self.key_end[1:]
        elif season == 4:
            url += '?season=SEASON4&' + self.key_end[1:]
        else:
            url += self.key_end
        return self.send_req(url)

    def get_ranked_stats_by_summoner(self, summoner, season=None):
        json_dict = self.get_summoner_by_name(summoner)
        summoner_id = json_dict['id']
        return self.get_ranked_stats_by_id(summoner_id, season)

    """ LEAGUES """
    def get_league_data_by_id(self, id):
        url = self.team_base_url + '/league/by-summoner/' + str(id) + self.key_end
        return self.send_req(url)

    def get_league_data_by_summoner(self, summoner):
        json_dict = self.get_summoner_by_name(summoner)
        summoner_id = json_dict['id']
        return self.get_league_data_by_id(summoner_id)

    """ GAMES """
    def get_recent_games_by_id(self, id):
        url = self.base_url + '/game/by-summoner/' + str(id) + '/recent' + self.key_end
        return self.send_req(url)

    def get_recent_games_by_summoner(self, summoner):
        json_dict = self.get_summoner_by_name(summoner)
        summoner_id = json_dict['id']
        return self.get_recent_games_by_id(summoner_id)

    """ CHAMPIONS """
    def get_all_champions(self):
        url = self.base_url + '/champion' + self.key_end
        return self.send_req(url)

    def get_free_champions(self):
        url = self.base_url + '/champion?freeToPlay=true&' + self.key_end[1:]
        return self.send_req(url)

    """ INTERNAL FUNCS """
    def send_req(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        else:
            return self.get_status_error(r.status_code)


    def get_status_error(self, status):
        if status == 400:
            raise HTTPException("400 error - bad request")
        elif status == 401:
            raise HTTPException("401 error - invalid URL")
        elif status == 404:
            raise HTTPException("404 error - summoner not found")
        elif status == 500:
            raise HTTPException("500 error - internal server error")
        else:
            raise HTTPException(str(status) + " error - unknown")

