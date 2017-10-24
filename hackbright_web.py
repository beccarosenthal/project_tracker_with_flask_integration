"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template, session, flash, redirect

#imports hackbright.py so we have all the files
import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    # return "{acct} is the GitHub account for {first} {last}".format(
    #     acct=github, first=first, last=last)

    html = render_template("student_info.html", first=first, 
                                                last=last, 
                                                github=github)

    return html

#title in Kabob case
@app.route("/student-search")
def get_student_form():
    """Show form to search for student"""

    return render_template("student_search.html")



@app.route("/student-add")
def student_add():
    """renders form for create new student"""

    return render_template("create_new_student.html")


@app.route("/create-new-student", methods=['POST'])
def create_new_student():
    #.for instead of .args because post request
    first_name = request.form.get("fname")
    last_name = request.form.get("lname")
    github = request.form.get("ghub")


    hackbright.make_new_student(first_name, last_name, github)
   
    
    return render_template("confirm_student_addition.html", first=first_name, 
                                                last=last_name,
                                                github=github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
