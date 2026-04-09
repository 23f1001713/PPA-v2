<style scoped>
.main-container{
  margin: 30px 150px;
  width:100%;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
.app-con {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .app-card {
            background: white;
            border-radius: 16px;
            padding: 28px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
            border-left: 5px solid blue;
        }

        .app-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        }

        .app-card-header {
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 20px;
            padding-bottom: 20px;
            border-bottom: 2px solid #f0f0f0;
        }

        .app-t {
            font-size: 1.4rem;
            font-weight: 700;
            color: #2d3436;
            margin-bottom: 8px;
        }

        .app-c {
            color: #667eea;
            font-size: 1rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .status-b {
            padding: 10px 20px;
            border-radius: 25px;
            font-size: 0.85rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            white-space: nowrap;
        }

        .status-applied {
            background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
            color: white;
        }

        .status-shortlisted {
            background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%);
            color: #2d3436;
        }

        .status-selected {
            background: linear-gradient(135deg, #55efc4 0%, #00b894 100%);
            color: white;
        }

        .status-rejected {
            background: linear-gradient(135deg, #fab1a0 0%, #ff7675 100%);
            color: white;
        }


</style>

<template>
  <div class="main-container">
    <div class="app-con">

        <div class="app-card">
            <div class="app-card-header">
                <div class="app-i">
                    <div class="app-id">#1</div>
                    <div class="app-t"> Job Title</div>

                </div>
              
                <span class="status-b status-selected">Selected</span>
               
                <span class="status-b status-shortlisted">Shortlisted</span>
                
                <span class="status-b status-rejected">Not Selected</span>
                
                <span class="status-b status-applied">In Progress</span>
                
            </div>

            <div class="app-m">
                <div class="meta-b">
                    <div class="meta-l">Applied On</div>
                    v <i class="bi bi-calendar3"></i>
                    Date
                </div>
            </div>

        </div>



    </div>

  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { studentAPI } from '@/services/api';

const fetcAppl  = async ()=>{
    try{
        const response = await studentAPI.getApplications();
        console.log(response.data)
    }catch(error){
        console.log(error.message)
    }
}

onMounted(() =>{
    fetcAppl();
})

</script>