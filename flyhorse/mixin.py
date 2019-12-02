from django.utils import timezone
import datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test

"""
Verifica si el usuario no Inicio Sesión
"""
def user_login(user):
	return user.is_authenticated != True

"""
Verifica si el usuario Inicio Sesión y es Admininistrador del Sistemas
"""
def user_admin(user):
    return (user.is_authenticated == True) and (user.type_u.codigo =='admin')

"""
Verifica si el usuario Inicio Sesión y es Admininistrador de Carreras
"""
def user_encar(user):
    return (user.is_authenticated == True) and (user.type_u.codigo == 'encar')

"""
Verifica si el usuario Inicio Sesión y es Admininistrador de Transacciones
"""
def user_trans(user):
    return (user.is_authenticated == True) and (user.type_u.codigo == 'trans')

"""
Verifica si el usuario Inicio Sesión y es Usuario Apostador
"""
def user_user(user):
    return (user.is_authenticated == True) and (user.type_u.codigo == 'user')


"""
Verifica si el usuario Inicio Sesión y es Admininistrador del Sistemas o Admininistrador de Carreras
"""
def admin_encar(user):
    return (user.is_authenticated == True) and (user.type_u.codigo == 'admin' or user.type_u.codigo == 'encar')


"""
Verifica si el usuario Inicio Sesión y es Admininistrador del Sistemas o Admininistrador de Carreras
"""
def user_trans(user):
    return (user.is_authenticated == True) and (user.type_u.codigo == 'user' or user.type_u.codigo == 'trans')

"""
Verifica si el usuario Inicio Sesión y es Admininistrador del Sistemas o Usuario Apostador
"""

def user_admin(user):
    return (user.is_authenticated == True) and (user.type_u.codigo == 'user' or user.type_u.codigo == 'admin')

"""
Mixin que guarda la Ultima Conexion que Tuvo el Usuario
"""
class LastAccessMixin(object):
    def dispatch(self, request, *args, **kwargs):
        request.user.last_access = timezone.now()
        request.user.save(update_fields=['last_access'])
        return super(LastAccessMixin, self).dispatch(request, *args, **kwargs)

"""
Mixin que verifica si el Usuario Inicio Sesion y 
si no lo hizo lo devuelve al index
"""
class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

"""
Mixin que verifica si el Usuario Inicio Sesion y 
si lo hizo no puede volver al index, lo devuelve a 
la pagina de inico para los usuarios
"""
class LoginAuthenticatedMixin(object):
    @method_decorator(user_passes_test(user_login,login_url='inicio'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginAuthenticatedMixin, self).dispatch(request, *args, **kwargs)

"""
Mixin que verifica si el Usuario Inicio Sesion 
y es Administrador del Sistema, si no lo es, 
lo devuelve a la pagina de inico para los usuarios
"""
class AuthenticatedAdminMixin(object):
    @method_decorator(user_passes_test(user_admin, login_url=''))
    def dispatch(self, request, *args, **kwargs):
        return super(AuthenticatedAdminMixin, self).dispatch(request, *args, **kwargs)

"""
Mixin que verifica si el Usuario Inicio Sesion 
y es Administrador de Carreras, si no lo es, 
lo devuelve a la pagina de inico para los usuarios
"""
class AuthenticatedEncarMixin(object):
    @method_decorator(user_passes_test(user_encar, login_url=''))
    def dispatch(self, request, *args, **kwargs):
        return super(AuthenticatedEncarMixin, self).dispatch(request, *args, **kwargs)

"""
Mixin que verifica si el Usuario Inicio Sesion 
y es Administrador de Transacciones, si no lo es, 
lo devuelve a la pagina de inico para los usuarios
"""
class AuthenticatedTransMixin(object):
    @method_decorator(user_passes_test(user_trans, login_url=''))
    def dispatch(self, request, *args, **kwargs):
        return super(AuthenticatedTransMixin, self).dispatch(request, *args, **kwargs)

"""
Mixin que verifica si el Usuario Inicio Sesion 
y es Usuario Apostador, si no lo es, 
lo devuelve a la pagina de inico para los usuarios
"""
class AuthenticatedUserMixin(object):
    @method_decorator(user_passes_test(user_user, login_url=''))
    def dispatch(self, request, *args, **kwargs):
        return super(AuthenticatedUserMixin, self).dispatch(request, *args, **kwargs)

"""
Mixin que verifica si el Usuario Inicio Sesion 
y es Administrador o Encargado, si no lo es, 
lo devuelve a la pagina de inico para los usuarios
"""
class AuthorizedUserMixin(object):
    @method_decorator(user_passes_test(admin_encar, login_url=''))
    def dispatch(self, request, *args, **kwargs):
        return super(AuthorizedUserMixin, self).dispatch(request, *args, **kwargs)


"""
Mixin que verifica si el Usuario Inicio Sesion 
y es Usuario o Transaccion, si no lo es, 
lo devuelve a la pagina de inico para los usuarios
"""
class AuthorizedUser2Mixin(object):
    @method_decorator(user_passes_test(user_trans, login_url=''))
    def dispatch(self, request, *args, **kwargs):
        return super(AuthorizedUser2Mixin, self).dispatch(request, *args, **kwargs)

"""
Mixin que verifica si el Usuario Inicio Sesion 
y es Usuario o Transaccion, si no lo es, 
lo devuelve a la pagina de inico para los usuarios
"""
class AuthorizedUser3Mixin(object):
    @method_decorator(user_passes_test(user_admin, login_url=''))
    def dispatch(self, request, *args, **kwargs):
        return super(AuthorizedUser3Mixin, self).dispatch(request, *args, **kwargs)

"""
NOTA: Para la utilizacion de los Mixins en las vistas 
basadas en clases primero entra como parametro la Mixin 
y despues la Vista Generica
"""
