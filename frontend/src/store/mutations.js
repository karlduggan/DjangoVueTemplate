// mutations.js
export default {
    // Mutation definitions
    setUser: (state, user) => {
      state.user = user;
    },
    setLoggedIn: (state, isLoggedIn) => {
      state.isLoggedIn = isLoggedIn;
    },
  };
  