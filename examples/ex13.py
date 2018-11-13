'''
Module ex13

A Flask REST endpoint application
'''

from ex12 import Contact, ContactsDao
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def info():
    return 'This is a Flask REST endpoint'

@app.route('/api/contacts')
def all_contacts():
    dao = ContactsDao()
    return json.dumps(dao.getAllContacts(), 
        default=lambda c: c.__dict__)