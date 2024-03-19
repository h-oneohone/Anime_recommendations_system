// eslint-disable-next-line
/* eslint-disable */
<template>
  <v-app>
    <NavBar @filter-by-class="updateFilteredMaps" @filter-maps="handleEmitSearch" />
    <v-container fluid>
      <v-card color="#F7F7F7" tile flat class="d-flex align-center justify-center mt-12" dark></v-card>
      <v-toolbar color="transparent" dark class="mt-3"></v-toolbar>
      <v-row>
        <!-- Loop through filteredMaps and add a click event handler -->
        <v-col cols="12" sm="3" v-for="(map, index) in filteredMaps" :key="'map-' + index">
          <v-card @click="openMap(map)" height="300" align="center" flat outlined tile>
            <v-img
              :src="decodeImage(map.image)"
              alt="Decoded Image"
              width="200"
              height="200"
              contain
            ></v-img>
            <v-card-text class="mt-n1">
              <strong>{{ map.title }}</strong>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <!-- Display enlarged image in a modal dialog -->
      <v-dialog v-model="showEnlargedMap" max-width="80%">
        <v-card>
          <v-toolbar color="transparent">
            <v-spacer></v-spacer>
            <v-card-actions>
              <v-btn @click="closeMap">Close</v-btn>
            </v-card-actions>
          </v-toolbar>
          <!-- Center the image using Flexbox -->
          <div class="center-image">
            <v-img :src="selectedMap ? decodeImage(selectedMap.image) : ''" alt="Enlarged Image"></v-img>
          </div>
        </v-card>
      </v-dialog>
    </v-container>
    <FooterView />
  </v-app>
</template>

<script setup>
// import { defineComponent } from 'vue';

// Components
import NavBar from "@/components/NavBar.vue";
import FooterView from "@/components/FooterView.vue";
import { ref, computed, provide, onMounted } from "vue";
import { mapGetters } from "vuex";
import { useStore } from "vuex";
mapGetters;
provide("demo", 12);

const selectedMap = ref(null); // Variable to track the selected map
const showEnlargedMap = ref(false); // Variable to control the modal dialog

// Function to open the selected map in the modal dialog
const openMap = map => {
  selectedMap.value = map;
  showEnlargedMap.value = true;
};

// Function to close the modal dialog
const closeMap = () => {
  selectedMap.value = null;
  showEnlargedMap.value = false;
};

const store = useStore();

// Khi component được khởi tạo, chúng ta có thể gọi action để lấy dữ liệu từ API
onMounted(async () => {
  await store.dispatch("fetchDataFromAPI");
});

// Tạo một computed property để kết nối maps với imageData trong store
const maps = computed(() => store.getters.imageData);

const search = ref("");

const decodeImage = base64Data => {
  // Decode base64 image data and return it as a data URI
  return `data:image/jpeg;base64,${base64Data}`;
};

const filteredMaps = computed(() => {
  return maps.value.filter(item =>
    item.title.toLowerCase().includes(search.value.toLowerCase())
  ); // Filter by title containing the search value
});

console.log(filteredMaps);

const handleEmitSearch = value => {
  search.value = value;
};
</script>
<style scoped>
.v-container {
  width: 100%;
  padding: 16px 0px !important;
  margin-right: auto;
  margin-left: auto;
}
.v-card.borderme {
  border: 2px solid black !important;
}
.v-card.borderout {
  border: 1px solid #d5f0db !important;
}
.center-image {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%; /* Ensure the container takes the full height of the card */
}
</style>