import flask


def render():

    return flask.render_template(
        template_name_or_list = "home.html"
    )