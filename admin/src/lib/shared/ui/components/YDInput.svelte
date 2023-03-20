<script lang="ts">
    export let value = ''
    export let invalid = false
</script>

<input bind:value={value} class={$$props.class + ' yd-input'} class:invalid {...$$restProps}>

<style lang="postcss">
    .yd-input {
        @apply rounded-md border border-zinc-300 transition-all duration-300 py-1 px-2 outline-white focus:outline-amber-500;
    }

    .yd-input.invalid {
        @apply border-red-400 outline-red-400;
    }
</style>
