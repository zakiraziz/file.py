# Hey, I'm Zakir Aziz! 👋

### A passionate programmer from Pakistan 🇵🇰

![Welcome](https://images.unsplash.com/photo-1553484771-6f1b8f63b2f7) 

- 🔭 Currently working on: **Python Turtle Graphics Projects**
- 🌱 Learning about: **Functions, Recursion, and Color Patterns in Python**
- 👨‍💻 Exploring: **Creative Coding** and **Beautiful Design Elements**
- 💡 Always curious about **innovative programming concepts** and **visual artistry**!

---

### 🛠️ Languages & Tools:
- **Languages:** ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
- **Tools:** ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

---

### 💻 Projects
- **Python Turtle Graphics Art** - Crafting visually appealing patterns using code!
- **GitHub Profile Enhancement** - Adding creative and unique elements to make profiles stand out.

---

### 🌱 What I’m Learning:
- **Advanced Python Techniques** like recursion and algorithms.
- **Design** - How to combine code with aesthetics for beautiful user experiences.

---

### 📫 Let's Connect:
- LinkedIn: [Zakir Aziz](https://www.linkedin.com/)
- Email: zakir.aziz@example.com

---

### 📊 GitHub Stats:

![Zakir's GitHub stats](https://github-readme-stats.vercel.app/api?username=zakir-aziz&show_icons=true&theme=radical)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=zakir-aziz&layout=compact&theme=radical)

---

### ✨ Fun Fact:
I enjoy experimenting with **code** and **designs** that bring out the **beauty** in programming!

---

Thanks for visiting! Keep coding! 😊
Key Features:
Personalized Introduction: Highlights your journey as a passionate programmer from Pakistan.
Beautiful Visual Elements: Includes a header image for a welcoming touch.
Stats & Skills: GitHub stats and language tools help showcase your progress.
Project Highlights: Features current projects like Python Turtle Graphics and GitHub profile enhancement.
Design and Learning: Emphasizes your interests in creative coding and learning new techniques.

# Random Score Game 🎮

Welcome to the **Random Score Game**! This is a simple game written in Python where a random score is generated, and the highest score (hiscore) is saved in a file for future comparisons.

## How it works 🛠️

- Each time you play the game, a random score between 1 and 62 is generated.
- The game compares your score with the previous highest score (stored in a `hiscore.text` file).
- If your score is higher than the current hiscore, it updates the file with the new hiscore.
- The game is straightforward and offers a basic example of working with files and random numbers in Python.

## Code Explanation 📜

```python
import random

def game():
    print("you are playing the game..")
    score = random.randint(1, 62)
    # Fetch the hiscore
    with open("hiscore.text") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"your score: {score}")
    if(score > hiscore or hiscore == ""):
        # Write the new hiscore to the file
        with open("hiscore.text", "w") as f:
            f.write(str(score))

    return score

game()
How to Play 🕹️
Clone the repository to your local machine.
Ensure you have Python installed.
Run the script game.py.
Each time you run the game, it will generate a random score and update the highest score if your score beats the current hiscore.
Features 🎉
Random Score Generator: Generates a random score each time you play.
Hiscore Saving: Keeps track of the highest score across multiple games by saving it in a hiscore.text file.
File Handling: Demonstrates basic file reading and writing in Python.
Future Improvements 🚀
Add multiple difficulty levels.
Include more dynamic scoring mechanisms.
Create a graphical interface using libraries like tkinter or pygame.
Contributing 👥
Feel free to fork the repository, submit pull requests, or open issues to suggest improvements or report bugs!****
