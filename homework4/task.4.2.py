import requests 
username = input("Введите имя пользователя на GitHub: ")
url = f'https://api.github.com/users/{username}'
response = requests.get(url)
if response.status_code == 200: # Если запрос выполнен успешно
    user_data = response.json()
    name = user_data.get('name', 'Не указано')
    login = user_data.get('login', 'Не указано')
    public_repos = user_data.get('public_repos', 'Не указано')
    print(f'Имя пользователя: {name}')
    print(f'Логин: {login}')
    print(f'Количество репозиториев: {public_repos}')