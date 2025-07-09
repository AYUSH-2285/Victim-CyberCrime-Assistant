from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.reports.models import Report

reports_bp = Blueprint("reports", __name__, template_folder="../templates")

@reports_bp.route("/", methods=["GET"])
def report():
    reports = Report.query.all()
    return render_template("index.html", reports=reports)

@reports_bp.route("/submit", methods=["GET", "POST"])
def submit_report():
    if request.method == "POST":
        category = request.form["category"]
        description = request.form["description"]
        new_report = Report(category=category, description=description)
        db.session.add(new_report)
        db.session.commit()
        flash("Report submitted successfully", "success")
        return redirect(url_for("reports.report"))
    return render_template("report_form.html")
