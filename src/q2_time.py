from typing import List, Tuple
from collections import Counter
import json
import re

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    emoji_regex = r'[\U0001F300-\U0001F5FF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\u2600-\u26FF\u2700-\u27BF]'


    with open(file_path, 'r') as f:
        emoji_counts = Counter()
        for line in f:

            tweet = json.loads(line)
            emojis = re.findall(emoji_regex, tweet['content']) 
            emoji_counts.update(emojis)


    return emoji_counts.most_common(10)