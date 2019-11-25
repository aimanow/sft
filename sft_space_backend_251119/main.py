from app.factory import app_factory
from config import ConfigType


def main():
    app_factory(ConfigType.DevelopmentConfig).run(debug=True)


if __name__ == "__main__":
    main()
