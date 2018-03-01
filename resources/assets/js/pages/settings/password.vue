<template>
  <v-card flat>
    <form @submit.prevent="update" @keydown="form.onKeydown($event)">
      <v-card-title primary-title>
        <h5 class="subheading mb-0">{{ $t('your_password') }}</h5>
      </v-card-title>
      <v-card-text>

        <!-- Password -->
        <password-input
          :form="form"
          :hint="$t('password_length_hint')"
          :v-errors="errors"
          :value.sync="form.old_password"
          v-on:eye="eye = $event"
          name="old_password"
          v-validate="'required|min:6'"
        ></password-input>

        <!-- New Password -->
        <password-input
          :form="form"
          :hint="$t('password_length_hint')"
          :v-errors="errors"
          :value.sync="form.new_password"
          v-on:eye="eye = $event"
          v-validate="'required|min:6'"
        ></password-input>

        <!-- Password Confirmation -->
        <password-input
          :form="form"
          :hide="eye"
          :label="$t('confirm_password')"
          :v-errors="errors"
          :value.sync="form.new_password2"
          data-vv-as="new_password"
          hide-icon="true"
          name="new_password2"
          v-validate="'required|confirmed:password'"
        ></password-input>
        <!-- <form-feedback :form="form" :text="$t('password_updated')"></form-feedback> -->

      </v-card-text>
      <v-card-actions>
        <submit-button :block="true" :form="form" :label="$t('update')"></submit-button>
      </v-card-actions>
    </form>
  </v-card>
</template>

<script>
import Form from 'vform'

export default {
  name: 'password-view',
  data: () => ({
    form: new Form({
      old_password: '',
      new_password: '',
      new_password2: '',
    }),
    eye: true
  }),

  methods: {
    async update () {
      if (await this.formHasErrors()) return

      this.$emit('busy', true)

      await this.form.patch(this.$baseURL + 'api/change_password')

      this.form.reset()
      this.$emit('busy', false)

      this.$store.dispatch('responseMessage', {
        type: 'success',
        text: this.$t('password_updated')
      })
    }
  }
}
</script>
