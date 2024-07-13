from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    dates = defaultdict(lambda: {'total_tweets': 0, 'users': defaultdict(int)})
    
    with open(file_path, 'r') as file:
        for line in file:
            json_object = json.loads(line)
            date = datetime.fromisoformat(json_object['date']).date()
            user = json_object['user']['username']
            
            dates[date]['total_tweets'] += 1
            dates[date]['users'][user] += 1
    
    top_10_dates = sorted(dates.items(), key=lambda x: x[1]['total_tweets'], reverse=True)[:10]
    
    top_users_for_dates = [
        (date, max(data['users'].items(), key=lambda x: x[1])[0])
        for date, data in top_10_dates
    ]
    
    return top_users_for_dates
