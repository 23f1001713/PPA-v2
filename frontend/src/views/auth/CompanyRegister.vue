<style scoped>
.main-co {
            max-width: 1200px;
            margin: 30px auto;
            padding: 0 30px;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        }

        .pro-cont {
            background: white;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
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
            width: 450px;
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
</style>

<template>
  <div class="main-co">
        <div class="pro-cont">
            <div class="register_as">
                <button type="button" ><RouterLink to="/register/student">Register for Student</RouterLink></button>
                
            </div>
            <div v-if="alertMessage" :class="['alert', alertType]">
        {{ alertMessage }}
        <button class="close-alert" @click="clearAlert">&times;</button>
      </div>

            <form @submit.prevent="handleSubmit">
                <h2>Company Registraion Form
                </h2>

                <div class="form-section">
                    <div class="form-grid">
                        <div class="form-group">
                            <label class="form-label required" for="email">Email:</label>
                            <input class="form-control" type="email" v-model="formData.email" name="email" id="email" required :disabled="loading">
                        </div>
                        <div class="form-group">
                            <label class="form-label required" for="username">Username:</label>
                            <input class="form-control" type="text" v-model="formData.username" name="username" id="username" required :disabled="loading">
                        </div>
                        <div class="form-group">
                            <label class="form-label required" for="password">Password:</label>
                            <input class="form-control" type="password" v-model="formData.password" name="password" id="password" required :disabled="loading">
                        </div>
                        <div class="form-group">
                            <label class="form-label required" for="name">Company Name :</label>
                            <input class="form-control" type="text" name="name" v-model="formData.name" id="name" placeholder="Company Name"
                                required :disabled="loading">
                        </div>
                        <div class="form-group">
                            <label class="form-label required" for="name">Hr Contact :</label>
                            <input class="form-control" type="text" name="hr" v-model="formData.hr" id="hr" placeholder="Hr Contact" required :disabled="loading">
                        </div>
                        <div class="form-group">
                            <label class="form-label required" for="name">Website :</label>
                            <input class="form-control" type="text" v-model="formData.website" name="website" id="website" placeholder="Website"
                                required :disabled="loading">
                        </div>
                    </div>
                </div>

                <br>
                <button class="btn btn-primary" style="margin-left: 500px;" type="submit">Register</button>

            </form>
            <div class="footer">
                <p>Already have an Account <RouterLink style="text-decoration: none;" to="/login" >Login here</RouterLink></p>
            </div>

</div>
</div>

</template>

<script>
import { ref } from 'vue'
import { useRouter } from 'vue-router'


export default {
  name: 'CompanyRegister',
  setup() {
    const router = useRouter()
    
    const formData = ref({
      email: '',
      username: '',
      password: '',
      name: '',
      hr: '',
      website: ''
    })

    const loading = ref(false)
    const alertMessage = ref('')
    const alertType = ref('')

     const clearAlert = () => {
      alertMessage.value = ''
      alertType.value = ''
    }

    const showAlert = (message, type) => {
      alertMessage.value = message
      alertType.value = type
      // Auto clear after 5 seconds
      setTimeout(() => {
        clearAlert()
      }, 5000)
    }


    const validateForm = () => {
      if (!formData.value.email.match()) {
        showAlert('Please enter a valid email address', 'alert-error')
        return false
      }
      
      if (formData.value.password.length < 6) {
        showAlert('Password must be at least 6 characters long', 'alert-error')
        return false
      }
      
      if (!formData.value.website.match(/^https?:\/\/.+/)) {
        showAlert('Please enter a valid website URL (start with http:// or https://)', 'alert-error')
        return false
      }
      
      return true
    }
    const handleSubmit = async () => {
      // Clear previous alerts
      clearAlert()
      
      // Validate form
      if (!validateForm()) {
        return
      }

    loading.value = true
      
      try {
        // Prepare data to send to backend
        const requestData = {
          email: formData.value.email,
          username: formData.value.username,
          password: formData.value.password,
          company_name: formData.value.name,
          hr_contact: formData.value.hr,
          website: formData.value.website,
          role: 'company'
        }
        const response = await fetch('http://localhost:5000/api/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          },
          body: JSON.stringify(requestData)
        })
        
        // Parse response
        const data = await response.json()
        
        if (response.ok) {
          // Registration successful
          showAlert('Company registration successful! Please wait for admin approval.', 'alert-success')
          
          // Reset form
          formData.value = {
            email: '',
            username: '',
            password: '',
            name: '',
            hr: '',
            website: ''
          }
          
          // Redirect to login page after 2 seconds
          setTimeout(() => {
            router.push('/login')
          }, 2000)
        } else {
          // Registration failed
          showAlert(data.message || 'Registration failed. Please try again.', 'alert-error')
        }
        
      } catch (error) {
        console.error('Registration error:', error)
        showAlert('Network error. Please check if the backend server is running.', 'alert-error')
      } finally {
        loading.value = false
      }
    }
    
    return {
      formData,
      loading,
      alertMessage,
      alertType,
      handleSubmit,
      clearAlert
    }
  }
}

</script>