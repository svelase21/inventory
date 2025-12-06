# Frontend
FROM node:22.16.0

# Workdir
WORKDIR /app

# Copy package.json & package-lock.json
COPY package.json package-lock.json ./

# Install all dependencies
RUN npm install

# Copy all code
COPY . .

# EXPOSE the port when running Vite
EXPOSE 5173

# Running command to start
CMD ["npm", "run", "dev", "--", "--host"]