import re

re_pref = r'([!./]|)'
re_pref_ = r'[!./]'
re_pref_minus = r'([!./]|-|)'
refp = r'[!./]'
re_link_sup = r'(https://t\.me/|tg://openmessage\?user_id=|@)(\d{6,14}|[\w\d]{5,32})'


deep_links = {
    'tag': '@',
    'link': 'https://t.me/',
    'mention': 'tg://openmessage?user_id=',
    'mention_click': 'tg://user?id='
}

