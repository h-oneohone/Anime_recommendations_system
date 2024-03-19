<template>
  <v-footer>
    <v-card elevation="0" rounded="0" width="100%" class="text-center" color="#FAFAFA">
        <v-card-text>
            @ {{ new Date().getFullYear()}} - <strong>From IEC PTIT </strong>
        </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {

}
</script>

<style>
.v-footer {
    padding: 8px 0;
}
</style>