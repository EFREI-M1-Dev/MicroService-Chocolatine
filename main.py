import requests


def get_codes():
    nbPosts = int(input("Combien de posts voulez-vous afficher ?"))

    for i in range(1, nbPosts+1):
        r = requests.get("https://jsonplaceholder.typicode.com/posts/" + str(i))
        print(r.json()['title'])


def get_users():
    nbUsers = int(input("Combien d'utilisateurs voulez-vous afficher ?"))

    for i in range(1, nbUsers+1):
        r = requests.get("https://jsonplaceholder.typicode.com/users/" + str(i))
        print(r.json()['name'])


def create_post():
    title = input("Écrivez un titre :")
    body = input("Écrivez un corps de texte :")

    data = {
        'title': title,
        'body': body
    }
    r = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

    if r.status_code == 201:
        print("La requête POST a réussi. Voici son ID :")
        print(r.json()['id'])
    else:
        print(f"La requête POST a échoué avec le code d'erreur : {r.status_code}")


def main():
    print("1 - Afficher des posts")
    print("2 - Afficher des users")
    print("3 - Ajouter un post")

    choice = input("Que voulez-vous faire ?")

    match choice:
        case "1":
            get_codes()
        case "2":
            get_users()
        case "3":
            create_post()
        case _:
            print("Valeur non reconnue")
            exit()


main()
