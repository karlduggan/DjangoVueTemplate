// index.js
import { createStore } from 'vuex';
import state from './state';
import getters from './getters';
import mutations from './mutations';
import actions from './actions';
import user from './modules/user';

export default createStore({
  state,
  getters,
  mutations,
  actions,
  modules: {
    user,
  },
});
