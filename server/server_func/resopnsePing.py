import json
from typing import Union

def pingPongJson(jsonIn):
    try: 
        if isinstance(jsonIn, dict):
            return jsonIn
        elif isinstance(jsonIn, str):
            json_dict = json.loads(jsonIn)
            response_json = json.dumps(json_dict)
            return response_json
    except Exception as e:
        return f"pingPongJson fail {e}"
    