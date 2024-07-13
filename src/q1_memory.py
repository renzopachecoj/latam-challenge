from typing import List, Tuple
from datetime import datetime
import json

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    
    dates = {}
    with open(file_path, 'r') as file:
        for line in file:
            json_object = json.loads(line)
            date = datetime.fromisoformat(json_object['date']).date()
            user = json_object['user']['username']
            if date in dates:
                dates[date]['total_tweets'] += 1
                if json_object['user']['username'] in  dates[date]['users']:
                    dates[date]['users'][user] += 1
                else:
                    dates[date]['users'][user] = 1
            else:
                dates[date] = {}
                dates[date]['total_tweets'] = 1
                dates[date]['users'] = {}
                dates[date]['users'][user] = 1
            
        top_10_dates = sorted(dates.items(), key=lambda x: x[1]['total_tweets'], reverse=True)[:10]

        top_users_for_dates = []

        for date, data in top_10_dates:
            users = data['users']
            if users:
                top_user = max(users.items(), key=lambda x: x[1])
                top_users_for_dates.append((date, top_user[0]))

        return top_users_for_dates

            
            
            