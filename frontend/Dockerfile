FROM node:20

RUN npm install -g pm2

RUN mkdir /app
COPY . /app

WORKDIR /app

RUN yarn install
# RUN yarn robots
# RUN yarn sitemap
RUN yarn build

EXPOSE 3000
CMD [ "pm2-runtime", "start", "./ecosystem.config.js" ]
