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
      <h1>Application Management </h1>
    </div>

    <div class="stats" v-if="stats">
    <div class="stat ">
        <div class="stat-number">{{ stats.total }}</div>
        <div class="stat-label">Total Application</div>
    </div>
    <div class="stat">
        <div class="stat-number">{{ stats.selected }}</div>
        <div class="stat-label">Selected</div>
    </div>
    <div class="stat  ">
        <div class="stat-number">{{ stats.shortlisted }}</div>
        <div class="stat-label">Shortlised</div>
    </div>
<div class="stat  ">
        <div style="color: red;" class="stat-number">{{stats.pending}}</div>
        <div class="stat-label">Pending</div>
    </div>
    <div class="stat  ">
        <div style="color: red;" class="stat-number">{{ stats.rejected }}</div>
        <div class="stat-label">Rejected</div>
    </div>
</div>
<div class="stats" v-else>Loading Data.....</div>

<div id="tableView">
    <table class="app-tab">
        <thead>
            <tr>

                <th>Student ID</th>
                <th>Student Name</th>
                <th>DriveId / Drive Name</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            
            <tr v-for="a in apple" :key="a.student_id">


                <td><strong>{{ a.student_id }}</strong></td>
                <td>
                    <div class="s-cell">

                        <div class="stud-deta">
                            <div class="stud-name">{{a.student_name}}</div>

                        </div>
                    </div>
                </td>

                <td>
                    <div class="d-info">
                        
                        <div class="drive-title-sm">{{ a.drive_id }}/{{ a.drive_name }}</div>

                    </div>
                </td>

                <td>

                    <span v-if="a.status == 'SELECTED'" class="status-badge status-selected">Selected</span>
                    <span v-else-if="a.status == 'REJECTED'" class="status-badge status-selected">Rejected</span>
                    <span v-else-if="a.status == 'PENDING'" class="status-badge status-selected">Pending</span>
                    <span v-else class="status-badge status-shortlisted">Blocked</span>

                    

                </td>
                <td>
                    <div class="t-a">
                        
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
import { adminAPI } from '@/services/api';
import { ref,onMounted } from 'vue';

const stats = ref({
total:0,pending:0,shortlisted:0,selected:0,rejected:0
})

const apple = ref([])
const fetchAApplication = async () => {
    try {
        const response = await adminAPI.getApplications();
        const serverData = response.data.data;
        stats.value = {
            total:serverData.total,
            selected:serverData.selected,
            rejected:serverData.rejected,
            pending:serverData.pending,
            shortlisted:serverData.shortlisted
        }
        apple.value = serverData.applications
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

onMounted(() =>{
    fetchAApplication()
})
</script>