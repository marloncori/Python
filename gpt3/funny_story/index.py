from flask import Flask, request, render_template, redirect, make_response, session #send_file
from openai_api import OpenAI_API
import openai
import secrets

# Set the OpenAI API key
secret = OpenAI_API()
openai.api_key = secret.key

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

@app.route("/")
def home():
    # Render the home page template
    return render_template("home.html")

def generate_story(name, age, nationality, living_country, hobbies, strange_word, strange_object, strange_habit):
    # Use the OpenAI API to generate a funny story based on the input data
    prompt = f"Write a funny story about {name} who is a {age}-year-old {nationality} living in {living_country}. He enjoys {hobbies}, but his strangest habit is {strange_habit}. Include this idea in the story: One day {name} found, a {strange_object} that could talk, and called itself {strange_word}, From that day on, his life was never the same."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=2024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response["choices"][0]["text"]

@app.route("/generate", methods=["POST"])
def generate():
    # Get the input data from the form
    name = request.form.get("name")
    age = request.form.get("age")
    nationality = request.form.get("nationality")
    living_country = request.form.get("living_country")
    hobbies = request.form.get("hobbies")
    strange_word = request.form.get("strange_word")
    strange_object = request.form.get("strange_object")
    strange_habit = request.form.get("strange_habit")
    story_language = request.form.get("story_language")

    # Generate the story using the OpenAI API
    story = generate_story(name, age, nationality, living_country, hobbies, strange_word, strange_object, strange_habit)
    
    session['story'] = story
    session['story_language'] = story_language
    return redirect('/result')

@app.route("/result", methods=["GET"])
def show_results():
    # Get the generated story from the session
    story = session.get('story')
    story_language = session.get('story_language')

    # Render the results template with the generated story
    return render_template("results.html", story=story, story_language=story_language)


@app.route("/download", methods=["POST"])
def download():
    # Get the generated story from the form
    story = request.form.get("story")

    # Create a text file with the story and allow the user to download it
    response = make_response(story)
    response.headers["Content-Disposition"] = "attachment; filename=funny_story.txt"
    return response

if __name__ == "__main__":
    app.run()