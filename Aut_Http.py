import hug

admin_area = hug.http(requires=hug.authentication.basic(hug.authentication.verify('Anthony', '1234')))



@admin_area.get('/admin/hello')
def admin_hello():
    return 'Bienvenido Anthony'




