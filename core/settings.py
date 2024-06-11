from pydantic import SecretStr, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    user_id: int
    api_id: SecretStr
    api_hash: SecretStr
    phone_number: SecretStr
    db_url: SecretStr
    # redis: RedisDsn
    
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')



settings = Settings(_env_file='secret_data.env', _env_file_encoding='utf-8')
