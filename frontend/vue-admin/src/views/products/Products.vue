<template>
  <div>
    <div class="pt-3 pb-2 mb-3 border-bottom">
      <v-btn href="/products/create" variant="contained" color="primary">
        Add
      </v-btn>
    </div>
    <v-simple-table>
      <template v-slot:default>
        <thead>
          <tr>
            <th>#</th>
            <th>Image</th>
            <th>Title</th>
            <th>Description</th>
            <th>Price</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="product in products.slice(
              (page - 1) * perPage,
              page * perPage
            )"
            :key="product.id"
          >
            <td>{{ product.id }}</td>
            <td>
              <v-img max-height="80" max-width="120" :src="product.image" />
            </td>
            <td>{{ product.title }}</td>
            <td>{{ product.description }}</td>

            <td>{{ product.price }}$</td>
            <td>
              <v-btn-toggle>
                <v-btn
                  color="primary"
                  :href="`/products/${product.id}/edit`"
                  small
                  elevation="2"
                  >Edit</v-btn
                >
                <v-btn
                  color="error"
                  @click="del(product.id)"
                  small
                  elevation="2"
                  >Delete</v-btn
                >
              </v-btn-toggle>
            </td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
    <div class="text-center">
      <v-pagination
        v-model="page"
        total-visible="7"
        :length="lastPage"
      ></v-pagination>
    </div>
  </div>
</template>

<script lang="ts">
import axios from "axios";

export default {
  name: "Products",
  data() {
    return {
      products: [],
      page: 1,
      perPage: 10,
      lastPage: 0,
    };
  },
  async mounted() {
    const { data } = await axios.get("products");
    this.products = data;
    this.lastPage = Math.ceil(data.length / this.perPage);
  },
  methods: {
    async del(id: number) {
      if (confirm("Are you sure_?")) {
        await axios.delete(`products/${id}`);

        this.products = this.products.filter((p) => p.id !== id);
      }
    },
  },
};
</script>

<style></style>
