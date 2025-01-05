# Summary

This project aims to simplify database management by using a code-first approach. It leverages migrations to handle schema changes and seeders to populate the database with initial data on development or testing environments.

# Prerequisites

Node.js (v14 or higher)
npm (v6 or higher)

# Installation

1. install dependencies:
   ```bash
   npm install
   ```
2. Setup environment variables by creating a .env file; see .env.example file at root level of the project

# Usage

Run npm run db-migrate to run dependencies; by default env variables are used to connect to the DB, config file is dynamic and uses such configuration to populate the fields as security measure to avoid unwanted changes on production instances
Run npm run db-seed to seed database with data for development or testing purposes
Create as many seeders as needed, project comes with faker for complex data types generation