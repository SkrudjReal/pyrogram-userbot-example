from pydantic import BaseModel

import textwrap as tw

class UserConfig(BaseModel):
    prefix: str


tricks = {
    'user': {
        'prefix': 'а'
    }
}


ucfg = UserConfig.parse_obj(tricks['user'])

