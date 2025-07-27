#===========================================================
# Database Related Functions
#===========================================================

from libsql_client import create_client_sync, LibsqlError
from contextlib import contextmanager
from dotenv import load_dotenv
from os import getenv
from app.helpers.logging import log_db_request, log_db_result


# Load Turso environment variables from the .env file
load_dotenv()
TURSO_URL = getenv("TURSO_URL")
TURSO_KEY = getenv("TURSO_KEY")


#-----------------------------------------------------------
# Connect to the Turso DB and return the connection
#-----------------------------------------------------------
@contextmanager
def connect_db():
    from flask import current_app as app
    client = None

    try:
        # Create a connection to the Turso DB
        client = create_client_sync(url=TURSO_URL, auth_token=TURSO_KEY)

        # Clear any past queries
        app.dbSQL = None
        app.dbParams = None

        # Wrap the execute method to add logging
        original_execute = client.execute

        def logged_execute(sql, *params, **kwargs):
            # Store for later error handling
            app.dbSQL = sql
            app.dbParams = params[0] if params else None

            # Log and run the query
            log_db_request(app, sql, params)
            result = original_execute(sql, *params, **kwargs)
            log_db_result(app, sql, result)

            return result

        # Update the execute function
        client.execute = logged_execute

        # And return the client connection
        yield client

    finally:
        if client is not None:
            client.close()


