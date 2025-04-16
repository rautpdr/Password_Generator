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
![Main GUI] ![image](https://github.com/user-attachments/assets/8f2a8323-cf99-47ca-9612-c5703fc93d7e)


### 🔐 Confirmation Popup
![Confirmation]![image](https://github.com/user-attachments/assets/5715ff27-78cf-4e35-bada-b801e8a3521c)


### 🗂️ Data Stored in Text File
![Saved Data]![image](https://github.com/user-attachments/assets/38de3904-d64d-4fe7-87eb-ca9344dc5d1e)


