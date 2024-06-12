# ecospheres-sitemap

Génère le sitemap pour ecologie.data.gouv.fr en utilisant l'API publique de data.gouv.fr.

- Récupère les `Topic` taggués `univers-ecospheres`
- Construit un sitemap avec
    - Les `Topic` récupérés plus haut, la date de dernière modification est celle du `Topic`
    - Les pages statiques indiquées dans `STATIC_URLS`, la date de dernière modification est celle du header `last-modified`
- Publie `sitemap.xml` sur un déploiement Github pages ➡️
