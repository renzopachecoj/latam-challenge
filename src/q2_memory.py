from typing import List, Tuple
import json
import emoji
from collections import defaultdict
from datetime import datetime
import emoji.unicode_codes


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emojis = {}
    with open(file_path, 'r') as file:
        for line in file:
            json_object = json.loads(line)
            content = json_object.get('content', "")
            for char in content:
                if (0x1F300 <= ord(char) <= 0x1F5FF) or \
                (0x1F600 <= ord(char) <= 0x1F64F) or \
                (0x1F680 <= ord(char) <= 0x1F6FF) or \
                (0x2600 <= ord(char) <= 0x26FF) or \
                (0x2700 <= ord(char) <= 0x27BF):
                    if char in emojis:
                        emojis[char] += 1
                    else:
                        emojis[char] = 1

    top_10_emojis = sorted(emojis.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_10_emojis