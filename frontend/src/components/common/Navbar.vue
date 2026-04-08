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
        button{
            background-color: #8100D1;
        }

</style>

<template>
  <nav class="nav">
        <div class="navbar">
            <a href="#" class="nav-logo">
                <i class="bi bi-mortarboard-fill"></i>
                Placement Portal
            </a>



            <ul class="nav-list" id="navbarMenu">
                <li><RouterLink to="/student/dashboard" class="s"><i class="bi bi-house-door"></i> Dashboard</RouterLink></li>
                <li><RouterLink to="/student/drives" class="s_d"><i class="bi bi-briefcase"></i> Drives</RouterLink></li>
                <li><RouterLink to="/student/applications" class="s_a"><i class="bi bi-file-earmark-text"></i> My
                        Applications</RouterLink></li>
                <li><RouterLink to="/student/history" class="s_a"><i class="bi bi-file-earmark-text"></i> My
                        History</RouterLink></li>
                <li><RouterLink to="/student/profile" class="s_p"><i class="bi bi-person"></i> Profile</RouterLink>
                </li>
                <li><RouterLink  class="s_p"><i class="bi bi-box-arrow-right"></i> <button @click="handleLogout">Logout</button></RouterLink>
                </li>
            </ul>
        </div>
    </nav>

</template>

<script>
import { useRouter } from 'vue-router';
export default {
  name: 'Navbar'
}



const router = useRouter();

const handleLogout = () => {
  // 1. Remove all stored user data
  localStorage.removeItem('user_token');
  localStorage.removeItem('user_role');

//   2. Optional: If using a state manager like Pinia/Vuex, reset it here
  authStore.logout();

  // 3. Redirect to login page
  router.push('/login');
};
</script>

<!-- /* <template>
  <button @click="handleLogout" class="logout-btn">
    Logout
  </button>
</template>
</script> */ -->