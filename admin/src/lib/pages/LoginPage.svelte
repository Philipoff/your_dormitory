<script lang="ts">
    import {goto} from "$app/navigation";
    import LoginPanel from "$lib/widgets/LoginPanel.svelte";
    import {getAuthToken} from "../features/auth";
    import {Routes} from "../../routes/routes";

    if (getAuthToken()) {
        goto(Routes.HOME_PAGE)
    }
</script>

<div class="h-[100vh] w-[100vw] flex justify-center items-center">
    <LoginPanel/>
</div>
