<template>
  <Products
    :products="filteredProducts"
    :filters="filters"
    @set-filters="filtersChanged"
  />
</template>

<script lang="ts">
import { onMounted, reactive, ref } from "vue";
import Products from "./Products.vue";
import { Product } from "@/models/products";
import axios from "axios";
import { Filter } from "@/models/filters";
export default {
  name: "ProductsFrontend",
  components: { Products },
  props: ["product", "filters"],
  emits: ["set-filters"],

  setup() {
    const allProducts = ref<Product[]>([]);
    const filteredProducts = ref<Product[]>([]);
    const filters = reactive({
      s: "",
      sort: "",
      page: 1,
    });

    onMounted(async () => {
      const { data } = await axios.get("products/frontend");

      allProducts.value = data;
      filteredProducts.value = data;
    });

    const filtersChanged = (f: Filter) => {
      filters.s = f.s;
      filters.sort = f.sort;
      filters.page = f.page;
      let products = allProducts.value.filter(
        (p) =>
          p.title.toLowerCase().indexOf(filters.s.toLowerCase()) >= 0 ||
          p.description.toLowerCase().indexOf(filters.s.toLowerCase()) >= 0
      );

      if (filters.sort === "asc" || filters.sort === "desc") {
        products.sort((a, b) => {
          const diff = a.price - b.price;

          if (diff === 0) return 0;

          const sign = Math.abs(diff) / diff;
          return filters.sort === "asc" ? sign : -sign;
        });
      }

      filteredProducts.value = products;
    };

    const loadMore = () => {
      context.emit("set-filter", {
        ...props.filter,
        page: props.filters.page + 1,
      });
    };

    return {
      filteredProducts,
      filters,
      filtersChanged,
    };
  },
};
</script>

<style></style>
