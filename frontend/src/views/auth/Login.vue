<style scoped>
.main-container{
  margin: 10px 200px;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
.container{
  margin: 100px 300px;
}

.container h2{
  margin: 0 0 30px 0;
  font-size: 3rem;
}
.mb-3{
  margin-bottom: 30px;
}
label{
  font-weight: 600;
}
input{
  padding: 15px 30px;
  margin-top: 10px;
  width: 350px;
  border-radius: 7px;
}
.dgrid button{
  padding: 10px 30px;
  margin-left:150px ;
  color: white;
  background-color: blue;
  border-radius: 8px;

}

.register button{
  padding: 8px 30px;
  margin-left: 30px;
}

a{
  text-decoration: none;
}


</style>
<template>
  <div class="main-container">
            <div class="container">
              <div v-if="alertMessage" :class="['alert',alertType]">
                {{ alertMessage }}
              </div>
                <h2 class="mb-3">Welcome Back,______
                </h2>

                <form @submit.prevent ="handleSubmit">
                    <div class="mb-3">
                        <label for="username" class="form-label">Username</label><br>
                        <input type="username" class="form-control" v-model="formData.username" id="username" name="username"
                            placeholder="Your Username" :disabled="loading">
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">Password</label><br>
                        <input type="password" class="form-control" v-model="formData.password" id="password" name="password"
                            placeholder="password" :disabled="loading">
                    </div>

                    <div class="dgrid">
                        <button type="submit" class="btn btn-primary w-100">Log In</button>

                    </div>
                </form>


                <div class="mt-4 text-center">
                    <p>New to the portal?</p>
                    <div class="register">
                        <button><RouterLink to="/register/company"> Register Company</RouterLink></button>
                        <button><RouterLink to="/register/student"> Register Student</RouterLink></button>
                    </div>
                </div>
            </div>
        </div>


</template>

<script>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

export default {
  name: 'Login',
  setup() {
    const router = useRouter()

    const formData = ref({
      username: '',
      password: ''
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
      setTimeout(() => clearAlert(), 5000)
    }

    const handleSubmit = async () => {
      clearAlert()
      loading.value = true

      try {
        const response = await fetch('http://localhost:5000/api/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          },
          body: JSON.stringify(formData.value) // Simplified: sending the whole ref value
        })

        const data = await response.json()

        if (response.ok) {
          showAlert('Login successful! Redirecting...', 'alert-success')
          localStorage.setItem('user_token', data.token);
          localStorage.setItem('user_role', data.role);
          // To-Do: Store your JWT token here (localStorage.setItem('token', data.token))

        setTimeout(() => {
        if (data.role === 'ADMIN') {
            router.push('/admin/dashboard');
        } else if (data.role === 'COMPANY') {
            router.push('/company/dashboard');
        } else {
            router.push('/student/dashboard');
        }
    }, 1000);
        } else {
          // Use data.error to match your Flask backend
          showAlert(data.error || data.message || 'Login failed', 'alert-error')
        }
      } catch (error) { // Added (error) here
        console.error('Login error:', error)
        showAlert('Network error. Is the server running?', 'alert-error')
      } finally {
        loading.value = false
      }
    }

    return { formData, loading, alertMessage, alertType, handleSubmit }
  }
}
</script>