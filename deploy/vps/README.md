# VPS deploy — tamia4life.com

Phase 1 gate is **not met**. This hosts the §9.4 discovery page only.

## DNS (required before public HTTPS)

The domain is on Hostinger **parking** nameservers today (`athena.dns-parking.com`) and the A record is `2.57.91.91` (parking page). The VPS is:

| Type | Name | Value |
|---|---|---|
| A | `@` | `82.25.97.164` |
| A | `www` | `82.25.97.164` |
| AAAA | `@` | `2a02:4780:41:41c4::1` (optional) |
| AAAA | `www` | `2a02:4780:41:41c4::1` (optional) |

In Hostinger: switch the domain off parking DNS onto normal Hostinger DNS (or Cloudflare), then set the records above. Traefik will then issue Let's Encrypt via TLS-ALPN.

## Deploy

From the repo root (or this folder after rsync to `/opt/tamia4life` on the VPS):

```bash
deploy/vps/sync-html.sh
cd deploy/vps
docker compose up -d
```

`sync-html.sh` copies the canonical HTML plus `favicon.svg`, `favicon.ico`, and `apple-touch-icon.png` into `html/`.

Do not add a form to this page. Mailbox `hello@tamia4life.it` is still a placeholder.
