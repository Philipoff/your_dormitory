FROM node:16.19.1-alpine3.17 as builder

WORKDIR /app

COPY . /app/

RUN yarn && yarn client:build

FROM node:16.19.1-alpine3.17

WORKDIR /app

COPY --from=builder /app/.output /app/.output

CMD ["node", ".output/server/index.mjs"]