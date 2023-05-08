from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    db_host: SecretStr
    db_port: SecretStr
    db_name: SecretStr
    db_user: SecretStr
    db_password: SecretStr

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()
