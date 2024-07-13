from flask import Flask, render_template
from utils import SCORES_FILE_NAME, BAD_RETURN_CODE
import os

app = Flask(__name__, template_folder='html_templates')


@app.route("/")
def home():
    if not os.path.exists(SCORES_FILE_NAME) or os.stat(SCORES_FILE_NAME).st_size == 0:
        return render_template('error.html', ERROR=BAD_RETURN_CODE)
    else:
        with open(SCORES_FILE_NAME, "r") as file:
            current_score = file.read().strip()
            if not current_score.isdigit():
                return render_template('error.html', ERROR=BAD_RETURN_CODE)
            else:
                return render_template('score.html', SCORE=current_score)


if __name__ == '__main__':
    app.run(port=5001)





