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
</style>

<template>
  <div class="main-container">
    <div class="header">
        <div class="welcomecon">
            <h1>Welcome ,Akash Maurya !</h1>

        </div>
    </div>

    <div class="stats">
        <div class="stat">
            <div class="stat-n">10</div>
            <div class="stat-l">Active Drives</div>
        </div>

        <div class="stat ">
            <div class="stat-n">10</div>
            <div class="stat-l">Applied</div>
        </div>

        <div class="stat ">
            <div class="stat-n">10</div>
            <div class="stat-l">Shortlisted</div>
        </div>

    
        <div class="stat ">
            <div class="stat-n">10</div>
            <div class="stat-l">Rejected</div>
        </div>
    </div>


<div class="quick">
  <div class="panel"><h3>View Recent Jobs</h3>
  <button>View More</button>
  </div>
  <div class="panel"><h3>Recent Applications</h3>
  <button>View More</button>
  </div>
</div>

    
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { studentAPI } from '@/services/api';

const studDash = async ()=>{
  try{
    const response = await studentAPI.getDashboard();
    console.log(response.data)
  }catch(error){
    console.log(error.message)
  }
}
onMounted(() => {
  studDash();
});

</script>