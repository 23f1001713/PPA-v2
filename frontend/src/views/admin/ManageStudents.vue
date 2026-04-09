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
    <h1><i class="bi bi-people"></i> Student Management</h1>


</div>
<div class="nav">
    <form >
        <div class="search">
            <input type="text" placeholder="Search companies..." name="search">
        
        <input  style="background-color: blue; color: white;" class="btn btn-outline-success" type="submit" value="Search">
        </div>
    </form>

</div>





<div class="stats" v-if="stats">
    <div class="stat hov">
        <div class="stat-number">{{ stats.t_s }}</div>
        <div class="stat-label">Total Students</div>
    </div>
    <div class="stat applied hov">
        <div class="stat-number">{{ stats.s_a }}</div>
        <div class="stat-label">Approved</div>
    </div>
    <div class="stat shortlisted hovr">
        <div class="stat-number">{{ stats.s_b }}</div>
        <div class="stat-label">Blacklisted</div>
    </div>
</div>
<div class="stats" v-else>Loading Stats here....</div>
<div id="tableView">
    <table class="app-tab">
        <thead>
            <tr>

                <th>Student ID</th>
                <th>Student Name</th>
                <th>Total Applications</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            
            <tr  v-for="student in students" :key="student.id">


                <td><strong>{{ student.id }}</strong></td>
                <td>
                    <div class="s-cell">

                        <div class="stud-deta">
                            <div class="stud-name">{{ student.name }}</div>

                        </div>
                    </div>
                </td>

                <td>
                    <div class="d-info">
                        
                        <div class="drive-title-sm">{{ student.app_count }}</div>

                    </div>
                </td>

                <td>

                    <span class="status-badge status-selected" v-if="student.status == 'APPROVED'">Approved</span>

                    
                    <span class="status-badge status-shortlisted" v-else>Blocked</span>

                    

                </td>
                <td>
                    <div class="t-a">
                        <a href="#">
                            
                            <button @click="handleToggleStatus(student)" v-if="student.status != 'APPROVED'" style="background-color: #28a745; color: white;" class="btn-sm btn-view">
                                <i class="bi bi-unlock"></i> Unblock
                            </button>
                           
                            <button @click="handleToggleStatus(student)" v-else style="background-color: #dc3545; color: white;" class="btn-sm btn-view">
                                <i class="bi bi-slash-circle"></i> Block
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
import { ref,onMounted } from 'vue';
import { adminAPI } from '@/services/api';
import { useRouter } from 'vue-router';
import { defineStore } from 'pinia';

const stats = ref({
    s_a:0,s_b:0,t_s:0
})

const students = ref([])


const fetchAStudent = async () => {
    try {
        const response = await adminAPI.getStudents();
        const serverData = response.data.data;
        stats.value = {
      s_a: serverData.s_a,
      s_b: serverData.s_b,
      t_s: serverData.t_s
    };

    console.log(serverData)
    students.value = serverData.students
        
        
        
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
    const action = student.status === 'APPROVED' ? 'unblock' : 'block';
    
    // Confirm with user
    if (!confirm(`Are you sure you want to ${action} this student?`)) return;

    try {
        const response = await adminAPI.blacklistStudent(student.id);
        fetchAStudent();
        console.log(response.data)
    } catch (error) {
        console.error("Failed to change status:", error);
        alert("Error updating status");
    }
};

// export const useSearchStore = defineStore('search', {
//   state: () => ({
//     results: [],
//     isLoading: false
//   }),
//   actions: {
//     async performSearch(text) {
//       this.isLoading = true;
//       try {
//         const response = await adminAPI.search(text);
//         this.results = response.data; // Store response
//       } finally {
//         this.isLoading = false;
//       }
//     }
//   }
// });

onMounted(() =>{
    fetchAStudent();
})
</script>