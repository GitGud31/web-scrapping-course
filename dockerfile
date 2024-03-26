# Use the official PostgreSQL image as base
FROM postgres:latest

# Set environment variables
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase

# Expose PostgreSQL port
EXPOSE 5432
