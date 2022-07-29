<template>
  <v-app>
    <Nav />
    <div class="container-fluid">
      <div class="row">
        <Menu />

        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
          <div class="table-responsive">
            <router-view />
          </div>
        </main>
      </div>
    </div>
  </v-app>
</template>

<script>
import Vue from "vue";
import Nav from "@/components/Nav.vue";
import Menu from "@/components/Menu.vue";
import axios from "axios";
import { User } from "@/models/user";
export default {
  name: "Layout",
  components: { Nav, Menu },
  data() {
    return {
      user: new User(),
    };
  },
  async mounted() {
    try {
      const { data } = await axios.get("user");
      await this.$store.dispatch('setUser', data)
    } catch (error) {
      console.log(error);
      await this.$router.push("/login");
    }
  },
};
</script>
