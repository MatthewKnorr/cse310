// Include necessary libraries
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <ctime>
#include <windows.h>

// Forward declaration for the function defined later in the code
std::string getCurrentDateTime();

// Definition of the Task class
class Task {
public:
    // Constructor to initialize a task with a description and timestamp
    Task(const std::string& description) : description(description) {
        timestamp = getCurrentDateTime();
    }

    // Getter function for task description
    std::string getDescription() const {
        return description;
    }

    // Getter function for task timestamp
    std::string getTimestamp() const {
        return timestamp;
    }

    // Setter function for updating the timestamp
    void setTimestamp(const std::string& newTimestamp) {
        timestamp = newTimestamp;
    }

private:
    std::string description;
    std::string timestamp;
};

// Function to get current date and time as a string
std::string getCurrentDateTime() {
    std::time_t now = std::time(nullptr);
    std::tm timeInfo;

    // Use localtime_s instead of localtime to avoid deprecation warning
    if (localtime_s(&timeInfo, &now) != 0) {
        throw std::runtime_error("Error getting local time");
    }

    char buffer[80];
    std::strftime(buffer, sizeof(buffer), "%H:%M %m-%d", &timeInfo);

    return buffer;
}

// Definition of the FileHandler class
class FileHandler {
public:
    // Static function to save tasks to a file
    static bool saveTasksToFile(const std::vector<Task>& tasks, const std::string& filename) {
        // Open the file in append mode
        std::ofstream outputFile(filename, std::ios::app);

        // Check if the file is open
        if (outputFile.is_open()) {
            // Iterate through tasks and write them to the file
            for (const Task& task : tasks) {
                outputFile << task.getDescription() << " - " << task.getTimestamp() << '\n';
            }

            // Close the file and return success
            outputFile.close();
            return true;
        }

        // Return failure if unable to open the file
        return false;
    }

    // Static function to load tasks from a file
    static bool loadTasksFromFile(std::vector<Task>& tasks, const std::string& filename) {
        // Open the file
        std::ifstream inputFile(filename);

        // Check if the file is open
        if (inputFile.is_open()) {
            // Clear existing tasks before loading from the file
            tasks.clear();

            std::string taskDescription;

            // Read each line from the file and create a Task object
            while (std::getline(inputFile, taskDescription)) {
                Task loadedTask(taskDescription);
                loadedTask.setTimestamp(getCurrentDateTime());  // Set timestamp when adding to vector
                tasks.push_back(loadedTask);
            }

            // Close the file and return success
            inputFile.close();
            return true;
        }

        // Return failure if unable to open the file
        return false;
    }
};

// Function to clear the console screen on Windows or Linux/Unix
void clearScreen() {
    // Check if the code is being compiled on Windows
#ifdef _WIN32
    std::system("cls");
    // If not on Windows, assume a Unix-like system
#else
    std::system("clear");
#endif
}

// Function to set the console window size on Windows
void setConsoleWindowSize(int width, int height) {
    // Get the handle to the console
    HANDLE console = GetStdHandle(STD_OUTPUT_HANDLE);

    // Check if the console handle is valid
    if (console == INVALID_HANDLE_VALUE) {
        // Handle error
        return;
    }

    // Define the rectangle for setting the console window size
    SMALL_RECT rect = { 0, 0, static_cast<SHORT>(width - 1), static_cast<SHORT>(height - 1) };

    // Set the console window size
    SetConsoleWindowInfo(console, TRUE, &rect);
}

// Main function where the program execution begins
int main() {
    // Declare a vector to store tasks
    std::vector<Task> tasks;

    // Infinite loop for the main program menu
    while (true) {
        // Display the main menu options
        setConsoleWindowSize(70, 15);
        std::cout << "Welcome! Select one of the following options to get started.\n\n";
        std::cout << "1. View unsaved Tasks\n";
        std::cout << "2. Add Task\n";
        std::cout << "3. Remove Task\n";
        std::cout << "4. Save Tasks to File\n";
        std::cout << "5. Display Tasks from File\n";
        std::cout << "6. Remove Tasks From File\n";
        std::cout << "7. Exit\n\n";

        // Declare a variable to store user input
        std::string userInput;

        // Prompt the user for input
        std::cout << "What's Your Choice: ";

        // Read user input
        std::cin >> userInput;

        // Process the user's selected option
        if (userInput == "1") {
            // View unsaved Tasks
            if (!tasks.empty()) {
                std::cout << "\nUnsaved Tasks:\n";

                // Iterate through tasks and display them
                for (const Task& task : tasks) {
                    std::cout << task.getDescription() << " - " << task.getTimestamp() << '\n';
                }

                std::cout << '\n';
            }
            else {
                std::cout << "No unsaved tasks.\n\n";
            }
        }
        else if (userInput == "2") {
            // Add Task
            std::string newTaskDescription;
            std::cout << "You Selected: Add Task\n";
            std::cout << "Enter the new task: \n";

            // Ignore the newline character from the previous input
            std::cin.ignore();

            // Get the entire line, including spaces
            std::getline(std::cin, newTaskDescription);

            // Create a Task object and add it to the vector
            Task newTask(newTaskDescription);
            tasks.push_back(newTask);

            std::cout << "Task added successfully!\n\n";
        }
        else if (userInput == "3") {
            // Remove Task
            std::cout << "You Selected: Remove Task\n";

            // Check if tasks vector is not empty
            if (!tasks.empty()) {
                // Display tasks for removal
                std::cout << "Tasks for Removal:\n";

                // Iterate through tasks and display them with numbers
                for (size_t i = 0; i < tasks.size(); ++i) {
                    const Task& task = tasks[i];
                    std::cout << i + 1 << ". " << task.getDescription() << " - " << task.getTimestamp() << '\n';
                }

                std::cout << "Please enter the task number you'd like to remove (enter '*' to remove all tasks):\n\n";

                // Prompt user for task number to remove
                std::string removeTaskInput;
                std::getline(std::cin >> std::ws, removeTaskInput);

                if (removeTaskInput == "*") {
                    tasks.clear(); // Remove all tasks
                    std::cout << "All tasks removed successfully!\n\n";
                }
                else {
                    try {
                        // Convert user input to an integer
                        int removeTaskNumber = std::stoi(removeTaskInput);

                        // Check if the task number is valid
                        if (removeTaskNumber > 0 && removeTaskNumber <= tasks.size()) {
                            std::string removedTaskName = tasks[removeTaskNumber - 1].getDescription();
                            tasks.erase(tasks.begin() + removeTaskNumber - 1);
                            std::cout << "Task \"" << removedTaskName << "\" removed successfully!\n\n";
                        }
                        else {
                            std::cout << "Invalid task number.\n\n";
                        }
                    }
                    catch (const std::invalid_argument) {
                        std::cout << "Invalid input. Please enter a valid task number or '*'.\n\n";
                    }
                }
            }
            else {
                std::cout << "No tasks available to remove.\n\n";
            }
        }
        else if (userInput == "4") {
            // Save Tasks to File
            if (!tasks.empty()) {
                // Call the static function from FileHandler to save tasks to file
                if (FileHandler::saveTasksToFile(tasks, "tasks.txt")) {
                    std::cout << "Tasks saved to tasks.txt successfully!\n\n";
                    tasks.clear(); // Clear the tasks vector after saving
                }
                else {
                    std::cout << "Unable to save tasks to tasks.txt.\n\n";
                }
            }
            else {
                std::cout << "No unsaved tasks to save.\n\n";
            }
        }
        else if (userInput == "5") {
            // Display Tasks from File
            std::vector<Task> loadedTasks; // Temporary vector to store loaded tasks

            // Call the static function from FileHandler to load tasks from file
            if (FileHandler::loadTasksFromFile(loadedTasks, "tasks.txt")) {
                std::cout << "Tasks loaded from tasks.txt successfully!\n\n";

                // Display tasks from the loaded vector
                if (!loadedTasks.empty()) {
                    std::cout << "\nTasks from tasks.txt:\n";

                    // Iterate through loaded tasks and display only the task description
                    for (const Task& task : loadedTasks) {
                        std::cout << task.getDescription() << '\n';
                    }

                    std::cout << '\n';
                }
                else {
                    std::cout << "No tasks available in tasks.txt.\n\n";
                }
            }
            else {
                std::cout << "Unable to load tasks from tasks.txt.\n\n";
            }
        }
        else if (userInput == "6") {
            // Remove Tasks From File
            std::ifstream inputFile("tasks.txt");

            // Check if the file is open
            if (inputFile.is_open()) {
                std::string task;
                std::vector<std::string> fileTasks;

                // Display tasks from file with numbers
                std::cout << "\nTasks from File:\n";
                int lineNumber = 1;

                // Read each line from the file and display with line numbers
                while (std::getline(inputFile, task)) {
                    std::cout << lineNumber << ". " << task << '\n';
                    fileTasks.push_back(task);
                    lineNumber++;
                }

                // Close the file
                inputFile.close();

                // Prompt user for task number to remove
                std::cout << "Enter the task number you'd like to remove (enter '0' to cancel): ";
                std::string removeTaskInput;
                std::getline(std::cin >> std::ws, removeTaskInput);

                if (removeTaskInput == "0") {
                    std::cout << "Task removal canceled.\n\n";
                }
                else {
                    try {
                        // Convert user input to an integer
                        int removeTaskNumber = std::stoi(removeTaskInput);

                        // Check if the task number is valid
                        if (removeTaskNumber > 0 && removeTaskNumber <= lineNumber - 1) {
                            std::string removedTaskName = fileTasks[removeTaskNumber - 1];
                            fileTasks.erase(fileTasks.begin() + removeTaskNumber - 1);

                            // Write updated tasks back to the file
                            std::ofstream outputFile("tasks.txt");

                            // Check if the file is open
                            if (outputFile.is_open()) {
                                // Iterate through tasks and write them back to the file
                                for (const std::string& updatedTask : fileTasks) {
                                    outputFile << updatedTask << '\n';
                                }

                                // Close the file and inform about successful removal
                                outputFile.close();
                                std::cout << "Task \"" << removedTaskName << "\" removed from tasks.txt successfully!\n\n";
                            }
                            else {
                                std::cout << "Unable to open tasks.txt for writing.\n\n";
                            }
                        }
                        else {
                            std::cout << "Invalid task number.\n\n";
                        }
                    }
                    catch (const std::invalid_argument& e) {
                        std::cout << "Invalid input. Please enter a valid task number or '0' to cancel.\n\n";
                    }
                }
            }
            else {
                std::cout << "Unable to open tasks.txt for reading.\n\n";
            }
        }
        else if (userInput == "7") {
            // Exit
            std::cout << "You Selected: Exit\n";
            std::cout << "Exiting the program. Thank you!\n\n";
            break; // Exit the while loop
        }
        else {
            std::cout << "Invalid Option\n";
        }
    }

    return 0;
}