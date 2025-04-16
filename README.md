# PASSWORD GENERATOR & MANAGER 🔐

A Python GUI application built with Tkinter to help users generate strong, secure passwords and store them safely. It features a simple and clean interface with data confirmation prompts, and stores credentials in a local `.txt` file for easy access.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How it Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Lessons Learned](#lessons-learned)
- [Screenshots](#screenshots)

## Overview

This project combines a password generator and a minimal password manager. It allows users to generate random passwords with one click, fill in login details for various websites, confirm the information, and store it in a local file securely.

## Features

- ✅ One-click secure password generation
- ✅ Auto-fill email field for convenience
- ✅ Confirmation popup before saving credentials
- ✅ Data storage in structured format (`website | email | password`)
- ✅ Simple Tkinter-based user interface

## How it Works

1. **Enter Details**: Fill in the website and email/username fields.
2. **Generate Password**: Click the “Generate Password” button to create a secure password automatically.
3. **Add Entry**: After reviewing the confirmation popup, click "OK" to save the data to `data.txt`.
4. **View Data**: Open `data.txt` to see the stored entries in a structured format.

## Technologies Used

- **Python**: Core programming language
- **Tkinter**: GUI creation and input management
- **random / string**: For password generation logic
- **file handling**: Used to write and store data in a `.txt` file

## Lessons Learned

- Mastered building multi-file GUI applications using Tkinter
- Improved modular code structure using classes and separation of logic
- Practiced file I/O operations and data formatting
- Implemented validation and confirmation dialogs to enhance UX

## Screenshots

### 🖥️ Main UI Interface
![Main GUI](https://github.com/rautpdr/Password_Generator/assets/placeholder/8162e061-9e44-49cc-8a7b-603664ade449.png)

### 🔐 Confirmation Popup
![Confirmation](https://github.com/rautpdr/Password_Generator/assets/placeholder/439053c7-874a-4255-8f16-84d975274cba.png)

### 🗂️ Data Stored in Text File
![Saved Data](https://github.com/rautpdr/Password_Generator/assets/placeholder/616a9f38-b3c5-4cd3-a66e-2f69e86eb7cd.png)

