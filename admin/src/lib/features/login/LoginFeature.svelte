<script>
    import YdInput from "$lib/shared/ui/components/YdInput.svelte";
</script>

<div class="flex flex-col gap-1">
    <YdInput placeholder="Логин" type="text"/>
    <YdInput placeholder="Пароль" type="password"/>

    <button class="rounded-lg bg-amber-500 text-white py-1.5 mt-2">
        Войти
    </button>
</div>
