<style scoped>
.nav {
            background-color: #8100D1;
            color: white;
            padding: 15px;
            
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 0;
            z-index: 1000;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        }

        .navbar {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .nav-logo {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 1.4rem;
            font-weight: 700;
            color: white;
            text-decoration: none;
        }

        .nav-logo i {
            font-size: 1.8rem;
        }

        .nav-list {
            display: flex;
            align-items: center;
            gap: 30px;
            list-style: none;
            margin: 0;
        }

        .nav-list a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s ease;
            padding: 8px 16px;
            border-radius: 20px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

</style>

<template>
  <nav class="nav">
        <div class="navbar">
            <a href="#" class="nav-logo">
                <i class="bi bi-mortarboard-fill"></i>
                Placement Portal -Company
            </a>


            



            <ul class="nav-list" id="navbarMenu">
                <li><RouterLink to="/company/dashboard" class="s"> Dashboard</RouterLink></li>
                <li><RouterLink to="/company/drives" class="s_d"> Drives</RouterLink></li>
                <li><RouterLink to="/company/applications" class="s_a">
                        Applications</RouterLink></li>
                <li><RouterLink to="/company/drives/create" class="s_a">
                        Create Drive</RouterLink></li>
                <li><RouterLink to="/company/profile" class="s_p"> Profile</RouterLink>
                </li>
                <li><RouterLink to="/" class="s_p"> Logout</RouterLink>
                </li>
            </ul>
        </div>
    </nav>

</template>
<script>
export default {
  name: 'Modal'
}
</script>