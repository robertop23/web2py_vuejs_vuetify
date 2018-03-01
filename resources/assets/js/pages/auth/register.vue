<template>
  <v-layout row>
    <v-flex xs12 sm8 offset-sm2 lg4 offset-lg4>
      <v-card>
        <progress-bar :show="form.busy"></progress-bar>
        <form @submit.prevent="register" @keydown="form.onKeydown($event)">
          <v-card-title primary-title>
            <h3 class="headline mb-0">{{ $t('register') }}</h3>
          </v-card-title>
          <v-card-text>

            <!-- Name -->
            <text-input
              :form="form"
              :label="$t('first_name')"
              :v-errors="errors"
              :value.sync="form.first_name"
              counter="30"
              name="name"
              v-validate="'required|max:30'"
            ></text-input>

            <!-- Last Name -->
            <text-input
              :form="form"
              :label="$t('last_name')"
              :v-errors="errors"
              :value.sync="form.last_name"
              counter="30"
              name="name"
              v-validate="'required|max:30'"
            ></text-input>

            <!-- Email -->
            <email-input
              :form="form"
              :label="$t('email')"
              :v-errors="errors"
              :value.sync="form.email"
              name="email"
              v-validate="'required|email'"
            ></email-input>

            <!-- Password -->
            <password-input
              :form="form"
              :hint="$t('password_length_hint')"
              :v-errors="errors"
              :value.sync="form.password"
              v-on:eye="eye = $event"
              v-validate="'required|min:6'"
            ></password-input>

            <!-- Password Confirmation -->
            <password-input
              :form="form"
              :hide="eye"
              :label="$t('confirm_password')"
              :v-errors="errors"
              :value.sync="form.password_confirmation"
              data-vv-as="password"
              hide-icon="true"
              name="password_confirmation"
              v-validate="'required|confirmed:password'"
            ></password-input>
            
          </v-card-text>
          <v-card-actions>
            <submit-button :block="true" :form="form" :label="$t('register')"></submit-button>
          </v-card-actions>
        </form>
      </v-card>
    </v-flex>
  </v-layout>

</template>

<script>
import Form from 'vform'

export default {
  name: 'register-view',
  metaInfo () {
    return { title: this.$t('register') }
  },

  data: () => ({
    form: new Form({
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      password_confirmation: ''
    }),
    eye: true
  }),

  methods: {
    async register () {
      if (await this.formHasErrors()) return

      // Register the user.
      await this.form.post(this.$baseURL + 'api/register')
      // Log in the user.
      const { data: { token } } = await this.form.post(this.$baseURL + 'api/login')
      // Save the token.
      this.$store.dispatch('saveToken', {
        token: token
      })

      // Update the user.
      await this.$store.dispatch('fetchUser')

      // Redirect home.
      this.$router.push({ name: 'home' })
    }
  }
}
</script>
