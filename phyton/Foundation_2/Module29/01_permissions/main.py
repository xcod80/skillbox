import functools

user_permissions = ['admin']

def check_permission(user : str = 'None'):
    def permission_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if user in user_permissions:
                    return func(*args, **kwargs)
                else:
                    raise PermissionError(f'PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
            except PermissionError as PE:
                print(PE)
        return wrapper
    return permission_decorator

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()