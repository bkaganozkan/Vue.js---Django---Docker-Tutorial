<template>
  <div class="col-md-12 mb-4 input-group">
    <input
      class="form-control"
      placeholder="Search..."
      @keyup="search($event.target.value)"
    />
    <div class="input-group-append">
      <select class="form-select" @change="sort($event.target.value)">
        <option value="">Select</option>
        <option value="asc">Price Ascending</option>
        <option value="desc">Price Descending</option>
      </select>
    </div>
  </div>
  <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
    <div class="col" v-for="product in products" :key="product.id">
      <div class="card shadow-sm">
        <img :src="product.image" alt="" height="200" />

        <div class="card-body">
          <p class="card-text">
            {{ product.title }}
          </p>
          <div class="d-flex justify-content-between align-items-center">
            <small class="text-muted">{{ product.price }} $</small>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="d-flex justify-content-center mt-4">
    <button class="btn btn-primary" @click="laodMore">Load More</button>
  </div>
</template>

<script lang="ts">
import { SetupContext } from "@vue/runtime-core";
export default {
  name: "Products",
  props: ["products", "filters"],
  emits: ["set-filters"],
  setup(props: any, context: SetupContext) {
    const search = (s: string) => {
      context.emit("set-filters", { ...props.filters, s, page: 1 });
    };

    const sort = (sort: string) => {
      context.emit("set-filters", {
        ...props.filters,
        sort,
        page: 1
      });
    };

    const laodMore = () => {
      context.emit("set-filters", {
        ...props.filters,
        page: props.filter.page + 1,
      });
    };

    return {
      search,
      sort,
      laodMore,
    };
  },
};
</script>

<style></style>
