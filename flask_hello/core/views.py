from flask import render_template, current_app as app

from ..core import core


@core.route('/', methods=['GET', ])
def index():
    app.logger.warning('Logging this!')
    return render_template('index.html')
