

<template>
  <div class="sidebar">
    <div class="sidebar-logo">
    <h1>Placement Portal</h1>
  </div>
  
      <ul class="sidebar-list">
        <li><RouterLink to="/admin/dashboard">Dashboard</RouterLink></li>
        <li><RouterLink to="/admin/students">Student</RouterLink></li>
        <li><RouterLink to="/admin/companies">Company</RouterLink></li>
        <li><RouterLink to="/admin/drives">Drives</RouterLink></li>
        <li><RouterLink to="/admin/applications">Application</RouterLink></li>

        <li class="logout"><button @click="handleLogout">Logout</button></li>
      </ul>
    

  </div>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
  name: 'Sidebar',
  setup(){
    const router = useRouter()

    const handleLogout = () =>{
        localStorage.removeItem('user_token')
        localStorage.removeItem('user_role')

        router.push({path:'/login' , 
            query: {message:'You are Logged Out sucessfully !.'}
        })
    }
    return {handleLogout}
  }
}
</script>

<style scoped>
        .sidebar {
            position: fixed;
            top: 0;
            left: 0;
            height: 100vh;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            width: 260px;
            background-color: rgb(6, 6, 135);
            padding: 20px 0;
            z-index: 1000;
            box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
        }
.sidebar-logo {
            padding: 0 20px 30px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 20px;
        }

        .sidebar-logo h1 {
            color: white;
            font-size: 1.4rem;
            font-weight: 600;
        }

        .sidebar-list {
            list-style: none;
            padding: 0;
        }

        .sidebar-list li {
            margin-bottom: 5px;
        }

        .sidebar-list a {
            display: flex;
            align-items: center;
            padding: 12px 20px;
            color: rgba(255, 255, 255, 0.8);
            text-decoration: none;
            transition: all 0.3s ease;
        }

.sidebar-list a:hover {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        border-left: 4px solid #4facfe;
    }
button{
    margin-left: 15px;
    margin-top: 30px;

    background-color: rgb(6, 6, 135);
    border: none;
    color: white;
    font-size: 14px;}

</style>