<style scoped>

.main-container{
  margin-left: 300px;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
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

        .nav{
          padding: 10px 30px;
          margin-top: 30px;
          border: 1px solid black;
          border-radius: 15px;
        }
      
        input{
          padding: 10px 30px;
          margin-right: 10px;
          border-radius: 15px;
        }
        
        .app-tab {
            width: 100%;
            border-collapse: collapse;
        }

        .app-tab thead {
            background: #f8f9fa;
        }

        .app-tab th {
            padding: 15px 20px;
            text-align: left;
            font-size: 0.85rem;
            font-weight: 600;
            color: #555;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border-bottom: 2px solid #e9ecef;
        }

        .app-tab tbody tr {
            border-bottom: 1px solid #f0f0f0;
            transition: all 0.3s ease;
        }

        .app-tab tbody tr:hover {
            background: #f8f9fa;
        }

        .app-tab td {
            padding: 18px 20px;
            font-size: 0.9rem;
            color: #2d3436;
        }
</style>

<template>
  <div class="main-container">
    <div class="header">
      <h1>Company Management </h1>
    </div>
    <div class="nav">
    <form >
        <div class="search">
            <input type="text" placeholder="Search companies..." name="search">
        
        <input style="background-color: blue; color: white;" class="btn btn-outline-success" type="submit" value="Search">
        </div>
    </form>

</div>
<div class="stats" v-if="stats">
    <div class="stat hov">
        <div class="stat-number">{{ stats.t_c }}</div>
        <div class="stat-label">Total Companies</div>
    </div>
    <div class="stat applied hov">
        <div class="stat-number">{{ stats.t_d }}</div>
        <div class="stat-label">Total Drives</div>
    </div>
    <div class="stat shortlisted hovr">
        <div class="stat-number">{{ stats.t_b }}</div>
        <div class="stat-label">Total Bloacked</div>
    </div>

</div>
<div class="stats" v-else> Loading Data .....</div>
<div id="tableView">
    <table class="app-tab">
        <thead>
            <tr>

                <th>Company ID</th>
                <th>Company Name</th>
                <th>Total Drives</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            
            <tr v-for="com in comlist" :key="com.id">
                <td><strong>{{ com.id }}</strong></td>
                <td>
                    <div class="s-cell">

                        <div class="stud-deta">
                            <div class="stud-name">{{com.name}}</div>

                        </div>
                    </div>
                </td>

                <td>
                    <div class="d-info">
                        
                        <div class="drive-title-sm">{{ com.drive_count }}</div>

                    </div>
                </td>

                <td>

                    <span v-if="com.status == 'APPROVED'" class="status-badge status-selected">Approved</span>

                    
                    <span v-else class="status-badge status-shortlisted">Blocked</span>

                    

                </td>
                <td>
                    <div class="t-a">
                        <a href="#">
                            
                            <button v-if="com.status != 'APPROVED'" @click="handleToggleStatus(com)" style="background-color: #28a745; color: white;" class="btn-sm btn-view">
                                <i class="bi bi-unlock"></i> Unblock
                            </button>
                           
                            <button v-else @click="handleToggleStatus(com)" style="background-color: #dc3545; color: white;" class="btn-sm btn-view">
                                <i class="bi bi-slash-circle"></i> Block
                            </button>
                          
                        </a>
                        <a href="#">
                            <button class="btn-sm btn-view">
                                <i class="bi bi-eye"></i> View Details
                            </button>
                        </a>
                        <a href="#">
                            <button class="btn-sm btn-view">
                                <i class="bi bi-eye"></i> View History
                            </button>
                        </a>

                    </div>
                </td>

            </tr>
            
        </tbody>
    </table>
</div>
  </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import { adminAPI } from '@/services/api';

const stats = ref({
    t_c:0,t_d:0,t_b:0
})

const comlist = ref([])

const fetchACompany = async () => {
    try {
        const response = await adminAPI.getCompanies();
        
        // Success: Handle your statistics data
        const serverData = response.data.data;
        stats.value = {
            t_c : serverData.t_c,
            t_d: serverData.t_d,
            t_b:serverData.t_b
        }

        comlist.value = serverData.companies
        console.log(comlist)
        console.log("Dashboard Stats:", serverData);
        
        
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

const handleToggleStatus = async (com) => {
    const action = com.status === 'APPROVED' ? 'block' : 'unblock';
    
    // Confirm with user
    if (!confirm(`Are you sure you want to ${action} this Company?`)) return;

    try {
        const response = await adminAPI.blacklistCompany(com.id);
        fetchACompany();
        console.log(response.data)
    } catch (error) {
        console.error("Failed to change status:", error);
        alert("Error updating status");
    }
};

onMounted(() =>{
    fetchACompany();
})
</script>