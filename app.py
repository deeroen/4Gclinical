from flask import Flask
from flask import request
from script.solver import *
from doctest import testmod

app = Flask(__name__)

@app.route("/")
def index():
    phone_number = request.args.get("phone_number", "").replace('"', "")
    word_list = request.args.get("word_list", "")
    if phone_number and word_list:
        output = str(solver(phone_number, sanatise_array(word_list), keypad))
    else:
        output = "[]"
    return (
        """<form action="" method="get">
                Phone number "3662277": <input type="text" name="phone_number">
                <br>
                <br>
                Array of words eg. ["foo", "bar", "baz"]: <input type="text" name="word_list">
                <input type="submit" value="Submit">
            </form>"""
        + "Output: "
        + output
    )


if __name__ == "__main__":
    # This line is meant for doctest, set verbose to true to see the result of the test
    testmod(verbose=False)
    app.run(host="127.0.0.1", port=8080, debug=True)