web2py vuejs vuetify

This is a proyect to integrate formally Web2py with Vue.JS

Include:
  - Vue.js
  - Vuetify
  - vee-validate
  - axios
  - vue-i18n
  - vue-router
  - more...

Instructions:

- npm install -> install node dependencies
- npm run watch -> compile node into static/public folder
- rename private/appconfig_example.ini to rename private/appconfig.ini and update this
- update routes dict from main routes.py to:

```
routers = dict(

    # base router
    BASE=dict(
        default_application='web2py_vuejs_vuetify',
    ),
    web2py_vuejs_vuetify=dict(
        default_function='index',
    )
)
```

The Vue files are inside resources folder

TODO:

  - Make all auth process
    - login
    - register
    - reset password
