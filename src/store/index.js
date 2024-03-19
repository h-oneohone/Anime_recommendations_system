// store.js

import Vuex from 'vuex';
import axios from 'axios';

export default new Vuex.Store({
  state: {
    imageData: [], // Initialize as an empty array to store received data
  },
  mutations: {
    SET_IMAGE_DATA(state, data) {
      state.imageData = data;
    },
  },
  actions: {
    setImageData({ commit }, data) {
      commit('SET_IMAGE_DATA', data);
    },
    // Add a new action to fetch data from the API
    async fetchDataFromAPI({ commit }) {
      try {
        const response = await axios.get('http://localhost:8000/anime_series/'); // Replace with your actual API URL
        if (response.status === 200) {
          const data = response.data;
          commit('SET_IMAGE_DATA', data);
          // console.log('Data fetched from the API:', data);
          return data; // Return the data in case you need it in your component
        }
      } catch (error) {
        console.error('Error fetching data from the API:', error);
        return []; // Return an empty array in case of an error
      }
    },
  },
  getters: {
    imageData: (state) => state.imageData,
  },
});

// export default createStore({
//   state() {
//     return  {
//       count: 0,
//     }
//   },
//   getters: {
//   },
//   mutations: {
//   },
//   actions: {
//   },
//   modules: {
//   }
// })


