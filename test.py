# @app.route('/')
# @oidc.require_login
# def protected():
#     info = session['oidc_auth_profile']
#     username = info.get('preferred_username')
#     email = info.get('email')
#     sub = info.get('sub')
#     print("""user: %s, email:%s"""%(username, email))
#
#     token = oidc.get_access_token()
#     return ("""%s"""%token)
#
#
# @app.route('/private', methods=['POST'])
# @oidc.accept_token(require_token=True)
# def hello_api():
#     return("""user: %s, email:%s"""%(g.oidc_token_info['username'], g.oidc_token_info['preferred_username']))
#
#
# @app.route('/logout')
# def logout():
#     """Performs local logout by removing the session cookie."""
#     refresh_token = oidc.get_refresh_token()
#     oidc.logout()
#     if refresh_token is not None:
#         keycloak_openid.logout(refresh_token)
#     oidc.logout()
#     g.oidc_id_token = None
#     return 'Hi, you have been logged out! <a href="/">Return</a>'
