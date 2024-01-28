# Overview

The provided C++ program serves as a task management system, allowing users to interact with a console-based interface for managing tasks. The program provides various options, including:

- Viewing unsaved tasks
- Adding tasks
- Removing tasks
- Saving tasks to a file
- Displaying tasks from a file
- Removing tasks from a file
- Exiting the program

Upon running the program, users are presented with a menu, and they can choose from the available options by entering the corresponding number. The program maintains a vector of `Task` objects, where each task consists of a description and a timestamp. Users can add new tasks, remove tasks from the current session, and save unsaved tasks to a file named "tasks.txt." Additionally, users can load and display tasks from the file, as well as remove specific tasks from the file.

The program incorporates object-oriented principles by defining a `Task` class and a `FileHandler` class for managing file I/O operations. It utilizes vectors to store tasks and provides a clean and interactive user experience. The software showcases C++ language features such as classes, file handling, input/output, exception handling, and vector usage. Overall, it demonstrates the capability of C++ in implementing a simple yet functional console-based application for task management.

Welcome to the Task Manager, a coding project designed with the singular purpose of advancing my proficiency in C++ and propelling my programming journey to new heights. This software acts as a practical exploration ground, allowing me to delve into the intricacies of C++ and reinforce fundamental concepts such as variables, expressions, conditionals, loops, and functions. Additionally, it serves as a platform to explore the functionality of data structures from the Standard Template Library (STL).

The Task Manager goes beyond being a mere task management tool; it is a dynamic playground for experimenting with the language, tackling challenges, and expanding my coding capabilities. With stretch goals including file handling, inheritance, and dynamic memory allocation, this project serves as a personal tutor, guiding me beyond the basics and encouraging me to push the boundaries of my C++ proficiency. Whether I'm adding or removing tasks, saving and loading from files, or exploring the codebase, the Task Manager is my companion in this coding odyssey, providing hands-on experience and invaluable insights.

Here's to unlocking new levels of knowledge and mastery in C++.

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running and a walkthrough of the code. Focus should be on sharing what you learned about the language syntax.}

[Software Demo Video](https://youtu.be/zD-N7JwRtK8)

# Development Environment

- **IDE:** Visual Studio - Streamlined coding and compilation.
- **Language:** C++ - Leveraging object-oriented capabilities.
- **Libraries:** iostream, fstream, vector, string (STL) - Enhancing functionality.
- **Interface:** Command Line Interface (CLI) - User-friendly console interactions.

# Useful Websites

- [C++ Tutorial](https://www.w3schools.com/cpp/)
- [C++ language documentation](https://learn.microsoft.com/en-us/cpp/cpp/?view=msvc-170)
- [C++ Language](https://cplusplus.com/doc/tutorial/)
- [Learn C++ from scratch](https://www.educative.io/blog/how-to-learn-cpp-the-guide-for-beginners)

# Future Work

In the pursuit of enhancing the Task Manager, several exciting avenues for future development await exploration:

    - Sleek GUI Implementation: Elevate the user experience by integrating a complete and intuitive graphical user interface (GUI), transforming the current console-based interaction into a visually engaging platform.

    - Optimized Display: Elevate the clarity of the user interface by refining the clearScreen() class, ensuring a cleaner and more visually appealing display for seamless interaction.

    - Interactive File Selection: Enhance file handling by enabling dynamic user interaction. Allow users to enter file names, providing them with a visual list of available options and streamlining the selection process.

    - Multi-File Functionality: Extend the functionality to handle multiple .txt files, allowing users to specify the file they wish to manage. While the current configuration centers around "tasks.txt," envision a future where users can seamlessly switch between different file contexts.