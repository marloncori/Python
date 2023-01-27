from openai_api import OpenAI_API
import openai
import flask

# Initialize the Flask app
app = flask.Flask(__name__)

# Set the OpenAI API key
secret = OpenAI_API()
openai.api_key = secret.key

@app.route("/generate_gift_ideas", methods=["POST"])
def generate_gift_ideas():
    # Get the input data from the request
    #input_data = flask.request.json
    input_data = flask.request.get_json()
    # Use the OpenAI API to generate 10 gift ideas
    prompt = f"Gift ideas for a {input_data['age']} year old {input_data['gender']} who is {input_data['marital_status']} and {input_data['has_children']} children, works as a {input_data['profession']}, and is interested in {input_data['area_of_interest']}:"
    model_engine = "davinci-3"
    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)
    gift_ideas = completions.choices[0].text.split("\n")

    # Return the gift ideas to the web app
    return flask.jsonify(gift_ideas)

@app.route("/save_gift_ideas", methods=["POST"])
def save_gift_ideas():
    # Get the gift ideas from the request
    gift_ideas = flask.request.json

    # Save the gift ideas to a file
    with open("gift_ideas.txt", "w") as f:
        for idea in gift_ideas:
            f.write(idea + "\n")

    # Return the file to the user
    return flask.send_file("gift_ideas.txt", as_attachment=True)

if __name__ == "__main__":
    app.run()