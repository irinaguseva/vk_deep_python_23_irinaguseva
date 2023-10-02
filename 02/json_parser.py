from __future__ import annotations
import json
from typing import Optional


def parse_json(json_str: str,
               required_fields: Optional[list[str]],
               keywords: Optional[list[str]],
               keyword_callback) -> None:

    if not keyword_callback:
        raise TypeError("keyword_callback не должна быть None")
    try:
        json_doc = json.loads(json_str)
    except json.JSONDecodeError as err:
        raise ValueError("Некорректная json-строка") from err
    for field in required_fields:
        if field in json_doc:
            for keyword in keywords:
                line = json_doc[field].split()
                for word in line:
                    if keyword.lower() == word.lower():
                        keyword_callback(field, word)
