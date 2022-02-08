logged_user = True

if logged_user:
    msg = "Usuário logado."
else:
    msg = "Usuário precisa logar."

print(msg)

#outra forma:

logged_user = True
msg2 = "Usuário logado." if logged_user else "Usuário precisa logar."
print(msg2)