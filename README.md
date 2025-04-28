
# Gemini Q&A Application

Gemini Q&A Application is a simple and interactive web app built with Streamlit that allows users to ask questions and receive AI-generated answers using Google's Gemini Generative AI model. It’s a lightweight demo for experimenting with the capabilities of large language models via a friendly interface.




## 🚀 Features
✍️ Ask any question and get an AI-generated answer in real time

🤖 Powered by Google's Gemini-Pro model

🔒 Secure API key management with .env

🔍 View available Gemini models and their supported generation methods




## 🛠️ Tech Stack

**Python** 3.10

**Streamlit** for the web UI

**google-generativeai** for accessing Gemini models

**python-dotenv** for environment variable management

## 📄 Requirements
If you don’t have a requirements.txt, create one with the following:
## 📦 Installation & Setup


1. 📥 Clone the Repository
Clone the GitHub repository to your local system to get the source code.

```sh
git clone https://github.com/your-username/gemini-qa-app.git
cd gemini-qa-app

```

This command copies the repository files to your machine and changes the current directory to the project folder.

2. 🐍 Create a Virtual Environment

Create an isolated Python environment using conda to manage dependencies easily.
```sh
conda create -p venv python=3.10 -y
```
-p venv creates a virtual environment in a folder named venv.
python=3.10 specifies the Python version.
-y auto-confirms the environment creation.

3. ⚡ Activate the Virtual Environment

Activate the environment you just created.
```sh
conda activate venv/
```
This ensures all the packages are installed and run within the isolated environment.

4. 📦 Install Required Dependencies
Install all the Python libraries specified in requirements.txt.
```sh
pip install -r requirements.txt
```
This step is crucial to ensure the app runs without missing any dependencies.

5. 🔐 Create a .env File
Create a .env file in the root directory of your project and add your Google API Key.
```sh
GOOGLE_API_KEY=your-api-key

```
This file is used to securely store sensitive credentials.
🔑 You need a valid API key from [Google AI Studio](https://makersuite.google.com/) .

6. 🚀 Run the Streamlit App
Start the application using Streamlit.

```sh
streamlit run app.py
```
7. 🌐 Open the App in Your Browser
Open the following URL in your browser:
```sh
http://localhost:8501
```
This is the default address where Streamlit apps run locally.


## 📷 Screenshot

![App Screenshot](https://github.com/kjoseshalu/gemini-question-answering/blob/main/Screenshot1.png)

![App Screenshot](https://github.com/kjoseshalu/gemini-question-answering/blob/main/Screenshot2.png)

