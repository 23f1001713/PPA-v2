<style scoped>
.main-container{
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  margin-left: 300px;
}

.header{
  border: 2px solid black;
  width: 1150px;
  background-color: white;
  border-radius: 15px;
  padding-left:40px ;
  margin-top: 30px;
   box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
}

.stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
            margin-top: 40px;
        }

        .stat {
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-top: 4px solid blue;
        }

        .stat:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
            border: 2px solid blue;
        }

      
        .stat-number {
            font-size: 2.5rem;
            font-weight: 700;
            color: blue;
            margin-bottom: 8px;
        }

        .stat-label {
            font-size: 0.9rem;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-weight: 500;
        }



</style>

<template>
  <div class="main-container">
    <div class="header">
      <h1>Admin Dashboard</h1>
    </div>

    <div class="stats" v-if="stats">
    <div class="stat hov">
        <div class="stat-number" data-stat = 't_a'>{{ stats.t_a }}</div>
        <div class="stat-label">Total Applications</div>
    </div>
    <div class="stat hov applied">
        <div class="stat-number">{{ stats.t_s }}</div>
        <div class="stat-label">Total Student</div>
    </div>
    <div class="stat hov shortlisted">
        <div class="stat-number">{{ stats.t_c }}</div>
        <div class="stat-label">Total Companies</div>
    </div>
    <div class="stat hovr selected">
        <div class="stat-number">{{ stats.t_d }}</div>
        <div class="stat-label"> Total Drives</div>
    </div>
    <div class="stat hovr rejected">
        <div style="color: red;" class="stat-number">{{ stats.p_d }}</div>
        <div class="stat-label">Pending Drives</div>
    </div>
    <div class="stat hovr rejected">
        <div style="color: red;" class="stat-number">{{ stats.p_c }}</div>
        <div class="stat-label">Pending Companies</div>
    </div>
    <div class="stat hovr rejected">
        <div style="color: red;" class="stat-number">{{ stats.b_s }}</div>
        <div class="stat-label">Blocked Students</div>
    </div>

</div>
<div class="stats" v-else> <h1>Loading Data .....</h1></div>
  </div>
</template>


<script setup>
import { onMounted,ref } from 'vue';
import { adminAPI } from '@/services/api';

const stats = ref({
    t_s: 0, t_c: 0, t_a: 0, t_d: 0, p_c: 0, p_d: 0, b_s: 0
});

const fetchAdminDashboard = async () => {
    try {
        const response = await adminAPI.getDashboard();
        
        stats.value = response.data.data.statistics;
        console.log("Dashboard Stats:", stats);
        
        
    } catch (error) {
        if (error.response) {
            // Handle specific status codes
            if (error.response.status === 401) {
                console.error("Session expired. Please login again.");
                // Redirect to login page
            } else if (error.response.status === 403) {
                console.error("Access Denied: You are not an Admin.");
            } else {
                console.error("Server Error:", error.response.data.message);
            }
        } else {
            console.error("Network Error:", error.message);
        }
    }
};

onMounted(() =>{
    fetchAdminDashboard();
})
</script>


