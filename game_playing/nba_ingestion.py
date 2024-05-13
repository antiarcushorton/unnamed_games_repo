import http.client
import json
import pandas as pd

data_list = []
token = '928fdade-5485-4d44-9810-1fda52e05737'

conn = http.client.HTTPSConnection("api.balldontlie.io")
payload = ''
headers = {
  'Authorization': f'{token}'
}
conn.request("GET", "/v1/games?start_date=2024-05-06&end_date=2024-05-07", payload, headers)
res = conn.getresponse()
data = res.read()
games = json.loads(data)['data']

for game in games:
    data_list.append([game['id'], game['date'], game['status'], game['postseason'], game['home_team_score'], game['visitor_team_score'], game['home_team']['id'], game['visitor_team']['id']])

df = pd.DataFrame(data_list, columns=['game_id', 'game_date', 'game_postseason_flg', 'game_status', 'game_home_tm_score', 'game_road_tm_score', 'home_tm_id', 'road_team_id'])
print(df)
