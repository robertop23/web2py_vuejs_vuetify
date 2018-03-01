import axios from 'axios'
import store from '~/store'
import router from '~/router'
import i18n from './vue-i18n'

axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'

axios.interceptors.request.use(request => {
  if (store.getters.authToken) {
    request.headers.common['Authorization'] = `Bearer ${store.getters.authToken}`
  }
  return request
})

axios.interceptors.response.use(response => response, error => {
  const { status, data } = error.response

  if (status >= 500) {
    store.dispatch('responseMessage', {
      type: 'error',
      text: data,
      title: i18n.t('error_alert_title'),
      modal: true
    })
  }

  if (status == 400) {
    if (data == 'Token is expired'){
      store.dispatch('responseMessage', {
        type: 'warning',
        text: i18n.t('token_expired_alert_text'),
      })
      .then(async () => {
        await store.dispatch('logout')

        router.push({ name: 'login' })
      })
    }
    else {
      store.dispatch('responseMessage', {
        type: 'error',
        text: data,
      })
    }
  }

  if (status === 401 && store.getters.authCheck) {
    store.dispatch('responseMessage', {
      type: 'warning',
      text: i18n.t('token_expired_alert_text'),
      title: i18n.t('token_expired_alert_title'),
      modal: true
    })
    .then(async () => {
      await store.dispatch('logout')

      router.push({ name: 'login' })
    })
  }

  return Promise.reject(error)
})
