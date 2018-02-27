import axios from 'axios'
import * as types from '../mutation-types'

// state
export const state = {
  brand: null,
  brands: null
}

// mutations
export const mutations = {
  [types.FETCH_BRAND_SUCCESS](state, {
    brand
  }) {
    state.brand = brand
  },

  [types.FETCH_BRAND_FAILURE](state) {
  },

  [types.UPDATE_BRAND](state, {
    brand
  }) {
    state.brand = brand
  }
}

// actions
export const actions = {

  async fetchBrand({
    commit
  }) {
    try {
      const {
        data
      } = await axios.get('/api/brand')

      commit(types.FETCH_BRAND_SUCCESS, {
        brand: data
      })
    } catch (e) {
      commit(types.FETCH_BRAND_FAILURE)
    }
  },

  async updateBrand({
    commit
  }, payload) {
    commit(types.UPDATE_BRAND, payload)
  },
}

// getters
export const getters = {
  brand: state => state.brand,
}
