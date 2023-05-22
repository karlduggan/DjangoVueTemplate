FROM node:14

WORKDIR /app

COPY package*.json ./

RUN npm install

# COPY . .
COPY package*.json ./
RUN npm install && \
    npm install vuex vue-router axios

CMD ["npm", "run", "serve"]
