<template>
  <v-card flat>
    <form @submit.prevent="update" @keydown="form.onKeydown($event)">
      <v-card-title primary-title>
        <h5 class="subheading mb-0">{{ $t('your_info') }}</h5>
      </v-card-title>
      <v-card-text>

        <!-- Name -->
        <text-input
          :form="form"
          :label="$t('first_name')"
          :v-errors="errors"
          :value.sync="form.first_name"
          counter="30"
          name="first_name"
          v-validate="'required|max:30'"
        ></text-input>

        <!-- Last Name -->
        <text-input
          :form="form"
          :label="$t('last_name')"
          :v-errors="errors"
          :value.sync="form.last_name"
          counter="30"
          name="last_name"
          v-validate="'required|max:30'"
        ></text-input>

      </v-card-text>
      <v-card-actions>
        <submit-button :block="true" :form="form" :label="$t('update')"></submit-button>
      </v-card-actions>
    </form>
  </v-card>
</template>

<script>
import Form from 'vform'
import { mapGetters } from 'vuex'

export default {
  name: 'profile-view',
  data: () => ({
    form: new Form({
      first_name: '',
      last_name: ''
    })
  }),

  computed: mapGetters({
    user: 'authUser'
  }),

  created () {
    // Fill the form with user data.
    this.form.keys().forEach(key => {
      this.form[key] = this.user[key]
    })
  },

  methods: {
    async update () {
      if (await this.formHasErrors()) return

      this.$emit('busy', true)
      // Update profile
      const { data: { user } } = await this.form.patch(this.$baseURL + 'api/profile')
      // Update User data
      await this.$store.dispatch('updateUser', { user: user })
      this.$emit('busy', false)

      this.$store.dispatch('responseMessage', {
        type: 'success',
        text: this.$t('info_updated')
      })
    }
  }
}
</script>
