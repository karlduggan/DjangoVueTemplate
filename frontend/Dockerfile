FROM node:14

WORKDIR /app

COPY package*.json ./

# RUN npm install
RUN npm install

COPY . .
# Build your Vue.js project
# RUN npm run build

CMD ["npm", "run", "serve"]


