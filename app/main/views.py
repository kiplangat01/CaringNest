from flask import abort, flash, redirect, render_template, request, url_for

from . import main


@main.route('/')
def index():


    return render_template('/main/index.html')


