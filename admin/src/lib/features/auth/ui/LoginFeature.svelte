<script>
    import YDInput from "@shared/ui/components/YDInput.svelte";
    import YDButton from "@shared/ui/components/YDButton.svelte";
    import {signIn} from "$lib/features/auth/model/signIn";
    import {goto} from "$app/navigation";

    let login = ''
    let password = ''
    let loginError = false

    const onSubmitLogin = () => {
        signIn(login, password)
            .then(() => {
                goto('/admin/')
            })
            .catch(() => {
                loginError = true
            })
    }
</script>

<div class="flex flex-col gap-1">
    <YDInput
            bind:value={login}
            placeholder="Логин"
            type="text"
    />
    <YDInput
            bind:value={password}
            placeholder="Пароль"
            type="password"
    />

    <YDButton class="mt-2" on:click={onSubmitLogin}>
        Войти
    </YDButton>
</div>
