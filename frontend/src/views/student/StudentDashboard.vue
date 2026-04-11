<style scoped>
.main-container{
  margin: 30px 150px;
  width:100%;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
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

      
        .stat-n {
            font-size: 2.5rem;
            font-weight: 700;
            color: blue;
            margin-bottom: 8px;
        }

        .stat-l {
            font-size: 0.9rem;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-weight: 500;
        }

        .quick{
          display: flex;
          margin-top: 50px;
          justify-content: space-around;
        }

        .panel{
          padding: 10px 80px;
        }
        .panel button{
          padding: 10px 20px;
          background-color: blueviolet;
          color: white;
          border-radius: 15px;
        }
        a{
          text-decoration: none;
        }
</style>

<template>
  <div class="main-container">
    <div class="header">
        <div class="welcomecon">
            <h1>Welcome ,{{stats.name}} !</h1>

        </div>
    </div>

    <div class="stats" v-if="stats">
        <div class="stat">
            <div class="stat-n">{{ stats.t_d }}</div>
            <div class="stat-l">Active Drives</div>
        </div>

        <div class="stat ">
            <div class="stat-n">{{stats.t_a}}</div>
            <div class="stat-l">Applied</div>
        </div>

        <div class="stat ">
            <div class="stat-n">{{ stats.sh }}</div>
            <div class="stat-l">Shortlisted</div>
        </div>

    
        <div class="stat ">
            <div class="stat-n">{{ stats.re }}</div>
            <div class="stat-l">Rejected</div>
        </div>
    </div>

<div class="stats" v-else>Loading Data.....</div>

<div class="quick">
  <RouterLink to="/student/drives"><div class="panel"><h3>View Recent Jobs</h3>
  <button>View More</button>
  </div></RouterLink>
  <RouterLink to="/student/applications"><div class="panel"><h3>Recent Applications</h3>
  <button>View More</button>
  </div></RouterLink>
   <div class="panel"><h3>Download Report</h3>
  <button @click="downloadReport">HTML/TEXT</button>
  </div>
  <div class="panel"><h3>Export History</h3>
  <button @click="ExportCSV">Export History</button>
  </div>
</div>

    
  </div>



</template>

<script setup>
import { onMounted ,ref} from 'vue';
import { studentAPI } from '@/services/api';

const stats = ref ({
  t_d:0 ,t_a:0,sh:0,se:0,re:0,name:""
})
const data = ref({
    'username':'',
    'email':'',
    'branch':'',
    'name':'',
    'cgpa':'',
    'resume':'',
    'status':''    
})

const studDash = async ()=>{
  try{
    const response = await studentAPI.getDashboard();
    const serverData= response.data.data;

    stats.value = {
      t_d:serverData.total_drives,
      t_a:serverData.applied,
      sh:serverData.shortlisted,
      se:serverData.selected,
      re:serverData.rejected,
      name:serverData.student.name
    }
    data.value = {
            username:serverData.user.username,
            email:serverData.user.email,
            name:serverData.student.name,
            branch:serverData.student.branch,
            cgpa:serverData.student.cgpa,
            resume:serverData.student.resume,
            status:serverData.student.status
        }
    console.log(serverData)
  }catch(error){
    console.log(error.message)
  }
}
const ExportCSV = async () =>{
  try{
    const response = await studentAPI.exportCSV();
    alert(response.data.message + "\nTask ID: " + response.data.data.task_id);

    console.log("Task started:", response.data);

  } catch (error) {
    alert('Failed to export');

    console.error("Export error:", error.response?.data || error.message);
  }
}
const downloadReport = () => {
    const reportHtml = `
    <html>
        <head><title>Student Report</title></head>
        <body style="font-family: sans-serif; padding: 20px;">
            <h2>Academic Report: ${data.value.name}</h2>
            <hr>
            <p><strong>Username:</strong> ${data.value.username}</p>
            <p><strong>Email:</strong> ${data.value.email}</p>
            <p><strong>Branch:</strong> ${data.value.branch}</p>
            <p><strong>CGPA:</strong> ${data.value.cgpa}</p>
            <p><strong>Status:</strong> ${data.value.status}</p>
            <h2>Placement Report: ${data.value.name}</h2>
            <hr>
            <p><strong>Total Application:</strong> ${stats.value.t_a}</p>
            <p><strong>Selected:</strong> ${stats.value.se}</p>
            <p><strong>Rejected:</strong> ${stats.value.re}</p>
            <p><strong>Shortlisted:</strong> ${stats.value.sh}</p>
        </body>
    </html>`;

    // 2. Create a Blob and a download link
    const blob = new Blob([reportHtml], { type: 'text/html' });
    const url = URL.createObjectURL(blob);
    console.log(data)
    const link = document.createElement('a');
    link.href = url;
    link.download = `${data.value.name}_Report.html`; // Filename
    
    // 3. Trigger Click and Cleanup
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
};


onMounted(() => {
  studDash();
});

</script>