import json
import re
from collections import Counter
from typing import List, Tuple

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    user_tag_pattern = r'@[\w]{1,15}'
    tag_counts = Counter()
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                item = json.loads(line)
                content = item.get('content', '')
                tags_found = re.findall(user_tag_pattern, content)
                tag_counts.update(tags_found)
            except json.JSONDecodeError:
                continue
    
    top_tags = tag_counts.most_common(10)
    return top_tags