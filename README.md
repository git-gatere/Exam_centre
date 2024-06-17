
---

# Exam Centre

## Table of Contents

- [About](#about)
- [Video Tutorial](#Exam_center_video.webm)
- [Technologies Used](#technologies-used)
- [Instructions](#instructions)
- [Contributing](#contributing)
- [License](#license)

## About

The Exam Centre Management System is a Python application designed to streamline the management of exam centers by storing and organizing data efficiently. The primary users of this application are invigilators who register candidates for specific subjects.

- Each candidate can only take one subject.
- An invigilator supervises exams in one room.
- Each subject is conducted in its own room.
- An invigilator can supervise multiple candidates.

## Video Tutorial

[/Exam_centre/Exam_center_video.webm](Exam_center_video.webm)

## Technologies Used

- Python
- SQLite (for database management)

## Instructions

1. **Fork and Clone the Repository**:
    - Fork this repository to your GitHub account.
    - Clone the forked repository to your local environment:
      ```bash
      git clone https://github.com/git-gatere/Exam_centre.git
      cd Exam_centre
      ```

2. **Set Up the Database**:
    - Run the following command to create the necessary database tables:
      ```bash
      python -m database.setup
      ```

3. **Run the Application**:
    - Start the application by running:
      ```bash
      python app.py
      ```

4. **Using the Application**:
    - The main menu provides options to manage candidates, invigilators, and subjects. Enter the number corresponding to the desired action:
      1. Add Candidate
      2. Add Subject
      3. Add Invigilator
      4. Display Candidates
      5. Display Subjects
      6. Display Invigilators
      7. Exit

    - Follow the prompts to add or display records. The application is designed to be user-friendly and self-explanatory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you would like to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](#license) file for details.

---

# MIT License

```markdown
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---