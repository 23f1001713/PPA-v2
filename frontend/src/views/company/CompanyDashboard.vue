<style scoped>
.main-container{
  margin: 10px 200px;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
.banner {
            background-color: white;
            color: black;
            padding: 50px;
            width: 1000px;
            border-radius: 20px;
            margin-bottom: 30px;
            box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
            position: relative;
            overflow: hidden;
        }


        .wel-con {
            position: relative;
            z-index: 1;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .wel-text h1 {
            font-size: 2.5rem;
            margin-bottom: 12px;
            font-weight: 800;
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }

        .stat {
            background: white;
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
            border-left: 5px solid blue;
            display: flex;
            align-items: center;
            gap: 20px;
        }

        .stat:hover {
            transform: translateY(-8px);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
            border: 1px solid blue;
        }





        .stat-i h3 {
            font-size: 2.2rem;
            font-weight: 800;
            color: #2d3436;
            margin-bottom: 5px;
        }

        .stat-i p {
            color: #636e72;
            font-size: 0.95rem;
            margin: 0;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-weight: 600;
        }

        .quick-actions-panel {
            background: white;
            border-radius: 16px;
            padding: 25px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            margin-bottom: 30px;
        }

        .quick-actions-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 12px;
        }

        .action-item {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 18px;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 15px;
            border: 2px solid transparent;
        }

        .action-item:hover {
            background: white;
            border-color: blue;
            transform: translateX(5px);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        .action-icon {
            width: 50px;
            height: 50px;
            border-radius: 12px;
            background-color: blue;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.4rem;
            flex-shrink: 0;
        }

        .action-text {
            flex: 1;
        }

        .action-title {
            font-weight: 700;
            color: #2d3436;
            font-size: 0.95rem;
            margin-bottom: 3px;
        }

        .action-desc {
            font-size: 0.8rem;
            color: #636e72;
        }

        a{
          text-decoration: none;
        }




</style>
<template>
  <div class="main-container">
    <div class="banner">
        <div class="wel-con">
            <div class="wel-text">
                <h1>Welcome back,{{ stats.name }}</h1>
                <p>Status : {{ stats.status }}</p>
                <p>website : {{ stats.website }}</p>
            </div>
            </div>
</div>
<div class="stats">
        <div class="stat">

            <div class="stat-i">
                <h3>{{ stats.pd }} </h3>
                <p>Pending Approval</p>
            </div>
        </div>

        <div class="stat ">

            <div class="stat-i">
                <h3>{{ stats.td }}</h3>
                <p>Active Drives</p>
            </div>
        </div>

        <div class="stat ">

            <div class="stat-i">
                <h3>{{ stats.ta }}</h3>
                <p>Total Applicants</p>
            </div>
        </div>

        <div class="stat">

            <div class="stat-i">
                <h3>{{ stats.sh }}</h3>
                <p>Shortlisted</p>
            </div>
        </div>
    </div>


<div>

    <div class="quick-actions-panel">
        <div class="section-header" style="border: none; padding-bottom: 0; margin-bottom: 20px;">
            <h2 style="font-size: 1.2rem;">
                <i class="bi bi-lightning-fill icon"></i>
                Quick Actions
            </h2>
        </div>

        <div class="quick-actions-grid">
            <RouterLink to="/company/drives/create" >
                <div class="action-item">
                    
                    <div class="action-text">
                        <div class="action-title">Create New Drive</div>
                        <div class="action-desc">Post a new job opportunity</div>
                    </div>
                </div>
            </RouterLink>

            <RouterLink to="/company/applications" >
                <div class="action-item">
                    
                    <div class="action-text">
                        <div class="action-title">Review Applicants</div>
                        <div class="action-desc">View and shortlist candidates</div>
                    </div>
                </div>
            </RouterLink >

            <RouterLink to="/company/drives" >
                <div class="action-item">
                    
                    <div class="action-text">
                        <div class="action-title">Manage Drives</div>
                        <div class="action-desc">Edit or close existing drives</div>
                    </div>
                </div>
            </RouterLink >




        </div>
    </div>

</div>



</div>


  
</template>


<script setup>

import { ref,onMounted } from 'vue';
import { companyAPI } from '@/services/api';


const stats = ref({
pd:0 , sh:0,td:0 , ta:0,name:'',status:'',website:'',
})
const fetchdata = async () =>{
    try{
    const response = await companyAPI.getDashboard();
    const serverData = response.data.data;

    stats.value = {
        pd:serverData.statistics.pending_drives,
        sh:serverData.statistics.shortlisted,
        td:serverData.statistics.total_drives,
        ta:serverData.statistics.total_applications,
        name:serverData.company.name,
        website:serverData.company.website,
        status:serverData.company.status
    }
    console.log(serverData)
}catch (error){
    console.log(error.message)
}
}

onMounted(() =>{
    fetchdata()
})

</script>