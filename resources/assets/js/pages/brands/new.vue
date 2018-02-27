<template>
<card :title="edit ? $t('edit_brand'): $t('new_brand')">
  <form @submit.prevent="save" @keydown="form.onKeydown($event)" enctype="multipart/form-data">
    <alert-success :form="form" :message="$t('brand_updated')"/>
    <div class="bd-example bd-example-tabs" role="tabpanel">
      <ul class="nav nav-tabs" id="myTab" role="tablist">
        <li class="nav-item">
          <a class="nav-link active" id="basic-tab" data-toggle="tab" href="#basic" role="tab" aria-controls="basic" aria-expanded="true">{{ $t('brand_tab_basic') }}</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" id="accounts-tab" data-toggle="tab" href="#accounts" role="tab" aria-controls="accounts" aria-expanded="false">{{ $t('brand_tab_accounts') }}</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" id="seller-tab" data-toggle="tab" href="#seller" role="tab" aria-controls="seller" aria-expanded="false">{{ $t('brand_tab_sc') }}</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" id="questions-tab" data-toggle="tab" href="#questions" role="tab" aria-controls="questions" aria-expanded="false">{{ $t('brand_tab_questions') }}</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" id="mailchimp-tab" data-toggle="tab" href="#mailchimp" role="tab" aria-controls="mailchimp" aria-expanded="false">{{ $t('brand_tab_mailchimp') }}</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" id="activecampaign-tab" data-toggle="tab" href="#activecampaign" role="tab" aria-controls="activecampaign" aria-expanded="false">{{ $t('brand_tab_activecampaign') }}</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" id="images-tab" data-toggle="tab" href="#images" role="tab" aria-controls="images" aria-expanded="false">{{ $t('brand_tab_images') }}</a>
        </li>
      </ul>
      <div class="tab-content" id="myTabContent">
        <div class="tab-pane fade active show" id="basic" role="tabpanel" aria-labelledby="basic-tab" aria-expanded="true">
          <!-- Brand -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('name_brand') }}</label>
            <div class="col-md-7">
              <input v-model="form.name" type="text" name="name" class="form-control"
                :class="{ 'is-invalid': form.errors.has('name') }">
              <has-error :form="form" field="name"/>
            </div>
          </div>

          <!-- Website -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('website') }}</label>
            <div class="col-md-7">
              <input v-model="form.website" type="text" name="website" class="form-control"
                :class="{ 'is-invalid': form.errors.has('website') }">
              <has-error :form="form" field="website"/>
            </div>
          </div>

          <!-- Gift Website -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('gift_website') }}</label>
            <div class="col-md-7">
              <input v-model="form.gift_website_url" type="text" name="gift_website_url" class="form-control"
                :class="{ 'is-invalid': form.errors.has('gift_website_url') }">
              <has-error :form="form" field="gift_website_url"/>
            </div>
          </div>

          <!-- Tag -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('tag') }}</label>
            <div class="col-md-7">
              <input v-model="form.tag" type="text" name="tag" class="form-control"
                :class="{ 'is-invalid': form.errors.has('tag') }">
              <has-error :form="form" field="tag"/>
            </div>
          </div>
        </div>
        <div class="tab-pane fade" id="seller" role="tabpanel" aria-labelledby="seller-tab" aria-expanded="false">
          <!-- SC User name -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('sc_username') }}</label>
            <div class="col-md-7">
              <input v-model="form.sc_username" type="text" name="sc_username" class="form-control"
                :class="{ 'is-invalid': form.errors.has('sc_username') }">
              <has-error :form="form" field="sc_username"/>
            </div>
          </div>

          <!-- SC User password -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('sc_password') }}</label>
            <div class="col-md-7">
              <input v-model="form.sc_password" type="password" name="sc_password" class="form-control"
                :class="{ 'is-invalid': form.errors.has('sc_password') }">
              <has-error :form="form" field="sc_password"/>
            </div>
          </div>
        </div>
        <div class="tab-pane fade" id="accounts" role="tabpanel" aria-labelledby="accounts-tab" aria-expanded="false">
          <!-- Contact URL -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('contact_url') }}</label>
            <div class="col-md-7">
              <input v-model="form.contact_url" type="text" name="contact_url" class="form-control"
                :class="{ 'is-invalid': form.errors.has('contact_url') }">
              <has-error :form="form" field="contact_url"/>
            </div>
          </div>

          <!-- Facebook -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('facebook_user') }}</label>
            <div class="col-md-7">
              <input v-model="form.facebook" type="text" name="facebook" class="form-control"
                :class="{ 'is-invalid': form.errors.has('facebook') }">
              <has-error :form="form" field="facebook"/>
            </div>
          </div>

          <!-- Twitter -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('twitter_user') }}</label>
            <div class="col-md-7">
              <input v-model="form.twitter" type="text" name="twitter" class="form-control"
                :class="{ 'is-invalid': form.errors.has('twitter') }">
              <has-error :form="form" field="twitter"/>
            </div>
          </div>

          <!-- Instagram -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('instagram_user') }}</label>
            <div class="col-md-7">
              <input v-model="form.instagram" type="text" name="instagram" class="form-control"
                :class="{ 'is-invalid': form.errors.has('instagram') }">
              <has-error :form="form" field="instagram"/>
            </div>
          </div>

          <!-- PInterest -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('pinterest_user') }}</label>
            <div class="col-md-7">
              <input v-model="form.pinterest" type="text" name="pinterest" class="form-control"
                :class="{ 'is-invalid': form.errors.has('pinterest') }">
              <has-error :form="form" field="pinterest"/>
            </div>
          </div>
        </div>
        <div class="tab-pane fade" id="questions" role="tabpanel" aria-labelledby="questions-tab" aria-expanded="false">
          <!-- Question 1 -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('question_1') }}</label>
            <div class="col-md-7">
              <input v-model="form.question_1" type="text" name="question_1" class="form-control"
                :class="{ 'is-invalid': form.errors.has('question_1') }">
              <has-error :form="form" field="question_1"/>
            </div>
          </div>

          <!-- Question 2 -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('question_2') }}</label>
            <div class="col-md-7">
              <input v-model="form.question_2" type="text" name="question_2" class="form-control"
                :class="{ 'is-invalid': form.errors.has('question_2') }">
              <has-error :form="form" field="question_2"/>
            </div>
          </div>

          <!-- Question 3 -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('question_3') }}</label>
            <div class="col-md-7">
              <input v-model="form.question_3" type="text" name="question_3" class="form-control"
                :class="{ 'is-invalid': form.errors.has('question_3') }">
              <has-error :form="form" field="question_3"/>
            </div>
          </div>

          <!-- Question 4 -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('question_4') }}</label>
            <div class="col-md-7">
              <input v-model="form.question_4" type="text" name="question_4" class="form-control"
                :class="{ 'is-invalid': form.errors.has('question_4') }">
              <has-error :form="form" field="question_4"/>
            </div>
          </div>

          <!-- Question 5 -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('question_5') }}</label>
            <div class="col-md-7">
              <input v-model="form.question_5" type="text" name="question_5" class="form-control"
                :class="{ 'is-invalid': form.errors.has('question_5') }">
              <has-error :form="form" field="question_5"/>
            </div>
          </div>
        </div>
        <div class="tab-pane fade" id="mailchimp" role="tabpanel" aria-labelledby="mailchimp-tab" aria-expanded="false">
          <!-- MailChimp DC -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('mailchimp_dc') }}</label>
            <div class="col-md-7">
              <input v-model="form.mailchimp_dc" type="text" name="mailchimp_dc" class="form-control"
                :class="{ 'is-invalid': form.errors.has('mailchimp_dc') }">
              <has-error :form="form" field="mailchimp_dc"/>
            </div>
          </div>

          <!-- MailChimp Key -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('mailchimp_key') }}</label>
            <div class="col-md-7">
              <input v-model="form.mailchimp_key" type="text" name="mailchimp_key" class="form-control"
                :class="{ 'is-invalid': form.errors.has('mailchimp_key') }">
              <has-error :form="form" field="mailchimp_key"/>
            </div>
          </div>
        </div>
        <div class="tab-pane fade" id="activecampaign" role="tabpanel" aria-labelledby="activecampaign-tab" aria-expanded="false">
          <!-- Active Campaign URL -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('activecampaign_url') }}</label>
            <div class="col-md-7">
              <input v-model="form.activecampaign_url" type="text" name="activecampaign_url" class="form-control"
                :class="{ 'is-invalid': form.errors.has('activecampaign_url') }">
              <has-error :form="form" field="activecampaign_url"/>
            </div>
          </div>
          <!-- Active Campaign Key -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('activecampaign_key') }}</label>
            <div class="col-md-7">
              <input v-model="form.activecampaign_key" type="text" name="activecampaign_key" class="form-control"
                :class="{ 'is-invalid': form.errors.has('activecampaign_key') }">
              <has-error :form="form" field="activecampaign_key"/>
            </div>
          </div>
        </div>
        <div class="tab-pane fade" id="images" role="tabpanel" aria-labelledby="images-tab" aria-expanded="false">
          <!-- Active Campaign URL -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('logo_image') }}</label>
            <div class="col-md-7">
              <input type="file" name="logo_image" class="form-control" @change="validate_logo"
                :class="{ 'is-invalid': form.errors.has('logo_image') }">
              <has-error :form="form" field="logo_image"/>
            </div>
          </div>
          <!-- Active Campaign Key -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">{{ $t('background_image') }}</label>
            <div class="col-md-7">
              <input type="file" name="background_image" class="form-control" @change="validate_background"
                :class="{ 'is-invalid': form.errors.has('background_image') }">
              <has-error :form="form" field="background_image"/>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Submit Button -->
    <div class="form-group row" v-show="form.name!=''">
      <div class="col-md-9 ml-md-auto">
        <v-button type="success" :loading="form.busy">{{ edit ? $t('update'): $t('save') }}</v-button>
      </div>
    </div>
  </form>
</card>
</template>

<script>
import axios from 'axios'
import Form from 'vform'

export default {
  scrollToTop: false,

  metaInfo () {
    return { title: this.$t('settings') }
  },
  data: () => ({
    form: new Form({
      name: '',
      website: '',
      gift_website_url: '',
      sc_username: '',
      sc_password: '',
      contact_url: '',
      facebook: '',
      twitter: '',
      instagram: '',
      pinterest: '',
      tag: '',
      question_1: '',
      question_2: '',
      question_3: '',
      question_4: '',
      question_5: '',
      mailchimp_dc: '',
      mailchimp_key: '',
      activecampaign_url: '',
      activecampaign_key: ''
    }),
    logo: {
      width: 220,
      height: 64,
      size: 100
    },
    background: {
      width: 2000,
      height: 1000,
      size: 300
    },
    edit: false
  }),
  mounted() {
    this.edit = (this.$route.name == 'settings.edit_brand')
    if (this.edit) {
      this.getBrand()
    }
  },
  methods: {
    validate_logo() {
      var files = document.getElementsByName('logo_image')[0].files
      var size = files[0].size/1024
      var error = null
      this.form.errors.errors = {}
      if (size > this.logo.size) {
        error = this.$t('validate_image_size') + this.logo.size + " KB"
        this.form.errors.errors = {"logo_image" : [error]}
        this.clear_element('logo_image')
      } else {
        var reader = new FileReader()
        reader.readAsDataURL(files[0])
        let me = this
        reader.onload = function (e) {
          var image = new Image()
          image.src = e.target.result
          image.onload = function () {
            var height = this.height
            var width = this.width
            if (height != me.logo.height) {
              error = me.$t('validate_image_height')+me.logo.height
            } else if (width != me.logo.width) {
              error = me.$t('validate_image_width')+me.logo.width
            }
            me.form.errors.errors = {"logo_image" : [error]}
            me.clear_element('logo_image')
          }
        }
      }
    },
    validate_background() {
      var files = document.getElementsByName('background_image')[0].files
      var size = files[0].size/1024
      var error = null
      this.form.errors.errors = {}
      if (size > this.background.size) {
        error = this.$t('validate_image_size') + this.background.size + " KB"
        this.form.errors.errors = {"background_image" : [error]}
        this.clear_element('background_image')
      } else {
        var reader = new FileReader()
        reader.readAsDataURL(files[0])
        let me = this
        reader.onload = function (e) {
          var image = new Image()
          image.src = e.target.result
          image.onload = function () {
            var height = this.height
            var width = this.width
            if (height != me.background.height) {
              error = me.$t('validate_image_height')+me.background.height
            } else if (width != me.background.width) {
              error = me.$t('validate_image_width')+me.background.width
            }
            me.form.errors.errors = {"background_image" : [error]}
            me.clear_element('background_image')
          }
        }
      }
    },
    clear_element(element) {
      document.getElementsByName(element)[0].value = ''
      document.getElementsByName(element)[0].type = ''
      document.getElementsByName(element)[0].type = 'file'
    },
    async upload_logo() {
      let data = new FormData()
      var files = document.getElementsByName('logo_image')[0].files
      for (var i = 0; i < files.length; i++) {
        let file = files.item(i);
        data.append('logo_image', file, file.name);
      }
      const config = {headers: { 'content-type': 'multipart/form-data' } }
      return await axios.post('/api/settings/brand/logo/upload/'+this.$route.params.id, data, config)
    },
    async upload_background() {
      let data = new FormData()
      var files = document.getElementsByName('background_image')[0].files
      for (var i = 0; i < files.length; i++) {
        let file = files.item(i);
        data.append('background_image', file, file.name);
      }
      const config = {headers: { 'content-type': 'multipart/form-data' } }
      return await axios.post('/api/settings/brand/background/upload/'+this.$route.params.id, data, config)
    },
    async getBrand() {
      try {
        const data = await axios.get('/api/brand/'+this.$route.params.id)
        this.form.name = data.data.name
        this.form.website = data.data.website
        this.form.gift_website_url = data.data.gift_website_url
        this.form.sc_username = data.data.sc_username
        this.form.sc_password = data.data.sc_password
        this.form.contact_url = data.data.contact_url
        this.form.facebook = data.data.facebook
        this.form.twitter = data.data.twitter
        this.form.instagram = data.data.instagram
        this.form.pinterest = data.data.pinterest
        this.form.tag = data.data.tag
        this.form.question_1 = data.data.question_1
        this.form.question_2 = data.data.question_2
        this.form.question_3 = data.data.question_3
        this.form.question_4 = data.data.question_4
        this.form.question_5 = data.data.question_5
        this.form.mailchimp_dc = data.data.mailchimp_dc
        this.form.mailchimp_key = data.data.mailchimp_key
        this.form.activecampaign_url = data.data.active_campaign_url
        this.form.activecampaign_key = data.data.active_campaign_key
      } catch (e) {
        console.log(e)
      }
    },
    async save () {
      var url = ''
      try {
        if (this.edit) {
          url = '/api/settings/brand/update/'+this.$route.params.id
        } else {
          url = '/api/settings/brand/save'
        }
        const data = this.form.patch(url)
        if (document.getElementsByName('logo_image')[0].files.length > 0) {
          this.upload_logo()
        }
        if (document.getElementsByName('background_image')[0].files.length > 0) {
          this.upload_background()
        }
        //this.form.reset()
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>
