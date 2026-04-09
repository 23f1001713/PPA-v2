<style scoped>
.main-container{
  margin: 30px 150px;
  width:100%;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
.header {
        background-color: white;
        color: black;
        padding: 40px;
        border-radius: 20px;
        margin-bottom: 30px;
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
    }

    .header h1 {
        font-size: 2.3rem;
        margin-bottom: 10px;
        font-weight: 800;
    }

    .drives {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(480px, 1fr));
            gap: 25px;
        }

        .drive {
            background: linear-gradient(to bottom, #ffffff 0%, #f8f9fa 100%);
            border-radius: 16px;
            padding: 25px;
            border: 2px solid #e9ecef;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
            border-left: 5px solid blue;
        }
        

        .drive:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
            border-color: #667eea;
        }

        .drive-h {
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 15px;
        }

        .drive-t {
            font-size: 1.2rem;
            font-weight: 700;
            color: #2d3436;
            margin-bottom: 8px;
        }

        .c-name {
            color: #667eea;
            font-size: 0.95rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .drive-b {
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            white-space: nowrap;
        }

        .badge-new {
            background: linear-gradient(135deg, #00b894 0%, #00cec9 100%);
            color: white;
        }



button{
          padding: 10px 20px;
          background-color: blueviolet;
          color: white;
          border-radius: 15px;
        }


</style>

<template>
  <div class="main-container">
    <div class="header">
        <h1><i class="bi bi-briefcase-fill"></i> Placement Drives</h1>
    </div>

    <div class="drives">

        
        <div v-for="d in drives" :key="d.id" class="drive">
            <div class="drive-h">
                <div>
                    <div class="drive-t">{{ d.title }}</div>
                    <div class="c-name">
                        <i class="bi bi-building"></i>
                      {{ d.company_name }}
                    </div>
                </div>
                <span class="drive-b badge-new">New</span>

            </div>

            <p class="drive-description">
                description:{{ d.description }}
            </p>

            <div class="drive-m">

                <div class="meta-i">
                    <i class="bi bi-calendar-check"></i>
                    <span>Deadline: {{ d.deadline }}</span>
                </div>

            </div>
            <div class="drive-tags">
                <p style="font-size: 12px;">Eligibility : {{ d.eligibility }}</p><span class="tag">Eligibility</span>
            </div>


            <div class="drive-f">
                <a class="btn-apply" href="/">
                    <button @click="applyNow" class="btn-apply">
                        <i class="bi bi-send-fill"></i>
                        Apply Now
                    </button>
                </a>

            </div>
        </div>
        
    </div>

  </div>
</template>

<script setup>
import { onMounted ,ref} from 'vue';
import { studentAPI } from '@/services/api';
const drives = ref([])


const drivefetch = async() =>{
    try{
        const response = await studentAPI.getDrives();
        const serverData = response.data.data;
        drives.value = serverData.drives
        console.log(serverData)
    }catch(error){
        console.log(error.message)
    }
}

const applyNow= async(drive)=>{
    try{
        
        const apply = await studentAPI.applyForDrive(drive.id)
        drivefetch()
        alert(apply.data)
        console.log(apply.data)
          
    }catch (error) {
        console.error("Failed to Apply:", error);
        
    }
}

onMounted(()=>{
    drivefetch();
}
)


</script>