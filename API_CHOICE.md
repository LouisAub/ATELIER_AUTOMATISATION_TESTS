# API Choice

- Étudiant : Louis Aubert
- API choisie : ipify
- URL base : https://api.ipify.org
- Documentation officielle / README : https://www.ipify.org/
- Auth : None / API Key / OAuth
- Endpoints testés :
  - GET https://api.ipify.org?format=json
- Hypothèses de contrat (champs attendus, types, codes) :
  - Code HTTP attendu : 200
  - Réponse JSON contenant un objet
  - Champ obligatoire : ip (string)
- Limites / rate limiting connu :
  - Pas de limite officielle documentée
- Risques (instabilité, downtime, CORS, etc.) :
  - Dépendance à un service externe
  - Possibles interruptions de service
  - Latence variable selon charge réseau
