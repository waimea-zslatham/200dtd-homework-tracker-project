#===========================================================
# YOUR PROJECT TITLE HERE
# YOUR NAME HERE
#-----------------------------------------------------------
# BRIEF DESCRIPTION OF YOUR PROJECT HERE
#===========================================================

from flask import Flask, render_template, request, flash, redirect
import html

from app.helpers.session import init_session
from app.helpers.db      import connect_db
from app.helpers.errors  import init_error, not_found_error
from app.helpers.logging import init_logging
from app.helpers.time    import init_datetime, utc_timestamp, utc_timestamp_now


# Create the app
app = Flask(__name__)

# Configure app
init_session(app)   # Setup a session for messages, etc.
init_logging(app)   # Log requests
init_error(app)     # Handle errors and exceptions
init_datetime(app)  # Handle UTC dates in timestamps



#-----------------------------------------------------------
# Home page route
#-----------------------------------------------------------
@app.get("/")
def index():
    with connect_db() as client:
        # Get all the subject from the DB
        sql = "SELECT id, name, teacher, priority FROM subjects ORDER BY priority ASC"
        params = []
        result = client.execute(sql, params)
        subjects = result.rows

        # And show them on the page
        return render_template("pages/home.jinja", subjects=subjects)


#-----------------------------------------------------------
# Subject page route - Show details of a single subject
#-----------------------------------------------------------
@app.get("/subject/<int:id>")
def show_subject(id):
    with connect_db() as client:
        # Get the subject details from the DB
        sql = "SELECT id, name, teacher, priority FROM subjects WHERE id=?"
        params = [id]
        result = client.execute(sql, params)

        # Did we get a result?
        if result.rows:
            # yes, so show it on the page
            subject = result.rows[0]

            # Get all the assessments from the DB
            sql = """
                SELECT id, name, due_date, priority, completed
                FROM assessments 
                WHERE subject_id = ?
                ORDER BY priority ASC
            """
            params = [id]
            result = client.execute(sql, params)
            assessments = result.rows


            return render_template("pages/subject.jinja", subject=subject, assessments=assessments)

        else:
            # No, so show error
            return not_found_error()


#-----------------------------------------------------------
# Route for checking a thing, using data posted from a form
#-----------------------------------------------------------
@app.post("/subject/<int:sid>/assessment/<int:aid>/done")
def mark_assessment_done(sid, aid):
    with connect_db() as client:
        # Add the thing to the DB
        sql = "UPDATE assessments SET completed=1 WHERE id=?"
        params = [aid]
        client.execute(sql, params)

        # Go back to the home page
        # flash(f"Assessment Completed", "success")
        return redirect(f"/subject/{sid}")

#-----------------------------------------------------------
# Route for unchecking a thing, using data posted from a form
#-----------------------------------------------------------
@app.post("/subject/<int:sid>/assessment/<int:aid>/not.done")
def mark_assessment_notdone(sid, aid):
    with connect_db() as client:
        # Add the thing to the DB
        sql = "UPDATE assessments SET completed=0 WHERE id=?"
        params = [aid]
        client.execute(sql, params)

        # Go back to the home page
        # flash(f"Assessment Not completed", "success")
        return redirect(f"/subject/{sid}")


#-----------------------------------------------------------
# Route for adding a thing, using data posted from a form
#-----------------------------------------------------------
@app.post("/add/subject")
def add_a_thing():
    # Get the data from the form
    subject  = request.form.get("subject")
    priority = request.form.get("priority")
    teacher = request.form.get("teacher")


    with connect_db() as client:
        # Add the thing to the DB
        sql = "INSERT INTO subjects (name, teacher, priority) VALUES (?, ?, ?)"
        params = [subject, teacher, priority]
        client.execute(sql, params)

        # Go back to the home page
        #flash(f"Thing '{subject}' added", "success")
        return redirect(f"/")
    

#-----------------------------------------------------------
# Route for adding an assessment to a specific subject
#-----------------------------------------------------------
@app.post("/subject/<int:sid>/add/assessment")
def add_assessment(sid):
    # Get data from the form
    name = request.form.get("assessment")
    priority = request.form.get("priority")
    due_date = request.form.get("date")

    with connect_db() as client:
        sql = """
            INSERT INTO assessments (name, due_date, priority, completed, subject_id)
            VALUES (?, ?, ?, 0, ?)
        """
        params = [name, due_date, priority, sid]
        client.execute(sql, params)

        return redirect(f"/subject/{sid}")


#-----------------------------------------------------------
# Route for deleting a thing, Id given in the route
#-----------------------------------------------------------
@app.get("/delete/<int:id>")
def delete_a_thing(id):
    with connect_db() as client:
        # Delete the thing from the DB
        sql = "DELETE FROM subjects WHERE id=?"
        params = [id]
        client.execute(sql, params)

        # Go back to the home page
        #flash("subject deleted", "success")
        return redirect(f"/")


#-----------------------------------------------------------
# Route for deleting an assessment
#-----------------------------------------------------------
@app.get("/subject/<int:sid>/delete/assessment/<int:aid>")
def delete_assessment(sid, aid):
    with connect_db() as client:
        # Delete the assessment from the DB
        sql = "DELETE FROM assessments WHERE id=?"
        params = [aid]
        client.execute(sql, params)

        # Go back to the subject page
        return redirect(f"/subject/{sid}")

