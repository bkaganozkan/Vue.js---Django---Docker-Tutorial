<template>
  <h3 class="mt-4">Account Information</h3>
  <form @submit.prevent="infoSubmit">
    <div class="mb-3">
      <label for="">First Name</label>
      <input
        v-model="infoData.first_name"
        class="form-control"
        name="first_name"
      />
    </div>
    <div class="mb-3">
      <label for="">Last Name</label>
      <input
        v-model="infoData.last_name"
        class="form-control"
        name="first_name"
      />
    </div>
    <div class="mb-3">
      <label for="">Email</label>
      <input v-model="infoData.email" class="form-control" name="first_name" />
    </div>
    <button class="btn btn-outline-secondary" type="submit">Save</button>
  </form>

  <h3 class="mt-4">Change Password</h3>
  <form @submit.prevent="passwordSubmit">
    <div class="mb-3">
      <label for="">Password</label>
      <input
        v-model="passwordData.password"
        class="form-control"
        name="first_name"
      />
    </div>
    <div class="mb-3">
      <label for="">Confirm Password</label>
      <input
        v-model="passwordData.password_confirm"
        class="form-control"
        name="first_name"
      />
    </div>
    <button class="btn btn-outline-secondary" type="submit">Save</button>
  </form>
</template>

<script>
import axios from "axios";
import { reactive } from "@vue/reactivity";
import { useStore } from "vuex";
import { computed, watch } from "@vue/runtime-core";
export default {
  name: "Profile",
  setup() {
    const infoData = reactive({
      first_name: "",
      last_name: "",
      email: "",
    });

    const passwordData = reactive({
      password: "",
      password_confirm: "",
    });

    const store = useStore();
    const user = computed(() => store.state.user);

    watch(user, () => {
      infoData.first_name = user.value.first_name;
      infoData.last_name = user.value.last_name;
      infoData.email = user.value.email;
    });

    const infoSubmit = async () => {
      const { data } = await axios.put("users/info", infoData);
      await store.dispatch("setUser", data);
    };
    const passwordSubmit = async () => {
      await axios.put("users/password", passwordData);
    };

    return {
      infoData,
      passwordData,
      infoSubmit,
      passwordSubmit,
    };
  },
};
</script>

<style></style>
