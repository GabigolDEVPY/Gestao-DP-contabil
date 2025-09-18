from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.func_accounts import Accounts

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route("/accounts", methods=["GET"])
def return_page():
    accounts, accounts_privadas = Accounts.return_accounts()
    return render_template("accounts.html", contas=accounts, contas_privadas=accounts_privadas)


@accounts_bp.route("/accounts/create", methods=["POST"])
def create_account():
    result = Accounts.create_accounts(dados=request.form.to_dict())
    if result:
        flash(result)
    return redirect(url_for("accounts.return_page"))

@accounts_bp.route("/accounts/delete", methods=["POST"])
def delete_account():
    result = Accounts.delete_account(dados=request.form.to_dict())
    if result:
        flash(result)
    return redirect(url_for("accounts.return_page"))


@accounts_bp.route("/accounts/edit", methods=["POST"])
def edit_account():
    result = Accounts.edit_account(dados=request.form.to_dict())
    if result:
        flash(result)
        return redirect(url_for("accounts.return_page"))
    return redirect(url_for("accounts.return_page"))
