v-list-tile<template>
  <div class="container">
    <div class="row">
      <accordion>
        <div class="card">
          <div class="card-header" role="tab" id="headingOne">
            <h5 class="mb-0">
              <a data-toggle="collapse" data-parent="#accordion" href="#serverDetails" aria-expanded="false" aria-controls="serverDetails">
                <fa icon="desktop" fixed-width/> {{ $t('your_server') }}
              </a>
            </h5>
          </div>

          <div id="serverDetails" class="collapse" role="tabpanel" aria-labelledby="headingOne">
            <div class="card-block">
              <table class="table table-striped">
                <tbody>
                  <tr>
                    <td>{{ $t('server_ip') }}: 192.168.0.1</td>
                  </tr>
                  <tr>
                    <td>{{ $t('server_status') }}: Running</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </accordion>
    </div>
    <div class="row">
      <card :title="$t('your_brands')" class="col-md-12">
        <router-link :to="{ name: 'brands.new' }" class="nav-link" active-class="active">
          <fa icon="plus" fixed-width/> {{ $t('new_brand') }}
        </router-link>
        <table class="table table-striped">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">{{ $t('brand_name') }}</th>
              <th scope="col">{{ $t('website') }}</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="brand in brands">
              <th scope="row">1</th>
              <td>{{ brand.name }}</td>
              <td>{{ brand.website }}</td>
              <td>
                <router-link :to="{ name: 'settings.edit_brand',params: {id: brand.id} }" class="nav-link" active-class="active">
                  <fa icon="pencil-alt" fixed-width/> {{ $t('action_edit_brand') }}
                </router-link>
              </td>
            </tr>
          </tbody>
        </table>
      </card>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  metaInfo () {
    return { title: this.$t('brands') }
  },

  data: () => ({
    brands: []
  }),

  mounted() {
    this.getBrands()
  },

  methods: {
    async getBrands() {
      try {
        const data = await axios.get('/api/brands/list')
        this.brands = data.data
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>
