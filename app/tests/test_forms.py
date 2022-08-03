from app.tests.conftest import app_test as flask_app
from ..forms import UnlockAccountForm, CreateAccountForm, CreateMultipleAccountsForm, LookupAccountForm, ReplayTransactionForm

class TestCreateAccountForm:
    def test_create_account_form(client):
        context = flask_app.test_request_context('http://127.0.0.1:5000/create_fresh', method='POST')
        context.push()
        CreateAccountForm.Meta.csrf = False
        form = CreateAccountForm(submit=True)
        assert form.validate_on_submit() == False

class TestCreateMultipleAccountsForm:
    def test_create_multiple_accounts_form(client):
        context = flask_app.test_request_context('http://127.0.0.1:5000/create', method='POST')
        context.push()
        CreateMultipleAccountsForm.Meta.csrf = False
        form = CreateMultipleAccountsForm(create_from_mnemonic='0', number_of_accounts=5, submit=True)
        assert form.validate_on_submit() == False

class TestUnlockAccountForm:
    def test_unlock_account_form(client):
        context = flask_app.test_request_context('http://127.0.0.1:5000/account', method='POST')
        context.push()
        UnlockAccountForm.Meta.csrf = False
        form = UnlockAccountForm(account_key='0', submit=True)
        assert form.validate_on_submit() == False

class TestLookupAccountForm:
    def test_lookup_account_form(client):
        context = flask_app.test_request_context('http://127.0.0.1:5000/lookup', method='POST')
        context.push()
        LookupAccountForm.Meta.csrf = False
        form = LookupAccountForm(account_id='0', account_key='meep', submit=True)
        assert form.validate_on_submit() == False

class TestReplayTransactionForm:
    def test_lookup_account_form(client):
        context = flask_app.test_request_context('http://127.0.0.1:5000/replay', method='POST')
        context.push()
        ReplayTransactionForm.Meta.csrf = False
        form = ReplayTransactionForm(tx_hash='0', submit=True)
        assert form.validate_on_submit() == False