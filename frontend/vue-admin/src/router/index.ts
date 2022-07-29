import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import Layout from "@/views/Layout.vue";
import Register from "@/views/Register.vue";
import Login from "@/views/Login.vue";
import Users from "@/views/Users.vue";
import Links from "@/views/Links.vue";
import Orders from "@/views/Orders.vue";
import Products from "@/views/products/Products.vue";
import ProductsForm from "@/views/products/ProductsForm.vue";
import Profile from '@/views/Profile.vue'

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  { path: "/login", component: Login },
  { path: "/register", component: Register },
  {
    path: "",
    component: Layout,
    children: [
      { path: "", redirect:'/users' },
      { path: "/users", component: Users },
      { path: "/users/:id/links", component: Links },
      { path: "/products", component: Products },
      { path: "/products/create", component: ProductsForm },
      { path: "/products/:id/edit", component: ProductsForm },
      { path: "/orders", component: Orders },
      { path: "/profile", component: Profile },
    ],
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
