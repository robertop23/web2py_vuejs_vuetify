export default ({ authGuard, guestGuard }) => [
  { path: '/' + window.config.appName + '/', name: 'welcome', component: require('~/pages/welcome.vue') },

  // Authenticated routes.
  ...authGuard([
    { path: '/' + window.config.appName + '/home', name: 'home', component: require('~/pages/home.vue') },
    { path: '/' + window.config.appName + '/settings',
      component: require('~/pages/settings/index.vue'),
      children: [
      { path: '/' + window.config.appName + '', redirect: { name: 'settings.profile' } },
      { path: '/' + window.config.appName + '/profile', name: 'settings.profile', component: require('~/pages/settings/profile.vue') },
      { path: '/' + window.config.appName + '/password', name: 'settings.password', component: require('~/pages/settings/password.vue') }
    ] }
  ]),

  // Guest routes.
  ...guestGuard([
    { path: '/' + window.config.appName + '/login', name: 'login', component: require('~/pages/auth/login.vue') },
    { path: '/' + window.config.appName + '/register', name: 'register', component: require('~/pages/auth/register.vue') },
    { path: '/' + window.config.appName + '/password/reset', name: 'password.request', component: require('~/pages/auth/password/email.vue') },
    { path: '/' + window.config.appName + '/password/reset/:token', name: 'password.reset', component: require('~/pages/auth/password/reset.vue') }
  ]),

  { path: '/' + window.config.appName + '*', component: require('~/pages/errors/404.vue') }
]
