Project Goals
Build a CRUD Todo List using Python.

Store data in a tasks.json file.

(Future) Connect to a Flask backend and HTML/CSS frontend.

Class Architecture
Task: Data model (ID, Title, Done).

Database: Handles raw file I/O (Read/Write JSON).

Repository: Handles CRUD logic (Add, Delete, Find).

UserInteraction: Terminal menu for the user.

The Checklist
[x] Define Task class.

[ ] Build Database JSON reader/writer.

[ ] Build Repository logic.

[ ] Test CRUD in terminal.

Timelines:
Phase 1: The Python "Engine" (Logic & JSON)
Time: 1–2 Weeks

Week 1: Learning how to structure your classes (Task, Repository, Database) and getting them to talk to each other.

Week 2: Handling the json library—learning how to turn your objects into strings and save them to a file without errors.

Goal: You can add, list, and delete tasks using just your terminal.

Phase 2: The "Bridge" (Flask/Web API)
Time: 1 Week

This is the quickest part if your logic is already solid. You are essentially "wrapping" your Python code so a website can talk to it.

Goal: You can visit a URL like localhost:5000/tasks and see your JSON data in the browser.

Phase 3: The "Face" (HTML/CSS & Integration)
Time: 2–3 Weeks

Week 1: Learning basic HTML (structure) and CSS (styling).

Week 2: The "Big Step"—using JavaScript (fetch) to make your HTML buttons actually trigger your Python code.

Goal: A fully functional website where you can type a task, hit "Enter," and see it appear on the list.
