# Discord Webhook Tool

## Description

Ce programme permet d'envoyer des messages et des images à un webhook Discord, de gérer des webhooks, de "pirater" un webhook (simuler une conversation avec lui), et plus encore. Il offre une interface utilisateur interactive pour diverses opérations avec les webhooks Discord.

## Fonctionnalités

1. **Webhook Spam** : Envoyer un message à un webhook un certain nombre de fois.
2. **Envoyer un message avec une image** : Envoyer un message accompagné d'une image à un webhook.
3. **Pwn un Webhook** : Simuler une conversation avec un webhook en envoyant des messages à celui-ci.
4. **Gérer un Webhook** : Renommer, changer l'avatar ou supprimer un webhook.
5. **Attacher un Webhook** : Attacher un webhook à l'outil pour l'utiliser avec les différentes fonctionnalités.

## Prérequis

- Python 3.x
- La bibliothèque `requests` (peut être installée via `pip install requests`)

## Installation

1. Clonez le repository sur votre machine locale.

   ```bash
   git clone https://github.com/k0x3z/webhook-pwner.git
Installez les dépendances requises :

bash 
Copier le code
pip install requests
Utilisation
Attacher un Webhook
===============================
Lorsque vous exécutez le programme pour la première fois, vous devez attacher un webhook en fournissant son URL. Si vous en avez déjà un attaché, vous pouvez le changer à tout moment via l'option 6.

Options disponibles
Après avoir attaché un webhook, vous pouvez choisir parmi les différentes options suivantes :

[1] Webhook Spam : Envoyer un message à un webhook un certain nombre de fois.
[2] Envoyer un message avec une image : Envoyer un message avec une image attachée à un webhook.
[3] Pwn un Webhook : Simuler une conversation avec un webhook.
[4] Gérer un Webhook : Renommer, changer l'avatar ou supprimer le webhook.
[5] Quitter : Quitter le programme.
[6] Attacher un Webhook : Attacher un nouveau webhook ou changer celui actuellement attaché.
Exemple d'exécution

Lancement du programme :

bash
Copier le code
python webhook_tool.py
Vous verrez les options suivantes :

text
Copier le code
Options:
[1] Webhook Spam
[2] Envoyer un message avec une image
[3] Pwn un Webhook
[4] Gérer un Webhook
[5] Quitter
[6] Attacher un Webhook
Choisissez une option en entrant le numéro correspondant et suivez les instructions à l'écran.

Avertissements
Ce programme doit être utilisé de manière responsable et uniquement pour des tests légitimes avec des webhooks que vous possédez ou avez l'autorisation d'utiliser.
L'utilisation de ce programme sur des webhooks sans autorisation peut être illégale et contre les règles d'utilisation de Discord.
Contribuer
Si vous souhaitez contribuer à ce projet, veuillez ouvrir une pull request avec vos modifications.

License
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus d'informations.

markdown
Copier le code

### Explication

- **Description** : Cette section explique ce que fait le programme.
- **Fonctionnalités** : Liste des fonctionnalités principales du programme.
- **Prérequis** : Indique les dépendances nécessaires (ici, Python et `requests`).
- **Installation** : Instructions pour cloner le repository et installer les dépendances.
- **Utilisation** : Explique comment utiliser le programme, y compris les options disponibles.
- **Avertissements** : Conseils sur l'utilisation éthique du programme.
- **Contribuer** : Instructions pour les contributions ouvertes.

Vous pouvez ajuster ce modèle en fonction des détails spécifiques de votre programme ou de votre projet.
