<script>
    import {fade} from 'svelte/transition'
    import {goto} from "$app/navigation";
    import 'reflect-metadata'
    import '$lib/app/index.css';
    import {checkAuth} from "$lib/features/auth/index";

    let checkingAuth = true;

    checkAuth().then(async (res) => {
        if (!res) {
            await goto('/admin/login')
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
