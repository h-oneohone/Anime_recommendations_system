<template>
  <v-app-bar app dark flat>
    <v-btn id="menu-activator" color="primary">
      <v-icon left class="mr-2">fas fa-bars</v-icon>
    </v-btn>
    <v-menu activator="#menu-activator">
      <v-list>
        <v-list-item v-for="(item, index) in items" :key="index" :value="index">
          <v-list-item-title @click="handleMenuItemClick(item)">{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

    <v-toolbar-title>Animes</v-toolbar-title>
    <div
      style="position: absolute;margin-left:auto;margin-right:auto;left:0;right:0;text-align: center;"
    >
      <!-- <h4>Hung dep trai</h4> -->
    </div>
    <v-spacer></v-spacer>

    <v-col cols="4">
      <v-row>
        <v-text-field
          v-model="searchKeyword"
          density="compact"
          variant="outlined"
          label="Search"
          append-inner-icon="fas fa-search"
          single-line
          hide-details
          class="mr-2"
          @input="filterMaps"
        ></v-text-field>
      </v-row>
    </v-col>

    <v-toolbar color="transparent">
      <v-spacer></v-spacer>

      <v-btn
        v-if="className === 'all'"
        class="text-black"
        variant="text"
        color
        @click="filterByClass0('all')"
      >Anime</v-btn>
      <v-btn
        v-else
        class="text-grey"
        variant="text"
        color="grey"
        @click="filterByClass0('all')"
      >Anime</v-btn>

      <v-btn
        v-if="className === 'map'"
        class="text-black"
        variant="text"
        color
        @click="filterByClass0('map')"
      >About</v-btn>
      <v-btn
        v-else
        class="text-grey"
        variant="text"
        color="grey"
        @click="filterByClass0('map')"
      >About</v-btn>

      <v-btn
        v-if="className === 'abnormal'"
        class="text-black"
        variant="text"
        color
        @click="filterByClass1('abnormal')"
      >Contact</v-btn>
      <v-btn
        v-else
        class="text-grey"
        variant="text"
        color="grey"
        @click="filterByClass1('abnormal')"
      >Contact</v-btn>
    </v-toolbar>

    <v-btn>
      <v-icon left class="mr-2">fas fa-user</v-icon>
    </v-btn>
  </v-app-bar>
</template>

<script>
import { inject } from "vue";
export default {
  setup: function() {
    const demo = inject("demo");
    console.log(demo);
    return;
  },
  data() {
    return {
      className: "all",
      searchKeyword: "",
      items: [{ title: "tap1" }, { title: "tap2" }]
    };
  },
  methods: {
    filterByClass0(className) {
      this.className = className;
      this.$emit("filter-by-class", className);
    },
    filterByClass1(className) {
      this.className = className;
      this.$emit("filter-by-class", className);
    },
    handleMenuItemClick(item) {
      if (item.title === "input list website") {
        this.$router.push("/input_list_web");
      } else if (item.title === "history") {
        this.$router.push("/history");
      }
    },
    filterMaps() {
      this.$emit("filter-maps", this.searchKeyword);
    }
  }
};
</script>

<style>
.text-black {
  color: black !important;
}

.text-grey {
  color: grey !important;
}
</style>