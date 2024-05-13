import http.client
import json
import pandas as pd
import game_playing.config.project_variables as pv


def ingest_mlb():
    data_list = []

    conn = http.client.HTTPSConnection("statsapi.mlb.com")
    payload = ''
    headers = {}
    conn.request("GET", f"/api/v1/schedule/games/?sportId=1&startDate={pv.thirty_days}&endDate={pv.today}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    game_dates = json.loads(data)['dates']

    for date in game_dates:
        games = date['games']
        for game in games:
            if 'score' in game:
                data_list.append(['MLB', game['gamePk'], game['officialDate'], game['status']['abstractGameState'], game['gameType'],
                              game['teams']['home']['score'], game['teams']['away']['score'],
                              game['teams']['home']['team']['id'], game['teams']['home']['team']['name'], game['teams']['away']['team']['id'], game['teams']['away']['team']['name']])
            else:
                data_list.append(
                    ['MLB', game['gamePk'], game['officialDate'], game['status']['abstractGameState'], game['gameType'],
                     None, None,
                     game['teams']['home']['team']['id'], game['teams']['home']['team']['name'], game['teams']['away']['team']['id'], game['teams']['away']['team']['name']])

    df = pd.DataFrame(data_list, columns=['league', 'game_id', 'game_date', 'game_postseason_flg', 'game_status', 'game_home_tm_score', 'game_road_tm_score', 'home_tm_id', 'home_team_nm', 'road_team_id', 'road_team_nm'])
    return df
