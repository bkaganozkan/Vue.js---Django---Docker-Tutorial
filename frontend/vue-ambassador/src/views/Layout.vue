<template>
  <Nav />
  <main>
    <Header v-if="showHeader" />

    <div class="album py-5 bg-light">
      <div class="container">
        <router-view />
      </div>
    </div>
  </main>
</template>

<script>
import Header from "@/components/Header.vue";
import Nav from "@/components/Nav.vue";
import ProductsFrontend from "@/views/ProductsFronted.vue";
import { computed, onMounted } from "@vue/runtime-core";
import { useStore } from "vuex";
import axios from "axios";
import { useRoute } from "vue-router";
export default {
  name: "Layout",
  components: { Nav, Header, ProductsFrontend },
  setup() {
    const store = useStore();
    const route = useRoute();
    const showHeader = computed(
      () => route.path === "/" || route.path === "/backend"
    );

    onMounted(async () => {
      try {
        const { data } = await axios.get("user");
        await store.dispatch("setUser", data);
      } catch (e) {
        await store.dispatch("setUser", null);
      }
    });

    return {
      showHeader,
    };
  },
};
</script>

<style></style>
