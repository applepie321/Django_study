<script>
    import { push } from 'svelte-spa-router'
    import fastapi from '../lib/api'
    import Error from '../components/Error.svelte'

    let error = {detail:[]}
    let login_username = ""
    let login_password = ""

    function login(event) {
        event.preventDefault()
        let url = "/api/user/login"
        let params = {
            username: login_username,
            password: login_password,
        }
        fastapi('post', url, params,
            (json) => {
                push("/")
            },
            (json_error) => {
                error = json_error  
            }
        )
    }
</script>