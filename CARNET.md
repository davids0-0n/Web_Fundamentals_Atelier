# 📒 Mon carnet de bord

**Nom :** Kouakou

**Prénom :** Joseph David Ophir

**Adresse de mon site :** https://davidson.pythonanywhere.com

> Modifiez ce fichier directement sur GitHub (icône crayon ✏️) pour répondre aux questions de chaque exercice.
> Écrivez avec vos propres mots : une réponse courte et juste vaut mieux qu'un long copier-coller ! 🙂

---

## 🟢 Exercice 1 — Mon premier déploiement

1. Où se trouve physiquement le code qui fabrique votre page : sur votre ordinateur, sur GitHub ou sur PythonAnywhere ?

   > _Ma réponse :_ GitHub

2. Pourquoi votre voisin(e) peut-il voir votre site, alors que vous n'avez rien installé sur son ordinateur ?

   > _Ma réponse :_ Parce que mon site tourne sur un serveur PythonAnywhere qui est connecté à internet en permanence et qui est accessible depuis une adresse publique.

---

## 🟢 Exercice 2 — Les URL et les routes

1. Dans l'URL `https://www.google.com/maps`, quel est le nom de domaine ? Quel est le chemin ?

   > _Ma réponse :_ Le nom de domaine est www.google.com, le chemin est /maps.

2. Que veut dire le message *Not Found* ? Qui l'a envoyé : votre navigateur ou le serveur ?

   > _Ma réponse :_ Le message *Not Found* veut dire que le serveur ne trouve pas le chemin indiqué. Il est envoyé par le serveur.

3. Que se passe-t-il si deux fonctions portent le même nom dans `flask_app.py` ? (Indice : essayez, puis lisez l'Error log.)

   > _Ma réponse :_ Le site ne démarre plus et affiche une erreur (« Something went wrong »), et ce sur toutes les pages, pas seulement la nouvelle. Dans l’Error log, on lit : AssertionError: View function mapping is overwriting an existing endpoint function: loisirs. Le log indique aussi l’endroit du problème : la ligne 37 de flask_app.py (@app.get("/test")). Flask utilise le nom de la fonction pour identifier chaque route : si deux fonctions ont le même nom, il y a un conflit et il refuse de lancer l’application. Il faut donc donner un nom différent à chaque fonction.

---

## 🔵 Exercice 3 — Le langage HTML

1. Quelle est la différence entre ce que le serveur **envoie** et ce que le navigateur **affiche** ?

   > _Ma réponse :_ Le serveur envoie seulement du code et le navigateur interprète ces balises et les transforme en page mise en forme.
2. À quoi servent les balises `<h1>`, `<p>`, `<ul>` et `<li>` ?

   > _Ma réponse :_ <h1> : le titre principal de la page.
                    <p> : un paragraphe de texte.
                    <ul> : une liste à puces, non ordonnée (unordered list).
                    <li> : un élément de la liste (list item), placé à l’intérieur de <ul>.

3. Pourquoi l'image s'affiche-t-elle alors qu'elle n'est pas sur votre serveur ?

   > _Ma réponse :_ Parce que la balise <img src="https://..."> contient l’adresse complète de l’image sur un autre serveur. Mon serveur envoie seulement le HTML. En le lisant, le navigateur voit l’adresse de l’image et envoie lui-même une deuxième requête à cet autre serveur pour la télécharger. Une page Web peut donc être fabriquée à partir de plusieurs serveurs différents.

---

## 🔵 Exercice 4 — Les templates

1. Pourquoi est-ce une bonne idée de séparer le code Python et le HTML ? (Pensez à une équipe avec un développeur et un graphiste.)

   > _Ma réponse :_ Chacun peut travailler sur sa partie sans gêner l’autre. Le développeur s’occupe du code Python. Le graphiste s’occupe des fichiers HTML dans templates/. Le graphiste n’a pas besoin de connaître Python, et le développeur ne risque pas de casser le design. Le code est aussi plus lisible, et on peut réutiliser le même template pour plusieurs pages en changeant seulement les données.

2. Les `{{ prenom }}` sont-ils remplacés par le serveur ou par le navigateur ? Comment l'avez-vous vérifié ?

   > _Ma réponse :_ Ils sont remplacés par le serveur. Je l’ai vérifié en affichant le code source de la page dans le navigateur. On n’y voit plus {{ prenom }}, mais directement la valeur. Le serveur remplace les variables avant d’envoyer le HTML, et le navigateur reçoit une page déjà complète.

---

## 🔵 Exercice 5 — Le CSS et les liens

1. Quelle est la différence de rôle entre le HTML et le CSS ?

   > _Ma réponse :_ Le HTML décrit le contenu et la structure de la page, le CSS décrit l’apparence.

2. Pour afficher votre page `/presentation`, combien de fichiers le navigateur doit-il télécharger ? (Vous pourrez le vérifier à l'exercice suivant !)

   > _Ma réponse :_ 3 fichiers.

3. Pourquoi faut-il parfois faire **Ctrl + F5** pour voir les changements de CSS ?

   > _Ma réponse :_ Parce que le navigateur garde une copie des fichiers déjà téléchargés dans son cache, pour aller plus vite la prochaine fois. Ctrl + F5 force le navigateur à retélécharger tous les fichiers depuis le serveur.

---

## 🟣 Exercice 6 — Espionner le navigateur

1. Que signifie HTTP ? Qui envoie la **requête** et qui envoie la **réponse** ?

   > _Ma réponse :_ HTTP veut dire HyperText Transfer Protocol. Le navigateur envoie la requête et le serveur renvoie la réponse.

2. Combien de requêtes votre page `/presentation` a-t-elle déclenchées ? Lesquelles ?

   > _Ma réponse :_ Avec le cache désactivé, l’onglet Réseau affiche 4 requêtes, mais seulement 2 viennent de mon site : presentation (la page HTML, code 200) et style.css (demandé par la ligne 6 du HTML, la balise <link>). Les deux autres (injectScript.js et injectScriptAdjust.js) sont lancées par content.js, c’est-à-dire par une extension de mon navigateur.

3. Que signifie le code `200` ? Et le code `404` de la favicon ?

   > _Ma réponse :_ 200 OK veut dire que la requête a réussi. 404 Not Found veut dire que le fichier demandé n’existe pas sur le serveur. Le navigateur cherche automatiquement une icône d’onglet favicon.ico, mais mon site n’en a pas. En ouvrant /favicon.ico, on obtient bien « Not Found ».

4. Pourquoi les modifications faites dans l'onglet Éléments ne sont-elles pas visibles par les autres visiteurs ?

   > _Ma réponse :_ Parce qu’elles modifient seulement la copie de la page chargée dans mon navigateur, sur mon ordinateur. Elles ne changent pas les fichiers sur le serveur. Les autres visiteurs reçoivent toujours la page envoyée par le serveur, et si je recharge la page, mes modifications disparaissent aussi. Pour modifier vraiment le site, il faut changer le code sur GitHub et le redéployer.

Défi : Pour presentation, le Content-Type vaut text/html; charset=utf-8. Pour style.css, il vaut text/css; charset=utf-8. Cet en-tête, envoyé par le serveur, indique au navigateur le type de fichier qu’il reçoit, pour qu’il sache comment le traiter : le HTML est affiché comme une page, le CSS est appliqué comme style. Le navigateur se fie à cet en-tête plutôt qu’à l’extension du fichier. La partie charset=utf-8 précise l’encodage des caractères, ce qui permet d’afficher correctement les accents (é, è, à…).
---

## 🟣 Exercice 7 — Envoyer des informations dans l'URL

1. Dans l'URL `https://www.youtube.com/results?search_query=chat`, quel est le nom du paramètre ? Quelle est sa valeur ?

   > _Ma réponse :_ Le paramètre s’appelle search_query et sa valeur est chat.

2. Pourquoi le serveur plante-t-il avec `a=bonjour` ? Que faudrait-il faire pour l'éviter ?

   > _Ma réponse :_ Le code Python essaie de transformer la valeur de a en nombre avec int(). Or "bonjour" n’est pas un nombre, donc Python lève une erreur , qui n’est pas gérée. Le serveur renvoie alors une erreur 500 (Internal Server Error). Pour l’éviter, il faut vérifier les données reçues avant de les utiliser : par exemple avec un try / except ValueError, ou en testant si la valeur est bien un nombre (.isdigit()). En cas de problème, on renvoie un message clair, comme « Veuillez entrer un nombre », au lieu de planter.

3. Pourquoi est-il dangereux d'afficher **tel quel** ce que l'utilisateur envoie ?

   > _Ma réponse :_ Parce que l’utilisateur peut écrire n’importe quoi dans l’URL, y compris du code HTML ou JavaScript (par exemple <script>alert('piraté')</script>). Si le serveur le renvoie tel quel dans la page, le navigateur l’exécute comme s’il faisait partie du site. 
---

## 🟣 Exercice 8 — Les formulaires

1. Quelle est la différence visible entre GET et POST ?

   > _Ma réponse :_ En GET, les données du formulaire apparaissent dans l’URL, après le ? : /salut?prenom=David&ville=Paris. En POST, l’URL reste simplement /salut : les données ne sont pas dans l’adresse, elles sont envoyées dans le corps de la requête. Le résultat affiché est le même (« Bonjour David, qui vient de Paris ! »), mais la façon de transmettre les données est différente.

2. Pour un formulaire de **recherche**, quelle méthode choisiriez-vous ? Et pour un formulaire de **connexion avec mot de passe** ? Pourquoi ?

   > _Ma réponse :_ Pour une recherche, je choisirais GET : la recherche apparaît dans l’URL, donc on peut l’ajouter aux favoris, la partager ou revenir en arrière (comme sur Google ou YouTube). Pour une connexion avec mot de passe, je choisirais POST : le mot de passe n’apparaît pas dans l’URL, donc il ne reste pas dans l’historique du navigateur, dans les journaux du serveur (Access log) ou dans un lien partagé par erreur.

3. Les données envoyées en POST sont-elles vraiment « secrètes » ? (Pensez à ce que vous avez vu dans l'onglet Réseau.)

   > _Ma réponse :_ Non. Elles sont seulement moins visibles, car elles ne sont pas dans l’URL. Dans l’onglet Réseau, en cliquant sur la requête salut puis sur l’onglet Payload, on voit clairement prenom=David et ville=Paris. N’importe qui ayant accès au navigateur peut les lire. Ce qui protège vraiment les données pendant le trajet sur Internet, c’est le HTTPS (le cadenas), qui chiffre la communication entre le navigateur et le serveur. POST + HTTPS est donc nécessaire pour un mot de passe.

---

## 🔴 Exercice 9 — Les codes de statut

1. Quelle est la différence entre une erreur `4xx` et une erreur `5xx` ? Qui est « fautif » dans chaque cas ?

   > _Ma réponse :_ Les codes 4xx sont des erreurs du client donc c'est lui le fautif. Les codes 5xx sont des erreurs du serveur donc c'est lui le fautif.

2. Comment fonctionne une redirection ? Qui fait la deuxième requête : le serveur ou le navigateur ?

   > _Ma réponse :_ Le serveur ne renvoie pas de page, mais un code 3xx avec un en-tête Location qui contient la nouvelle adresse. C’est le navigateur qui lit cet en-tête et envoie automatiquement une deuxième requête vers cette nouvelle adresse. 

3. Donnez un exemple de situation où un vrai site utilise une redirection.

   > _Ma réponse :_ Quand on tape http:// au lieu de https://, le site redirige automatiquement vers la version sécurisée en HTTPS. Autre exemple : quand on essaie d’ouvrir une page qui demande d’être connecté (comme sa boîte Gmail), le site redirige vers la page de connexion, puis, une fois connecté, redirige vers la page demandée au départ.

Défi : Le code 418 « I’m a teapot » (« Je suis une théière ») est une blague de l’IETF. Il vient d’un RFC publié le 1ᵉʳ avril 1998 (RFC 2324), qui décrit un faux protocole pour piloter des cafetières via Internet (HTCPCP). Un serveur qui est une théière doit répondre 418 si on lui demande de faire du café. Ce n’est pas un vrai code utilisé en pratique, mais beaucoup de sites et de logiciels l’ont gardé comme clin d’œil (par exemple google.com/teapot).
---

## 🔴 Exercice 10 — Ce que le serveur sait de vous

1. Citez trois informations que le serveur connaît sur vous, sans que vous ayez rien rempli.

   > _Ma réponse :_ Mon adresse IP, mon navigateur et mon système d’exploitation.

2. À quoi peut servir l'en-tête `Accept-Language` pour un site comme Wikipédia ?

   > _Ma réponse :_ Il indique au serveur dans quelle(s) langue(s) l’utilisateur préfère lire. Wikipédia peut s’en servir pour afficher automatiquement la page dans la bonne langue.

3. Dans l'Access log, retrouvez une requête qui a reçu un code `404`. Quelle page était demandée ?

   > _Ma réponse :_ Dans l’Access log, j’ai trouvé la ligne "GET /nimportequoi HTTP/1.1" 404. La page demandée était /nimportequoi, une route qui n’existe pas sur mon site (je l’avais tapée exprès pour tester ma page d’erreur 404). La ligne indique aussi mon adresse IP, la date et l’heure de la visite, la méthode (GET) et mon navigateur (Chrome sous Windows).

4. Après cet exercice, que pensez-vous de la notion de « navigation anonyme » ?

   > _Ma réponse :_ La navigation privée n’est pas vraiment anonyme. Elle n’enregistre rien sur mon ordinateur (pas d’historique, cookies effacés à la fermeture), mais elle ne cache rien au serveur. Celui-ci voit toujours mon adresse IP, mon navigateur, ma langue et les pages que je visite, et il les note dans ses journaux, comme on l’a vu dans l’Access log. Mon log contient même des visites que je n’ai pas faites moi-même (un robot python-requests, Discordbot) : le serveur enregistre tout le monde. Mon fournisseur d’accès ou le réseau de l’école peuvent aussi voir les sites visités. Pour cacher son adresse IP, il faudrait par exemple un VPN, et même là, l’anonymat n’est jamais total.

---

## 🔴 Exercice 11 — Le Web des machines : API et JSON

1. Quelle est la différence entre une page HTML et une réponse JSON ? À qui chacune est-elle destinée ?

   > _Ma réponse :_ Une page HTML contient du contenu mis en forme avec des balises : elle est destinée à un humain. Une réponse JSON contient seulement des données brutes, organisées sous forme de paires "clé": valeur sans mise en forme : elle est destinée à un programme.

2. Dans la page `/horloge`, quel code s'exécute sur le **serveur** et quel code s'exécute dans le **navigateur** ?

   > _Ma réponse :_ Sur le serveur, c’est le code Python de flask_app.py qui s’exécute : la route /horloge envoie la page HTML, et la route /api/heure calcule l’heure et la renvoie en JSON. Dans le navigateur, c’est le code JavaScript (dans la balise <script> de la page) qui s’exécute : il appelle régulièrement /api/heure avec fetch(), lit le JSON reçu, puis met à jour l’heure affichée sans recharger toute la page. 

3. Citez une application de votre téléphone qui, selon vous, utilise une API. Quelles données échange-t-elle ?

   > _Ma réponse :_ L’application Météo : elle envoie ma position (ou le nom de ma ville) à l’API d’un service météo, qui lui renvoie en JSON la température, le ciel prévu, le vent et les prévisions des prochains jours. L’application affiche ensuite ces données avec ses propres icônes et sa mise en page. 

---

## 🏁 Pour conclure

En quelques phrases, expliquez à un ami ce qui se passe entre le moment où il tape une adresse dans son navigateur et celui où la page s'affiche :

> _Ma réponse :_ Quand tu tapes une adresse (par exemple https://davidson.pythonanywhere.com/presentation), ton navigateur trouve d’abord l’adresse IP du serveur qui correspond au nom de domaine. Il lui envoie ensuite une requête HTTP du genre « donne-moi la page /presentation », avec au passage quelques infos sur toi. Le serveur reçoit cette requête, exécute son code, remplit le template HTML avec les bonnes données, puis renvoie une réponse : un code de statut (200 si tout va bien, 404 si la page n’existe pas, 500 si le serveur plante) et le contenu (en général du HTML). Ton navigateur lit ce HTML et, s’il y voit d’autres fichiers, il envoie une nouvelle requête pour chacun. Enfin, il assemble le tout et affiche la page mise en forme.
