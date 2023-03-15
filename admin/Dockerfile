FROM node:16.19.1-alpine3.17 as builder

WORKDIR /app

COPY ./package.json /app/

RUN yarn install

COPY . /app/

RUN yarn run admin:build

FROM nginx:alpine

WORKDIR /app

COPY --from=builder /app/build /var/www/app/static

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
