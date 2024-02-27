# Overview

I've developed a networking program that facilitates communication between two users in real-time. This program allows users to exchange messages seamlessly over a network, either through a client-server architecture or a peer-to-peer model. The goal behind creating this software was to deepen my understanding of networking concepts and enhance my skills as a software engineer.

To use the software, users need to run the provided Java application on their machines. If using the client-server model, one user should run the server application, while the other user(s) run the client application. If using the peer-to-peer model, each user should run the client application independently.

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

The architecture used in this program is primarily client-server, although it can also function in a peer-to-peer mode. TCP (Transmission Control Protocol) is employed for reliable, connection-oriented communication between clients and servers. The server listens on a specified port number (e.g., 9500), while clients connect to this port to establish communication.

Messages exchanged between clients and servers, or between peers, are formatted as simple text strings. Each message typically contains the sender's identifier and the actual content of the message.

# Development Environment

For developing this software, I utilized IntelliJ IDEA as my integrated development environment (IDE). The programming language used is Java, and I made extensive use of Java's built-in networking capabilities. Additionally, JavaFX was employed to create a graphical user interface (GUI) for the application, providing a more intuitive user experience.

# Useful Websites

During the development process, I found the following websites to be particularly helpful:
* [Oracle Java Documentation](https://docs.oracle.com/javase/8/docs/)
* [Baeldung](https://www.baeldung.com/)
* [GeeksforGeeks](https://www.geeksforgeeks.org/)

# Future Work

While the current version of the software fulfills basic messaging functionality, there are several areas that could be improved or expanded upon in the future:
* Implementing encryption for secure communication.
* Adding support for multimedia content such as images and files.
* Enhancing the GUI with more features and customization options.
* Optimizing the codebase for better performance and scalability.