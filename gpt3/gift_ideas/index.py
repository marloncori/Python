from openai_api import OpenAI_API
import openai
import flask
from flask import render_template
import nltk
from nltk.corpus import stopwords
from flask_session import Session
import secrets

# Set the OpenAI API key
secret = OpenAI_API()
openai.api_key = secret.key

# Initialize the Flask app
app = flask.Flask(__name__)
# Generate an authorization code for the app
app.secret_key = secrets.token_hex(32)
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

@app.route("/")
def home():
    # Render the home page template
    return render_template("home.html")

def detect_language(text):
    # Split the text into words
    words = nltk.word_tokenize(text)

    # Get the stopwords for each language
    stopwords_en = set(stopwords.words("english"))
    stopwords_es = set(stopwords.words("spanish"))
    stopwords_fr = set(stopwords.words("french"))

    # Count the number of stopwords in the text for each language
    stopwords_en_count = len([w for w in words if w.lower() in stopwords_en])
    stopwords_es_count = len([w for w in words if w.lower() in stopwords_es])
    stopwords_fr_count = len([w for w in words if w.lower() in stopwords_fr])

    # Determine the language with the most stopwords
    if stopwords_en_count > stopwords_es_count and stopwords_en_count > stopwords_fr_count:
        return "english"
    elif stopwords_es_count > stopwords_en_count and stopwords_es_count > stopwords_fr_count:
        return "spanish"
    elif stopwords_fr_count > stopwords_en_count and stopwords_fr_count > stopwords_es_count:
        return "french"
    else:
        return "unknown"

@app.route("/generate_gift_ideas", methods=["POST"])
def generate_gift_ideas():
    # Get the input data from the request
    input_data = flask.request.json
    # Detect the language of the input data
    language = detect_language(input_data["name"])

    # Use the OpenAI API to generate 10 gift ideas
    prompt = f"Gift ideas for a {input_data['age']} year old {input_data['gender']} who is {input_data['marital_status']} and {input_data['has_children']} children, works as a {input_data['profession']}, and is interested in {input_data['area_of_interest']}:"
    model_engine = "text-davinci-003"
    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)
    gift_ideas = completions.choices[0].text.split("\n")
    flask.session['gift_ideas'] = gift_ideas
    # Return the gift ideas to the web app
    # return flask.jsonify(gift_ideas)
    return flask.redirect('/results')

@app.route("/results", methods=["GET"])
def show_results():
    # Get the generated suggestions from the session
    gift_ideas = flask.session.get('gift_ideas')

    # Render the results template with the generated 10 gift ideas
    return render_template("results.html", gift_ideas=gift_ideas)

@app.route("/download", methods=["POST"])
def download():
    # Get the generated ideas from the form
    gift_ideas = flask.request.form.getlist("gift_ideas")
    # Create a text file with the story and allow the user to download it
    response = flask.make_response(gift_ideas)
    response.headers["Content-Disposition"] = "attachment; filename=ten_gift_ideas.txt"
    return response
    #return flask.redirect("/home")

if __name__ == "__main__":
    app.run()