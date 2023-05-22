// modules/user.js
export default {
    state: {
      // User module state properties
      name: '',
      email: '',
    },
    getters: {
      // User module getters
      getName: (state) => state.name,
      getEmail: (state) => state.email,
    },
    mutations: {
      // User module mutations
      setName: (state, name) => {
        state.name = name;
      },
      setEmail: (state, email) => {
        state.email = email;
      },
    },
    actions: {
      // User module actions
      updateUser: ({ commit }, user) => {
        // Perform update user logic
        commit('setName', user.name);
        commit('setEmail', user.email);
      },
    },
  };
  