package com.convo.chatapp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        int portNumber = 9500; // Choose any available port number

        try {
            // Start a server socket to listen for incoming connections
            ServerSocket serverSocket = new ServerSocket(portNumber);
            System.out.println("Waiting for other clients to connect...");

            // Start a thread to handle incoming connections from other clients
            Thread serverThread = new Thread(() -> {
                try {
                    Socket clientSocket = serverSocket.accept();
                    System.out.println("Another client connected: " + clientSocket.getInetAddress());

                    // Start a thread to handle communication with the other client
                    Thread clientThread = new Thread(() -> {
                        try {
                            BufferedReader input = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

                            // Read messages from the other client and display them
                            String message;
                            while ((message = input.readLine()) != null) {
                                System.out.println("Other client: " + message);
                            }
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                    });
                    clientThread.start();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            });
            serverThread.start();

            // Start a thread to send messages to the other client
            Thread senderThread = new Thread(() -> {
                try {
                    // Connect to the other client
                    Socket socket = new Socket("localhost", portNumber);
                    PrintWriter output = new PrintWriter(socket.getOutputStream(), true);

                    // Read messages from the user and send them to the other client
                    Scanner scanner = new Scanner(System.in);
                    String message;
                    while ((message = scanner.nextLine()) != null) {
                        output.println(message);
                    }

                    // Close the socket when done
                    socket.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            });
            senderThread.start();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}