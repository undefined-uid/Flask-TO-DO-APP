# Flask Todo App

A basic Todo web application built with **Flask** and **SQLAlchemy**.

I'm building this project mainly to practice the fundamentals of building a web application with Flask, especially **CRUD operations**, database interaction, routing, and working with forms.

## Features

* Create new tasks
* View tasks
* Edit existing tasks
* Delete tasks
* Mark tasks as completed
* View:

  * All tasks
  * Pending tasks
  * Completed tasks
* Pending tasks are shown by default on the home page
* Edit tasks directly from the same page

## Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* HTML
* CSS

## CRUD Operations

This project is mainly for practicing CRUD:

| Operation | Description                                 |
| --------- | ------------------------------------------- |
| Create    | Add a new todo                              |
| Read      | View todos                                  |
| Update    | Edit a todo or change its completion status |
| Delete    | Remove a todo                               |

## Project Structure

```text
todo-app/
│
├── app.py
├── templates/
│   └── home.html
├── static/
│   └── style.css
├── instance/
│   └── todo.db
├── requirements.txt
└── README.md
```

> The exact structure may change as the project develops.

## How It Works

The home page contains three task filters:

```text
All Tasks | Pending | Completed
```

When the user logs in, **Pending** tasks are displayed by default.

The same page is used for all three views rather than creating separate pages for each filter.

Tasks can also be edited directly from the home page without navigating to a separate edit page.

## Running the Project

Clone the repository:

```bash
git clone <repository-url>
cd todo-app
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### macOS / Linux

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
flask run
```

Then open the local URL shown by Flask in your browser.

## Project Goal

The goal of this project is not to build a feature-complete Todo application.

It is a small project for practicing:

* Flask routing
* Request handling
* HTML forms
* SQLAlchemy models
* Database queries
* CRUD operations
* Working with templates
* Updating the UI based on application state

## Future Improvements

Possible features to add later:

* User authentication
* Due dates
* Task priorities
* Task categories
* Search
* Better validation
* Improved UI
* REST API
* JavaScript-based interactions

## Status

🚧 **Work in progress**

This project is being built as part of my learning journey with Flask and web development.
