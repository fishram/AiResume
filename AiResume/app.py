from flask import Flask, render_template, request, redirect, url_for
import openai

openai.api_key = "your_api_key_here"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        job_experience = request.form["job-experience"]
        skills = request.form["skills"]
        career_goals = request.form["career-goals"]

        resume_text = generate_resume(name, email, job_experience, skills, career_goals)

        return render_template("index.html", resume_text=resume_text)

    return render_template("index.html")


def generate_resume(name, email, job_experience, skills, career_goals):
    prompt = f"Generate a resume for {name} with email {email}. Job experience: {job_experience}. Skills: {skills}. Career goals: {career_goals}."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(debug=True)
