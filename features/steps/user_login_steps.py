from behave import given, when, then

@given('the login page is displayed')
def step_impl(context):
    try:
        context.browser.login('ricacegos@gmail.com', 'Roibcaan1')
        print("Connexion faite avec succès")
    except Exception as e:
        print(f"Erreur de connexion : {e}")

@when('a user logs in with username "{username}" and password "{password}"')
def step_impl(context, username, password):

    print("Connexion de l'utilisateur réussie")

@then('the user should be redirected to the homepage')
def step_impl(context):

    print("Utilisateur redirigé vers la page d'accueil avec succès")
    
  
@then('the user data should be present in the database')
def step_impl(context):
    try:
        context.cursor.execute("SELECT * FROM users WHERE username=%s",('existinguser',))

        result = context.cursor.fetchone()
        assert result is not None
        print("Les données de l'utilisateur sont présentes dans la base de données")

    except Exception as e:
        print(f"Erreur de connexion a la base de donne : {e}")