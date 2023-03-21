<script>
    import 'reflect-metadata'
    import {goto} from "$app/navigation";
    import {fade} from 'svelte/transition'
    import '$lib/app/index.css';
    import {checkAuth} from "$lib/features/auth/index";
    import {Routes} from "./routes";

    let checkingAuth = true;

    checkAuth().then(async (res) => {
        if (!res) {
            await goto(Routes.LOGIN_PAGE)
        }
        checkingAuth = false;
    })
</script>

<div class="app">
    {#if (!checkingAuth)}
        <main transition:fade>
            <slot/>
        </main>
    {/if}
</div>

<style>
    body, .app {
        background: #f1f1f1;
    }
</style>
