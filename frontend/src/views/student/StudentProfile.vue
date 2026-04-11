<style scoped>
.main-container{
  margin: 30px 150px;
  width:100%;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
.pro-con {
            display: grid;
            grid-template-columns: 350px 1fr;
            gap: 30px;
        }

        .pro-side {
            background: white;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
            text-align: center;
            height: fit-content;
        }

        .pro-pic-con {
            position: relative;
            width: 180px;
            height: 180px;
            margin: 0 auto 20px;
        }

        .pro-pic {
            width: 180px;
            height: 180px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4rem;
            font-weight: bold;
            border: 5px solid #f0f0f0;
        }

        .pro-pic img {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
        }

        .change-photo-btn {
            position: absolute;
            bottom: 10px;
            right: 10px;
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: #667eea;
            color: white;
            border: 3px solid white;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 1.2rem;
        }

        .change-photo-btn:hover {
            background: #5568d3;
            transform: scale(1.1);
        }

        .pro-com {
            margin-top: 25px;
            padding-top: 25px;
            border-top: 1px solid #f0f0f0;
        }

        .com-text {
            font-size: 0.9rem;
            color: #636e72;
            margin-bottom: 10px;
        }

        .com-tage {
            font-size: 2rem;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 10px;
        }

        .pro-bar {
            width: 100%;
            height: 8px;
            background: #e9ecef;
            border-radius: 10px;
            overflow: hidden;
        }

        .pro-fill {
            height: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            width: 85%;
            transition: width 0.5s ease;
        }

        .com-tips {
            margin-top: 20px;
            text-align: left;
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
        }

        .com-tips h4 {
            font-size: 0.9rem;
            font-weight: 600;
            color: #2d3436;
            margin-bottom: 10px;
        }

        .com-tips ul {
            margin: 0;
            padding-left: 20px;
            font-size: 0.85rem;
            color: #636e72;
        }

        .com-tips li {
            margin-bottom: 5px;
        }


        .pro-cont {
            background: white;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        }

        .sec-title {
            font-size: 1.3rem;
            font-weight: 600;
            color: #2d3436;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #f0f0f0;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .sec-title i {
            color: #667eea;
        }

        .form-section {
            margin-bottom: 35px;
        }

        .form-section:last-child {
            margin-bottom: 0;
        }

        .form-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }

        .form-grid.single {
            grid-template-columns: 1fr;
        }

        .form-group {
            margin-bottom: 0;
        }

        .form-label {
            font-size: 0.9rem;
            font-weight: 600;
            color: #2d3436;
            margin-bottom: 8px;
            display: block;
        }

        .form-label.required::after {
            content: ' *';
            color: #d63031;
        }

        .form-control {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            font-size: 0.95rem;
            transition: all 0.3s ease;
        }

        .form-control:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }

        textarea.form-control {
            resize: vertical;
            min-height: 100px;
        }

        .form-help {
            font-size: 0.8rem;
            color: #636e72;
            margin-top: 5px;
        }

        .form-actions {
            display: flex;
            gap: 15px;
            margin-top: 30px;
            padding-top: 25px;
            border-top: 2px solid #f0f0f0;
        }

        .btn {
            padding: 12px 30px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 0.95rem;
        }

        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            flex: 1;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .btn-secondary {
            background: white;
            border: 1px solid #e0e0e0;
            color: #636e72;
        }

        .btn-secondary:hover {
            background: #f8f9fa;
            border-color: #667eea;
            color: #667eea;
        }

</style>

<template>
  <div class="main-container">
    <div class="header">
        <h1><i class="bi bi-person-circle"></i> My Profile</h1>
        <p> Your personal information</p>
    </div>





    <div class="pro-con">

        <div class="pro-side">
            <div class="pro-pic-con">
                <div class="pro-pic">
                    add

                </div>
                <label for="profilePicture" class="change-photo-btn">
                    <i class="bi bi-camera"></i>
                </label>
                <input type="file" id="profilePicture" style="display: none;" accept="image/*">
            </div>

            <h3 style="margin-bottom: 5px; color: #2d3436;">{{data.name}}</h3>



            <div class="pro-com">
                <div class="com-text">Profile Completion</div>
                <div class="com-tage">85%</div>
                <div class="pro-bar">
                    <div class="pro-fill"></div>
                </div>

                <div class="com-tips">
                    <h4>Complete Your Profile:</h4>
                    <ul>
                        <li>Add profile picture</li>
                        <li>Update skills section</li>
                        <li>Upload latest resume</li>
                    </ul>
                </div>
            </div>
        </div>

        <div class="profile-cont">


            <div class="form-section">
                <h2 class="sec-title">
                    <i class="bi bi-person-fill"></i>
                    Personal Information
                </h2>

                <div class="form-grid">
                    <div class="form-group">
                        <label class="form-label required">Full Name</label>
                        <input type="text" class="form-control" v-model="data.name"
                            placeholder="Enter your full name">
                    </div>



                    <div class="form-group">
                        <label class="form-label required">Email </label>
                        <input type="email" class="form-control" v-model="data.email" placeholder="Enter email">
                    </div>

                    <div class="form-group">
                        <label class="form-label required">Username</label>
                        <input type="text" class="form-control" v-model="data.username"
                            placeholder="Enter phone number">
                    </div>

                    <div class="form-group">
                        <label class="form-label">Date of Birth</label>
                        <input type="date" class="form-control" value="enter DOB">
                    </div>

                    <div class="form-group">
                        <label class="form-label">Gender</label>
                        <select class="form-control">
                            <option value="">Select Gender</option>
                            <option value="male" selected>Male</option>
                            <option value="female">Female</option>
                            <option value="other">Other</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Resume</label>
                        <input  type="file" class="form-control" value="Upload your resume">
                    </div>
                </div>
            </div>



            <div class="form-section">
                <h2 class="section-title">
                    <i class="bi bi-link-45deg"></i>
                    Social Links (Optional)
                </h2>

                <div class="form-grid">
                    <div class="form-group">
                        <label class="form-label">LinkedIn Profile</label>
                        <input type="url" class="form-control" placeholder="https://linkedin.com/in/yourprofile">
                    </div>

                    <div class="form-group">
                        <label class="form-label">GitHub Profile</label>
                        <input type="url" class="form-control" placeholder="https://github.com/yourusername">
                    </div>

                    <div class="form-group">
                        <label class="form-label">Portfolio Website</label>
                        <input type="url" class="form-control" placeholder="https://yourportfolio.com">
                    </div>

                    <div class="form-group">
                        <label class="form-label">Other Link</label>
                        <input type="url" class="form-control" placeholder="https://...">
                    </div>
                </div>
            </div>

            <!-- Action Buttons -->
            <div class="form-actions">
                <button @click="updateP" type="button" class="btn btn-primary">
                    <i class="bi bi-check-circle"></i> Save Changes
                </button>
                <button type="button" class="btn btn-secondary">
                    <i class="bi bi-x-circle"></i> Cancel
                </button>
            </div>

        </div>
    </div>


  </div>
</template>

<script setup>

import { studentAPI } from '@/services/api';
import { ref,onMounted } from 'vue';

const data = ref({
    'username':'',
    'email':'',
    'branch':'',
    'name':'',
    'cgpa':'',
    'resume':'',
    'status':''    
})

const getData = async() =>{
    try{
        const response = await studentAPI.getProfile()

        const serverData = response.data.data

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
        console.log(data)
    }catch(error){
        console.log(error.message)
    }
    
}

const updateP = async() =>{
    try{
        const payload = {
      username: data.value.username,
      email: data.value.email,
      branch: data.value.branch,
      name: data.value.name,
      cgpa: data.value.cgpa,
      status: data.value.status
    }
    const response = await studentAPI.updateProfile(payload);
        const serverData = response.data
        alert('Profile updated sucessful!')
        console.log(serverData)
    }catch(error){
        console.log(error)
    }
}
onMounted(() =>{
    getData()
})
</script>