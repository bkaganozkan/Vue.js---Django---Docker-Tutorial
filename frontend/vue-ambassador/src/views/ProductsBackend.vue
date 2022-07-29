<template>
  <Products :products="products" :filters="filters" @set-filters="load" />
</template>

<script lang="ts">
import { onMounted, reactive, ref } from "vue";
import Products from "./Products.vue";
import { Product } from "@/models/products";
import { Filter } from "@/models/filters";
import axios from "axios";
export default {
  name: "ProductsBackend",
  components: { Products },

  setup() {
    const products = ref<Product[]>([]);
    const filters = reactive({
      s: "",
      sort: "",
      page: 1,
    });

    const load = async (f: Filter) => {
      filters.s = f.s;
      filters.sort = f.sort;
      filters.page = f.page;
      const arr = [];

      if (filters.s) {
        arr.push(`s=${filters.s}`);
      }
      if (filters.sort) {
        arr.push(`sort=${filters.sort}`);
      }
      if (filters.page) {
        arr.push(`page=${filters.page}`);
      }
      const { data } = await axios.get(`products/backend?${arr.join("&")}`);

      products.value =
        filters.page === 1 ? data.data : [...products.value, ...data.data];
    };

    onMounted(async () => load(filters));

    return {
      products,
      filters,
      load,
    };
  },
};
</script>

<style></style>
