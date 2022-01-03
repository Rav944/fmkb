#Installation of the environment and packages:
    python3 -m venv env
    source venv/bin/activate
    pip install requirements
    ./manage.py makemigrations
    ./manage.py migrate

#database configuration:
Sample configuration file:

    [client]
    database = <database_name>
    user = <database_user_name>
    password = <password>
    default-character-set = utf8

File location:

    /etc/mysql/my.cnf

#Local variable:
Should be in the following file:

    /fmkb/fmkb/.env

Should contain:


    SECRET_KEY=<django_secret_key>
    DEFAULT_FILE_STORAGE=storages.backends.s3boto3.S3Boto3Storage

    AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
    AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
    AWS_STORAGE_BUCKET_NAME=<AWS_STORAGE_BUCKET_NAME>
    AWS_QUERYSTRING_AUTH=<AWS_QUERYSTRING_AUTH>
