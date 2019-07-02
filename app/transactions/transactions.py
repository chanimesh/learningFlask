from flask import Blueprint

transactions = Blueprint('transactions', 'transactions', url_prefix='/transactions')


@transactions.route('/')
def transactions_test():
    return 'testing transactions'


@transactions.route('/list')
def transactions_list():
    return 'show transactions'
