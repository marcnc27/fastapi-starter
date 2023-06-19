import uvicorn
from uvicorn.config import LOGGING_CONFIG

from config.configuration import Configuration

from constants import app_title


def main():
    configuration = Configuration.get()
    LOGGING_CONFIG["formatters"]["default"]["fmt"] = f"%(asctime)s - [{app_title}] - %(levelprefix)s %(message)s"
    LOGGING_CONFIG["formatters"]["access"][
        "fmt"] = f"%(asctime)s - [{app_title}] - %(levelprefix)s %(client_addr)s %(status_code)s"
    LOGGING_CONFIG["loggers"]["uvicorn"]["propagate"] = False
    LOGGING_CONFIG["loggers"]["uvicorn"]["level"] = "DEBUG"
    workers = 1 if configuration.DEBUG else 2
    uvicorn.run("core.app:app", host="0.0.0.0", workers=workers, log_config=LOGGING_CONFIG, port=configuration.PORT)


if __name__ == '__main__':
    main()
