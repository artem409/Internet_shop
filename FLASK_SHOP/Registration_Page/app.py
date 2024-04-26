import flask

registration = flask.Blueprint(
    name = "registration",
    import_name = "app",
    template_folder = "Registration_Page/templates",
    static_folder= "Registration_Page/static",
    static_url_path="/shop/"
)