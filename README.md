# Glory
Glory is web app to manage and store your achievements. It offers a convinient way for students to see their growth in real time.
Eventually down the line a feature to auto-generate a resume will be added.

## Screenshots
<div style="display: grid">
    <img src=./screenshots/login.jpeg>
    <img src=./screenshots/profile.jpeg>
    <img src=./screenshots/home.jpeg>
</div>

## Running the backend
The backend is all dockerised making it quite easy to run.

On first time startup:
```docker-compose up -d --build```

On subsequent startups simply run:
```docker-compose up```

## Developing the backend
Since the entire backend exists in docker container, it can be a bit annoying to develop it.
Thus we recommend creating a seperate venv with the correct python version as well as the pip packages.
The backend currently only works with python version 3.8 and 3.9. We recommend managing python versions on unix systems with [pyenv](https://github.com/pyenv/pyenv). 

Create a new virtual env with `pyenv` with python version 3.8 and activate it:
```pyenv install 3.8.17
pyenv virtualenv 3.8.17 glory-env
pyenv activate glory-env
```

Install the necessary dependencies:
```python -m pip install -r backend/requirements.txt```

## Running the front end
Ensure the backend is running locally then running the frontend is as simple as opening `index.html` with any browser.

## Created for a college project by:
- [Shresth Prasad](https://github.com/Yttrium-32)
- [Rishabh kumar](https://github.com/rishabhkumar2004)

## Changes made by Harshil here
- foo
- bar
