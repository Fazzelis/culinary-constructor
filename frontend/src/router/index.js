import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "constructor",
            component: () => import("@/pages/Constructor.vue"),
            meta: { requiresAuth: false },
        },
        {
            path: "/catalog",
            name: "catalog",
            component: () => import("@/pages/Catalog.vue"),
            meta: { requiresAuth: false },
        },
        {
            path: "/dish/:id",
            name: "dish",
            component: () => import("@/pages/dish/[id].vue"),
            meta: { requiresAuth: false },
        },
        {
            path: "/404",
            name: "404",
            component: () => import("@/pages/NotFound.vue"),
            meta: { requiresAuth: false },
        },
    ]
});

export default router;