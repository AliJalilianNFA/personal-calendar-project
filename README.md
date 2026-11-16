# Personal Calendar and Activity Management System

MBAN 5502 Programming Fundamentals — Group Project (Topic 6)

This repository contains two versions of the project:

1. **Python terminal application** — the main course project.
2. **Interactive web dashboard** — an additional browser-based demo for presentation and sharing.

## Repository Structure

```text
personal-calendar-project/
├── README.md
├── .gitignore
├── python_app/
│   ├── __init__.py
│   ├── main.py
│   ├── login.py
│   ├── activity_manager.py
│   ├── notes_manager.py
│   ├── data_manager.py
│   └── calendar_data.json
├── docs/
│   └── index.html
└── documentation/
    └── Project_Documentation.docx
```

## Python Application Features

- Login with Caesar-cipher encryption/decryption logic
- Maximum login attempts
- Add, display, update, and cancel activities
- Add and search upcoming meetings
- Detect overlapping schedule items
- Create, display, search, update, and delete notes
- Daily and weekly schedule summaries
- Total scheduled-hours calculation
- JSON-based data persistence
- Input validation for dates and time ranges

## Run the Python Application

From the repository root:

```bash
python python_app/main.py
```

The demo credentials included in `calendar_data.json` are:

```text
Username: ali
Password: 1234
```

These credentials are included only for the educational demo.

No external Python packages are required. The project uses Python standard-library modules such as `json`, `pathlib`, and `datetime`.

## Web Demo

The web version includes:

- Activity CRUD
- Meeting CRUD
- Note CRUD and search
- Conflict detection
- Daily and weekly summaries
- Scheduled-hours calculation
- JSON import/export
- Browser persistence using `localStorage`

Open locally:

```text
docs/index.html
```

### Publish with GitHub Pages

1. Push the repository to GitHub.
2. Open **Settings → Pages**.
3. Under **Build and deployment**, select **Deploy from a branch**.
4. Choose the `main` branch and `/docs` folder.
5. Save.

GitHub will provide a public URL for the interactive dashboard.

### Web Data Note

The GitHub Pages version is static. Data changes are stored in each user's own browser using `localStorage`; they are not automatically shared between group members. Use JSON Export/Import to move data between browsers.

## Documentation

Project documentation is available in:

```text
documentation/Project_Documentation.docx
```

## Course Scope

The Python terminal application is the core academic deliverable. The web dashboard is an optional enhancement for visualization and demonstration.


## Team Contributions

This project was completed as a group project. The core Python application was divided between team members as follows:

### [Satyam Verma](https://github.com/satyam96tennis) (`@satyam96tennis`)
- Developed the Login System
- Implemented username and password verification
- Implemented Caesar cipher encryption and decryption
- Added the maximum login-attempt logic


### [Dhruv Pankajkumar Patel](https://github.com/pateldhruv1312) (`@pateldhruv1312`)
- Developed the Activity and Meeting Management module
- Implemented activity creation, display, update, and cancellation
- Implemented meeting creation and upcoming-meeting search
- Implemented schedule conflict detection


### Ali Jalilian
- Developed the Data Management module
- Developed the Notes Management module
- Implemented daily and weekly schedule summaries
- Integrated the project modules in `main.py`
- Prepared the final project structure and documentation
- Created the interactive web dashboard as an additional visualization/demo layer for the GitHub version of the project

> The interactive web dashboard is an additional enhancement and is not presented as a replacement for the original team contributions to the Python application.

## GitHub Contributors

The repository is intended to credit all team members. GitHub's Contributors section is based on commit authorship, so each team member should make at least one commit from their own GitHub account, or be added as a verified co-author on a commit, for GitHub to list them automatically as contributors.
