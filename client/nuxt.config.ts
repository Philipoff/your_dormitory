// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    components: true,
    css: [
        '~/assets/css/main.css'
    ],
    app: {
        head: {
            title: 'Твоё общежитие',
            link: [
                { href: "https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css", rel: "stylesheet", integrity: "sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x", crossorigin: "anonymous"},
                { href: "https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;500&display=swap", rel: "stylesheet"}
            ],
            script: [
                { src: "https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js", integrity: "sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4", crossorigin: "anonymous"}
            ]
        }
    },
    runtimeConfig: {
        public: {
            /*baseURL: 'https://yourstudent.ru'*/
            baseURL: "http://localhost:3000"
        }
    }
})
