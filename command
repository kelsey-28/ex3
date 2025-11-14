C:\Users\HP>cd C:\Users\HP\OneDrive\Documents\ex3

C:\Users\HP\OneDrive\Documents\ex3>docker build -t flask-docker-app:local .
'docker' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\HP\OneDrive\Documents\ex3>docker run --rm -p 5000:5000 flask-docker-app:local
'docker' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\HP\OneDrive\Documents\ex3>docker login
'docker' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\HP\OneDrive\Documents\ex3>docker tag flask-docker-app:local <your-username>/flask-docker-app:latest
The system cannot find the file specified.

C:\Users\HP\OneDrive\Documents\ex3>docker push <your-username>/flask-docker-app:latest
The system cannot find the file specified.

C:\Users\HP\OneDrive\Documents\ex3>#Replace <your-username> with your Docker Hub username. Choose a repo name (e.g., flask-docker-app) and tag (e.g., latest).
The system cannot find the file specified.
