# Copyright 2025 Keisuke Tominaga a.k.a soundTricker
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Frontend Dockerfile for PPP Listener Web App
# Uses Node.js 22.16.0 for building and serving (SSR application)

# Build stage
FROM node:22.16.0-slim AS build
LABEL frontend_state=1

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy the rest of the application
COPY . .

# Build the application
RUN npm run build

# Production stage
FROM node:22.16.0-slim AS production

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install production dependencies only
RUN npm ci --omit=dev

# Install glob for API configuration script
RUN npm install glob

# Copy API configuration script
COPY api-config.js ./

# Copy built assets from the build stage
COPY --from=build /app/node_modules ./node_modules
COPY package*.json ./
COPY --from=build /app/build ./build
COPY --from=build /app/public ./public

# Environment variables
ENV PORT=8080
ENV NODE_ENV=production
ENV API_URL=""

# Expose port (Cloud Run will use the PORT environment variable)
EXPOSE 8080

# Start script to configure API and run server
COPY start.sh ./
RUN chmod +x start.sh

# Start the application
CMD ["./start.sh"]
