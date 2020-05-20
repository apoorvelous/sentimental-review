# sentimental-review
A Flask App that does sentimental analysis

## To deploy

1. Create a virtual environment with `Python3.8` -
`python3.8 -m venv venv`

2. Source the virtual environment -
`source venv/bin/activate`

3. Install the dependencies -
`pip install -r requirements.txt`

4. Run the following command -
`python download_nltk.py`

5. Export the environment variables -
`export FLASK_APP=app.py`
`export FLASK_DEBUG=False`

6. Start the server -
`flask run --port=5000`
