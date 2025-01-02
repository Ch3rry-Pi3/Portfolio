# Use a lightweight Node.js image based on Alpine Linux
FROM node:19-alpine

# Copy the package.json file into the container's /app directory
COPY package.json /app/

# Copy the source code (e.g., server.js) into the container's /app directory
COPY src /app/

# Set the working directory inside the container to /app
WORKDIR /app

# Install the project dependencies defined in package.json
RUN npm install

# Specify the command to run the Node.js application when the container starts
CMD ["node", "server.js"]