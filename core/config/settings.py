import os
from pydantic import BaseModel

# load .env file
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseModel):
    ENV: str
    ADLS_CONNECTION_STRING: str
    BRONZE_CONTAINER: str = "bronze"


def get_settings():

    env = os.getenv("ENV")

    if env == "dev":
        adls_conn = os.getenv("ADLS_CONNECTION_STRING")

        if not adls_conn:
            raise ValueError(
                "ADLS_CONNECTION_STRING is missing from environment"
        )

        if "AccountName=" not in adls_conn:
            raise ValueError(
            "ADLS_CONNECTION_STRING appears malformed"
        )
        return Settings(
        ENV=env,
        ADLS_CONNECTION_STRING=adls_conn,
        BRONZE_CONTAINER=os.getenv("BRONZE_CONTAINER", "bronze")
    )

    elif env == "stage":
        return Settings(
            ENV="stage",
            ADLS_CONNECTION_STRING="stage_conn",
        )

    return Settings(
        ENV="prod",
        ADLS_CONNECTION_STRING="prod_conn",
    )