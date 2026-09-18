from flask import Blueprint, render_template

from models.portfolio_model import PortfolioModel


main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    return render_template("index.html", slides=PortfolioModel.get_hero_slides(), services=PortfolioModel.get_services(), gallery=PortfolioModel.get_gallery_items())


@main_bp.route("/services")
def services():
    return render_template("index.html", services=PortfolioModel.get_services(), slides=[], gallery=[])


@main_bp.route("/gallery")
def gallery():
    return render_template("index.html", gallery=PortfolioModel.get_gallery_items(), slides=[], services=[])


@main_bp.route("/catalogue")
def catalogue():
    return render_template("index.html", slides=[], services=[], gallery=[])