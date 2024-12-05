# Real-Time-Chat-API
This project is a Real-Time Chat Application API built using Django Rest Framework (DRF). The API supports seamless real-time communication between users by utilizing both HTTP for traditional request-response interactions and WebSocket for real-time bi-directional communication. It is designed to handle efficient data storage and retrieval using MySQL, while Redis is employed as a caching tool to enhance performance and manage real-time data.

# Key Features :
# User Management

Secure user authentication and authorization using JWT.
Profile management and friend-list functionality.
# Real-Time Messaging

WebSocket integration for instant communication.
Support for one-on-one chats and group conversations.
Delivery and read receipt mechanisms.
# Message Storage and Retrieval

Persistent message storage in MySQL with optimized queries.
Message search and retrieval with pagination.
# Redis Caching

Real-time session management for active users.
Temporary storage of message queues and WebSocket events.
Caching frequently accessed data like user statuses and recent conversations.
# HTTP Endpoints

RESTful APIs for message history, chat creation, and user interactions.
Secure API endpoints with rate limiting.
# WebSocket Protocol

Event-driven architecture for real-time notifications and updates.
Handles disconnection gracefully, ensuring message delivery reliability.
# Scalable Design

Modular architecture to support future enhancements like video calls or media sharing.
Configured for horizontal scalability with Redis and WebSocket clustering.
# Tech Stack:

Backend Framework: Django Rest Framework
Database: MySQL
Real-Time Communication: WebSocket (via Django Channels)
Caching Layer: Redis
Authentication: JWT
