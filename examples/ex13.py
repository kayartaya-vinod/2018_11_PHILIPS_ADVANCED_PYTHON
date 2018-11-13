'''
Module ex13

A Flask REST endpoint application
'''

from ex12 import Contact, ContactsDao
from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/')
def info():
    return 'This is a Flask REST endpoint'

custom_headers = {}
custom_headers['Content-Type'] = 'application/json'
custom_headers['Accept'] = 'application/json'

@app.route('/api/contacts', methods=['GET'])
def all_contacts():
    dao = ContactsDao()
    output = json.dumps(dao.getAllContacts(), default=lambda c: c.__dict__)
    return Response(output, status='210', headers=custom_headers)

@app.route('/api/contacts/<contact_id>', methods=['GET'])
def one_contact(contact_id):
    dao = ContactsDao()
    contact_id = int(contact_id)
    c1 = dao.getContact(contact_id)
    output = json.dumps(None) if c1==None else c1.as_json
    return Response(output, headers=custom_headers)

@app.route('/api/contacts/<contact_id>', methods=['DELETE'])
def del_contact(contact_id):
    dao = ContactsDao()
    contact_id = int(contact_id)
    dao.deleteContact(contact_id)

    # Ideally DELETE request should return the deleted state from
    # the resource; In this case, we are returning the remaining state
    return all_contacts()

@app.route('/api/contacts', methods=['POST'])
def add_contact():
    c1 = Contact()
    c1.as_json = request.data
    dao = ContactsDao()
    c1 = dao.addContact(c1)
    return c1.as_json

@app.route('/api/contacts/<contact_id>', methods=['PUT'])
def update_contact(contact_id):
    c1 = Contact()
    c1.as_json = request.data
    c1.id = contact_id
    dao = ContactsDao()
    c1 = dao.updateContact(c1)
    return Response(c1.as_json, headers=custom_headers)