<template>
  <v-layout row>
    <v-flex xs12 sm2 offset-sm1 lg10 offset-lg1>
      <v-card>
        <progress-bar :show="busy"></progress-bar>
        <v-card-title primary-title class="grey lighten-4">
          <h3 class="headline mb-0">{{ $t('brands') }}</h3>
        </v-card-title>
        <v-data-table
          :headers="headers"
          :items="items"
          :loading="loading_data"
          class="elevation-1"
        >
          <v-progress-linear slot="progress" color="blue" indeterminate></v-progress-linear>
          <template slot="item" slot-scope="props">
            <td>{{ props.item.name }}</td>
            <td>{{ props.item.website }}</td>
            <td>{{ props.item.gift_website }}</td>
            <td>
              <router-link :to="{ name: 'brands.edit', params: {id:  props.item.id} }" class="nav-link" active-class="active">
                <v-icon color="blue darken-2">edit</v-icon>
              </router-link>
              <router-link :to="{ name: 'brands.delete', params: {id:  props.item.id} }" class="nav-link" active-class="active">
                <v-icon color="blue darken-2">delete</v-icon>
              </router-link>
            </td>
          </template>
        </v-data-table>
        </v-tabs>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>

import axios from 'axios'
import FeedbackMessage from '~/components/FeedbackMessage'

export default {
  name: 'brands-view',
  data () {
    return {
      busy: false,
      loading_data: true,
      brands: null,
      headers: [
        {
          text: 'Name',
          align: 'left',
          sortable: true,
          value: 'name',
        },
        { text: 'Website',
          align: 'left',
          sortable: true,
          value: 'website'
        },
        { text: 'Gift Website',
          align: 'left',
          sortable: true,
          value: 'gift_website' },
        { text: 'Actions',
          align: 'left',
          sortable: false,
          value: 'actions' },
      ],
      items: [
        {
          id: 1,
          name: 'Frozen Yogurt',
          website: 159,
          gift_website: 6.0,
        },
        {
          id: 2,
          name: 'Frozen Yogurt',
          website: 159,
          gift_website: 6.0,
        },
        {
          id: 3,
          name: 'Eclair',
          website: 159,
          gift_website: 6.0,
        }
      ]
    }
  },
  mounted() {
    this.listBrands()
    this.loading_data = false
  },
  methods: {
    async listBrands() {
      try {
        const data = await axios.get('/api/brands/list')
        console.log(data)
        this.brands = data.data
      } catch (e) {
        this.$store.dispatch('responseMessage', {
          type: 'warning',
          text: 'error loading brands'
        })
        console.log(e)
      }
    }
  }
}
</script>
