## Repository

Branch `back` - backend of application\
Branch `front` - frontend of application

## Running
### Clone the branch
```commandline
git clone -b api_v2 --single-branch git@gitlab.com:Danis_UA/sft.git
```

### Install requirements
```
pip install -r requirements.txt
```

### Create a PostgreSQL database
```commandline
sudo -i -u postgres
createdb database_name
createuser username --interactive
y
psql
```

```sql
ALTER USER username WITH PASSWORD 'password';
\q
```

### Create development config
Create your local development config: `config/development/config.py`:

```python
from config import ConfigBase


class LocalConfig(ConfigBase):
    SECRET_KEY = "DEVELOPMENT_SECRET_KEY"
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database_name'

    # For development you can use the service: https://mailtrap.io
    MAIL_DEFAULT_SENDER = 'noreply@sft.space'
    MAIL_SERVER, MAIL_PORT = "smtp.mailtrap.io", 2525
    MAIL_USERNAME = '<your_mailtrap_username>'
    MAIL_PASSWORD = '<your_mailtrap_password>'
    MAIL_FEEDBACK = 'info@sft.space'

    # If you are using a frontend application
    FRONTEND_URL = 'http://localhost:8000/'
    FRONTEND_EMAIL_CONFIRM_URL = '/email_confirmation'
    FRONTEND_PASSWORD_RESET_URL = '/password_reset'
```

### Upgrade the database scheme
```commandline
flask db upgrade
```

### Run the application
```commandline
flask run
```

### Read API docs
Working on Flask dev server
[http://localhost:5000/api/public/docs](http://localhost:5000/api/public/docs)
