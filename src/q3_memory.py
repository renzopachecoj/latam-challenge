import json
import re
from collections import defaultdict
from typing import List, Tuple

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    user_tag_pattern = r'@[\w]{1,15}'
    tag_counts = defaultdict(int)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                item = json.loads(line)
                content = item.get('content', '')
                tags_found = re.findall(user_tag_pattern, content)
                
                for tag in tags_found:
                    tag_counts[tag] += 1
            except json.JSONDecodeError:
                continue
    
    top_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_tags