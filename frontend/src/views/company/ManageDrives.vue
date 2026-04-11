
<style scoped>
.main-container{
  margin: 10px 200px;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.btn-create-drive {
            background: white;
            color: blue;
            padding: 14px 30px;
            border-radius: 30px;
            border: none;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 1rem;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
        }

        .btn-create-drive:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
        }

        .drives {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .drive {
            background: linear-gradient(to bottom, #ffffff 0%, #f8f9fa 100%);
            border-radius: 16px;
            padding: 25px;
            border: 2px solid #e9ecef;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .drive::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 5px;
            height: 100%;
            background-color: blue;
        }

        .drive:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
            border-color: blue;
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

        .drive-id {
            font-size: 0.85rem;
            color: #b2bec3;
            font-weight: 600;
        }

        .drive-s {
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .status-pending {
            background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%);
            color: #2d3436;
            animation: pulse 2s infinite;
        }

        .status-active {
            background: linear-gradient(135deg, #55efc4 0%, #00b894 100%);
            color: white;
        }

        .status-closed {
            background: linear-gradient(135deg, #dfe6e9 0%, #b2bec3 100%);
            color: #2d3436;
        }
.sec-card {
            background: white;
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            margin-bottom: 30px;
        }

        .sec-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 25px;
            width: 1000px;
            padding-bottom: 20px;
            border-bottom: 2px solid #f0f0f0;
        }

        .sec-header h2 {
            font-size: 1.5rem;
            font-weight: 700;
            color: #2d3436;
            display: flex;
            align-items: center;
            gap: 12px;
            margin: 0;
        }

        .drive-actions {
            display: flex;
            gap: 10px;
            margin-top: 15px;
            padding-top: 15px;
            border-top: 2px solid #f0f0f0;
        }

        .btn-action {
            flex: 1;
            padding: 10px 18px;
            border-radius: 8px;
            border: none;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            font-size: 0.9rem;
        }

        .btn-view {
            background-color: blue;
            color: white;
        }

        .btn-view:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .btn-edit {
            background: white;
            color: blue;
            border: 2px solid blue;
        }

        .btn-edit:hover {
            background: #667eea;
            color: white;
        }
a{
  text-decoration: none;
}



</style>
<template>
  <div class="main-container">
    <div class="dri">

    <div class="sec-card">
        <div class="sec-header">
            <h2>
                <i class="bi bi-briefcase-fill icon"></i>
                Active Placement Drives
            </h2>
            <RouterLink to="/company/drives/create" >
                <div class="welcome-actions">
                    <button class="btn-create-drive">
                        Create New Drive
                    </button>
                </div>
            </RouterLink>
        </div>
        

        <div class="drives">
            
            <div v-for="d in drives" :key="d.id" class="drive">
                <div class="drive-h">
                    <div>
                        <div class="drive-id">{{ d.id }}</div>
                        <div class="drive-t">{{d.title}}</div>
                    </div>
                    
                    <span v-if="d.status == 'PENDING'" class="drive-s status-pending">Pending Approval</span>
                   
                    <span v-else-if="d.status=='APPROVED'" class="drive-s status-active">Active</span>
                 
                    <span v-else class="drive-s status-closed ">Closed</span>
                   
                </div>

                <div class="drive-m">
                    <div class="meta-i">
                        <i class="bi bi-geo-alt-fill"></i>
                        <span>Description : {{ d.description }} </span>

                        <div class="meta-i">
                            <i class="bi bi-calendar-check"></i>
                            <span>Deadline: {{ d.date }}</span>
                        </div>

                    </div>
                </div>



                <div class="drive-actions">
                    
                        <button class="btn-action btn-view">
                            
                            View Applicants
                        </button>
                    
                   
                        <button @click="handleEdit(d)" class="btn-action btn-edit">
                           
                            Edit
                        </button>
                    
                    
                        <button v-if="d.status == 'CLOSED'" @click="closeD(d)" class="btn-action btn-edit">
                            
                            Unclose
                        </button>
                        <button v-else @click="closeD(d)" class="btn-action btn-edit">
                            
                            Close
                        </button>
                    
                </div>
            </div>
            
          



</div>
        </div>
    </div>
</div>


</template>

<script setup>
import { ref,onMounted } from 'vue';
import { companyAPI } from '@/services/api';
import { useRouter } from 'vue-router';

const drives = ref([]) 

const CompanyDrive = async()=>{
    try{
        const response = await companyAPI.getDrives();
        const serverData = response.data.data

        drives.value = serverData.drives
    }catch(error){
        console.log(error.message)
    }
}

const closeD = async (d)=>{
    const action = d.status === 'CLOSED' ? 'unclose' : 'close';
    console.log(d.status)
    if (!confirm(`Are you sure you want to ${action} this drive?`)) return;
    console.log(d.id)
    try {
        const response = await companyAPI.closeDrive(d.id);
        console.log(response.data)
        CompanyDrive()
    }catch(error){
        console.error("Failed to change status:", error);
        alert("Error updating status");
    }
}

const router = useRouter()

const handleEdit = (driveId) => {
    const id = driveId.id
    console.log('Navigating with ID:', driveId?.id || driveId); 
  router.push(`/company/drives/edit/${id}`)
}

onMounted(()=>{
    CompanyDrive()
})
</script>