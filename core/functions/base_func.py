import re

def link_getter(text: str) -> [str, bool]:
    expression = r'((https://t\.me/|@)[\w\d]{5,32}|tg://openmessage\?user_id=\d{6,14})'
    result = re.search(expression, text)
    if result:
        result = result[0].replace('https://t.me/', '').replace('tg://openmessage?user_id=', '').strip('@')
        if result.isdigit():
            return int(result)
        else:
            return str(result)
    else:
        return None