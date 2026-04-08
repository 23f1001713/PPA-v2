<style scoped>
.main{
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
.main h1 {
            margin-top: 250px;
            text-align: center;
        }

        .content {
            text-align: center;
        }

        .content a {
            padding: 2px;
        }

        .content a button {
            padding: 8px 50px;
            border-radius: 8px;

        }
        .content a button:hover {
            background-color: chocolate;

        }

</style>

<template>
  <div class="main">
        <h1>Welcome To Placement Portal</h1>
    </div>
    <div class="content">
        <RouterLink to="/register">
            <Button>Register</Button>
        </RouterLink>
        <RouterLink to="/login"><button>
                Login
            </button></RouterLink>
    </div>
</template>

<script>
export default {
  name: 'LandingPage'
}
</script>