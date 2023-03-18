<script lang="ts">
    import {createEventDispatcher} from "svelte";

    export let variant: 'orange' | 'green' = 'orange'

    $: buttonClass = `yd-button ${$$props.class} variant-${variant}`

    const dispatch = createEventDispatcher()
</script>

<button class={buttonClass} on:click={(p) => dispatch('click', p)}>
    <slot></slot>
</button>

<style lang="postcss">
    .yd-button {
        @apply rounded-lg py-1.5;
    }

    .variant-orange {
        @apply bg-amber-500 text-white;
    }

    .variant-green {
        @apply bg-green-600 text-white;
    }
</style>
