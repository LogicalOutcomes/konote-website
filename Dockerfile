# Stage 1: Build with Hugo + Pagefind
FROM hugomods/hugo:go-git-0.157.0 AS builder
RUN apk add --no-cache nodejs npm
WORKDIR /src
COPY . .
RUN hugo --minify
RUN npx pagefind@latest --site public/en/ --output-subdir _pagefind/
RUN npx pagefind@latest --site public/fr/ --output-subdir _pagefind/

# Stage 2: Serve with Caddy
FROM caddy:2-alpine
COPY --from=builder /src/public /srv
COPY Caddyfile /etc/caddy/Caddyfile
EXPOSE 8080
