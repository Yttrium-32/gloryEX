# Glory
Glory is desktop app made with Pyside6 to manage and store your achievements. It offers a convinient way for students to see their growth in real time.
Eventually down the line a feature to auto-generate a resume will be added.

## Screenshots
<div style="display: grid">
    <img src=./screenshots/login.png>
    <img src=./screenshots/cards.png>
</div>

## Backend (API)
### With docker

- Setup docker: https://docs.docker.com/compose/install/

- On first time startup:
    ```docker-compose up -d --build```

- On subsequent startups simply run:
    ```docker-compose up```

### Without docker
- Install all dependencies:
    ```
    python -m venv venv
    source venv/bin/activate
    python -m pip install -r requirements.txt
    ```
-  Setup postgresql on your system:
    https://www.postgresql.org/download/

- Run the api:
    ```
    uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
    ```

## GUI
- Install all dependencies:
    ```
    python -m venv venv
    source venv/bin/activate
    python -m pip install -r requirements.txt
    ```

- Run main.py:
    ```
    python main.py
    ```
