from flask import Flask, render_template, request, redirect, url_for, session, flash
app = Flask(__name__)

app.secret_key = "Ukiddingme,bro?"

session["tarefas"] = []