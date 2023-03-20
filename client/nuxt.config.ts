// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    components: true,
    css: [
        '~/assets/css/main.css'
    ],
    app: {
        head: {
            title: 'Твоё общежитие',
            link: [{ href: "https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;500&display=swap", rel: "stylesheet"}]
        }
    }
})
