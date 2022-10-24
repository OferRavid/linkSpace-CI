from flask import Flask,redirect,url_for
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import json
from flask import render_template
from bson import ObjectId
# import logging
import os

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    title = "link sample application with Flask and MongoDB" 
    heading = "linkspace"  
    app_env = os.environ.get("APP_ENV")
    secret_key = os.environ.get("SECRETKEY")
    mongodb = {}
    mongodb["username"] = os.environ.get("MONGODB_USERNAME")
    mongodb["password"] = os.environ.get("MONGODB_PASSWORD")
    mongodb["hostname"] = os.environ.get("MONGODB_HOSTNAME")
    mongodb["urlsuffix"] = os.environ.get("MONGODB_URL_SUFFIX")
    mongodb["dbname"] = os.environ.get("contactdb")
    mongo_uri = "mongodb://"+mongodb["username"]+":"+mongodb["password"]+"@"+mongodb["hostname"]+":27017/contactdb?"+mongodb["urlsuffix"]

    app.config.from_mapping(
        SECRET_KEY=secret_key,
        MONGO_DBNAME = mongodb["dbname"],
        MONGO_URI = mongo_uri
    )

    """Try connecting to mongoDB"""
    try:
        mongodb_client = PyMongo(app)
        db = mongodb_client.db
        app.logger.info("Succesfully connected to MongoDB!")
    except Exception as e:
        print("appppp")
        # logger.error("Could not connect to Mongo.\nException seen: " + str(e))


    if not app_env == "test":
        contact_db = db.contacts
    else:
        contact_db = db.test_contacts


    @app.route("/")
    @app.route("/list" , methods=['GET'])
    def lists ():

        app.logger.info('get all link')
        # Display all of the links
        all_links = contact_db.find()
        return render_template('home.html',links=all_links,t=title,h=heading)
        # return render_template('index.html',links=all_links,t=title,h=heading)

    @app.route("/action", methods=['POST'])
    def action ():
        #Adding a link
        print(request.values.get)
        link=request.values.get("link")
        desc=request.values.get("desc")
        date=request.values.get("date")
        Subject=request.values.get("Subject")
        contact_db.insert_one({ "link":link, "desc":desc, "date":date, "Subject":Subject, "done":"no"})
        app.logger.info('Adding a link' )
        
        return redirect("/list")

    @app.route("/remove" )
    def remove ():
        #Deleting a link 
        app.logger.info('del a link',request.values.get )
        print(request.values.get)
        key=request.values.get("_id")
        contact_db.delete_one({"_id":ObjectId(key)})
        app.logger.info('Deleting a link' + key)
        return redirect("/")

    @app.route("/update")
    def update ():
        print(request.values.get)
        id=request.values.get("_id")
        link=contact_db.find({"_id":ObjectId(id)})
        app.logger.info('update a link' + id)
        return render_template('update.html',links=link,h=heading,t=title)

    @app.route("/action3", methods=['POST'])
    def action3 ():
        #Updating a link
        print(request.values.get)
        link=request.values.get("link")
        desc=request.values.get("desc")
        date=request.values.get("date")
        Subject=request.values.get("Subject")
        id=request.values.get("_id")
        contact_db.update_one({"_id":ObjectId(id)}, {'$set':{ "link":link, "desc":desc, "date":date, "Subject":Subject }})
        return redirect("/")

    @app.route("/search", methods=['GET'])
    def search():
        print(request.values.get)
        app.logger.warning('Searching a link')
        #Searching a link
        key=request.values.get("key")
        if(key=="_id"):
            all_links = contact_db.find({"Subject":ObjectId(key)})
        else:
            all_links = contact_db.find({"Subject":key})
        return render_template('searchlist.html',links=all_links,t=title,h=heading)

    return app
