// actions.js
export default {
    // Action definitions
    login: ({ commit }, user) => {
      // Perform login logic
      commit('setUser', user);
      commit('setLoggedIn', true);
    },
    logout: ({ commit }) => {
      // Perform logout logic
      commit('setUser', null);
      commit('setLoggedIn', false);
    },
  };
  