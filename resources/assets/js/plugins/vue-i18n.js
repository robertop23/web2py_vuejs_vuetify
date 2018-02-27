import Vue from 'vue'
import VueI18n from 'vue-i18n'

Vue.use(VueI18n)
//const locale = window.navigator.userLanguage || window.navigator.language

const locale = window.config['locale']
const translations = window.config.translations

const i18n = new VueI18n({
  locale,
  messages: {
    [locale]: translations
  }
})

export default i18n
