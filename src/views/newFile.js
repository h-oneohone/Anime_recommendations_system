import { computed } from "vue";

// const filteredMaps = computed(() => {
//   if (className.value === "pa-0") {
//     return maps1.filter(map => {
//       return map.title.toLowerCase().includes(search.value.toLowerCase());
//     });
//   } else if (className.value === "pa-1") {
//     return maps2.filter(map => {
//       return map.title.toLowerCase().includes(search.value.toLowerCase());
//     });
//   }
//   return []; // Return an empty array if no class matches
// });
export default {
setup() {
const store = useStore(); // Get the Vuex store instance

const imageData = computed(() => {
return store.getters.imageData; // Replace 'imageData' with your actual getter name
});

return {
imageData,
};
},
};
