# ecospheres-sitemap

Génère le sitemap pour ecologie.data.gouv.fr en utilisant l'API publique de data.gouv.fr.

- Récupère les `Topic` taggués `univers-ecospheres`
- Construit un sitemap avec
    - Les `Topic` récupérés plus haut, la date de dernière modification est celle du `Topic`
    - Les pages statiques indiquées dans `STATIC_URLS`, la date de dernière modification est celle du header `last-modified`
- Publie sur s3 le `sitemap.xml`

## Run with docker

```shell
docker build -t ecospheres-sitemap .
docker run -e ENV=demo -e AWS_ENDPOINT_URL=https://s3.example.com -e AWS_ACCESS_KEY_ID=key -e AWS_SECRET_ACCESS_KEY=secret ecospheres-sitemap
```
