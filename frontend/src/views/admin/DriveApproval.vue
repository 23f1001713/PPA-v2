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

        .drives-container {
            display: grid;
            gap: 20px;
        }

        .drive-card {
            background: white;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
            border-left: 5px solid blue;
            position: relative;
        }

        .drive-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
        }



        .drive-header {
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 1px solid #f0f0f0;
        }

        .drive-title-section {
            flex: 1;
        }



        .drive-title {
            font-size: 1.4rem;
            font-weight: 600;
            color: #2d3436;
            margin-bottom: 8px;
        }

        .company-name {
            color: #667eea;
            font-weight: 500;
            font-size: 1rem;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .status-badges {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }

        .badge {
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .status-rejected {
            background: #ffebee;
            color: #c62828;
        }

        .badge-pending {
            background: #ffeaa7;
            color: #d63031;
        }

        .badge-approved {
            background: #55efc4;
            color: #00b894;
        }

        .badge-rejected {
            background: #ff7675;
            color: #d63031;
        }

        .badge-closed {
            background: #a29bfe;
            color: #6c5ce7;
        }
        .action-buttons {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 20px;
        }

        .btn-action {
            padding: 8px 18px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 500;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .btn-view {
            background: blue;
            color: white;
        }

        .btn-view:hover {
            background: blue;
            transform: scale(1.05);
        }

        .btn-approve {
            background: #00b894;
            color: white;
        }

        .btn-approve:hover {
            background: #00a383;
        }

        .btn-reject {
            background: #d63031;
            color: white;
        }

        .btn-reject:hover {
            background: #c0281f;
        }

        .btn-close {
            background: #fdcb6e;
            color: #2d3436;
        }

        .btn-close:hover {
            background: #ffc048;
        }

        


        </style>

<template>
  <div class="main-container">
    <div class="header">
      <h1>Drives Management </h1>
    </div>

    <div class="stats" v-if="stats">
    <div class="stat ">
        <div class="stat-number">{{ stats.total }}</div>
        <div class="stat-label">Total Drives</div>
    </div>
    <div class="stat">
        <div class="stat-number">{{ stats.t_a }}</div>
        <div class="stat-label">Total Approved</div>
    </div>
    <div class="stat  ">
        <div class="stat-number">{{ stats.t_p }}</div>
        <div class="stat-label">Pending</div>
    </div>
<div class="stat  ">
        <div style="color: red;" class="stat-number">{{ stats.t_c }}</div>
        <div class="stat-label">Closed</div>
    </div>
</div>
<div class="stats" v-else>Loading Data ....</div>

<div class="drives-container">
   
    <div v-for="drive in drives" :key="drive.id" class="drive-card pending">
        <div class="drive-header">
            <div style="display: flex; align-items: start; flex: 1;">

                <div class="drive-title-section">
                    <div class="drive-title">{{ drive.id }}:{{drive.job_title}}</div>
                    <h4>{{ drive.company_name }}</h4>

                </div>
            </div>
            <div class="status-badges">
              
                <span v-if="drive.status == 'APPROVED'" class="badge badge-approved">APPROVED</span>
                
                <span v-else-if="drive.status == 'PENDING'" class="badge badge-pending">PENDING</span>
                
                <span v-else class="badge badge-closed">CLOSED</span>
                
            </div>
        </div>

        <div class="drive-meta">

            <div class="meta-item">
                <p>Description : {{ drive.eligibility }} </p>

                <p>Description : {{ drive.description }} </p>
            </div>
            <div class="meta-item">
                <i class="bi bi-calendar-x"></i>
                <span>Deadline: {{drive.deadline}}</span>
            </div>


        </div>



        <div class="action-buttons">
           
                <button class="btn-action btn-view">
                    <i class="bi bi-eye"></i> View Details
                </button>
            
            
                <button @click="handleToggleStatus(drive)" v-if="drive.status == 'PENDING'" class="btn-action btn-approve">
                    <i class="bi bi-check-circle"></i> Approve
                </button>
                
                <button @click="handleToggleStatus(drive)" v-else-if="drive.status=='APPROVED'" class="btn-action btn-reject">
                    <i class="bi bi-x-circle"></i> Pending
                </button>       
                <button @click="handleToggleClosed(drive)" v-if="drive.status == 'CLOSED'" class="btn-action btn-approve">
                    <i class="bi bi-check-circle"></i> Unclose
                </button>
                
                <button @click="handleToggleClosed(drive)" v-else-if="drive.status!='CLOSED'" class="btn-action btn-reject">
                    <i class="bi bi-x-circle"></i> Close
                </button>
                
              
        </div>
    </div>

</div>



  </div>
</template>

<script setup>
import { ref,onMounted } from 'vue';
import { adminAPI } from '@/services/api';

const stats = ref({
    t_p:0,t_a:0,t_c:0,total:0
})

const drives = ref([])

const fetchADrives = async () => {
    try {
        const response = await adminAPI.getDrives();
        
        // Success: Handle your statistics data
        const serverData = response.data.data;

        stats.value = {
            t_p:serverData.t_p,
            t_a:serverData.t_a,
            t_c:serverData.t_c,
            total:serverData.total
        }

        drives.value = serverData.drives
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

const handleToggleStatus = async (student) => {
    const action = student.status === 'APPROVED' ? 'block' : 'unblock';
    
    // Confirm with user
    if (!confirm(`Are you sure you want to ${action} this drive?`)) return;

    try {
        const response = await adminAPI.approveDrive(student.id);
        fetchADrives();
        console.log(response.data)
    } catch (error) {
        console.error("Failed to change status:", error);
        alert("Error updating status");
    }
}

const handleToggleClosed = async (student) => {
    const action = student.status === 'CLOSED' ? 'unclose' : 'close';
    
    // Confirm with user
    if (!confirm(`Are you sure you want to ${action} this drive?`)) return;

    try {
        const response = await adminAPI.closeDrive(student.id);
        fetchADrives();
        console.log(response.data)
    } catch (error) {
        console.error("Failed to change status:", error);
        alert("Error updating status");
    }
}

onMounted(() =>{
    fetchADrives();
})
</script>