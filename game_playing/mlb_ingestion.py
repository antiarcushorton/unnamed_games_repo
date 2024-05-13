import http.client
import json
import pandas as pd

data_list = []

conn = http.client.HTTPSConnection("statsapi.mlb.com")
payload = ''
headers = {}
conn.request("GET", "/api/v1/schedule/games/?sportId=1&startDate=2024-05-12&endDate=2024-05-13", payload, headers)
res = conn.getresponse()
data = res.read()
game_dates = json.loads(data)['dates']

for date in game_dates:
    games = date['games']
    for game in games:
        if 'score' in game:
            data_list.append([game['gamePk'], game['officialDate'], game['status']['abstractGameState'], game['gameType'],
                          game['teams']['home']['score'], game['teams']['away']['score'],
                          game['teams']['home']['team']['id'], game['teams']['away']['team']['id']])
        else:
            data_list.append(
                [game['gamePk'], game['officialDate'], game['status']['abstractGameState'], game['gameType'],
                 None, None,
                 game['teams']['home']['team']['id'], game['teams']['away']['team']['id']])

df = pd.DataFrame(data_list, columns=['game_id', 'game_date', 'game_postseason_flg', 'game_status', 'game_home_tm_score', 'game_road_tm_score', 'home_tm_id', 'road_team_id'])
print(df)