import os
from peewee import *
from flaskr.connectdatabase import ConnectDatabase
from flaskr.models import Entries
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, current_app

app = Flask(__name__)
app.config.from_object(__name__)
