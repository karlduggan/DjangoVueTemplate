import Vuex from 'vuex'

export default new Vuex.Store({
  state: {
    isLoggedIn: true
  },
  mutations: {
    setLoggedIn(state, isLoggedIn) {
      state.isLoggedIn = isLoggedIn
    }
  }
})