FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli@5.0.8 -g && npm install --save axios@1.2.1 vuex@4.1.0 bootstrap@5.2.3

COPY package.json .
COPY package-lock.json .
RUN npm install

CMD ["npm", "run", "serve"]
