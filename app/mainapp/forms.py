from flask_wtf import FlaskForm


class ActionForm(FlaskForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
