import axios from 'axios'

// Base configuration - CHANGE ONLY THESE VARIABLES
const API_BASE_URL = 'http://localhost:5000/api'
const API_TIMEOUT = 30000 // 30 seconds

// Create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: API_TIMEOUT,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
})

// Request interceptor - adds token to all requests
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('user_token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('token'); // Or wherever you store your JWT
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// ============================================
// AUTH API
// ============================================
export const authAPI = {
  login: (username, password) => 
    api.post('/auth/login', { username, password }),
  
  registerCompany: (data) => 
    api.post('/auth/register', data),
  
  registerStudent: (data) => 
    api.post('/auth/register', data),
  
  refreshToken: () => 
    api.post('/auth/refresh'),
  
  logout: () => 
    api.post('/auth/logout')
}

// ============================================
// ADMIN API
// ============================================
export const adminAPI = {
  getDashboard: () => 
    api.get('/admin/dashboard'),
  
  getCompanies: (params = {}) => 
    api.get('/admin/companies', { params }),
  
  approveCompany: (companyId, action) => 
    api.put(`/admin/companies/${companyId}/approve`, { action }),
  
  blacklistCompany: (companyId) => 
    api.put(`/admin/companies/${companyId}/blacklist`),
  
  getStudents: (params = {}) => 
    api.get('/admin/students', { params }),
  
  blacklistStudent: (studentId) => 
    api.put(`/admin/students/${studentId}/blacklist`),
  
  getDrives: (params = {}) => 
    api.get('/admin/drives', { params }),
  
  approveDrive: (driveId, action) => 
    api.put(`/admin/drives/${driveId}/approve`, { action }),
  
  closeDrive: (driveId) => 
    api.put(`/admin/drives/${driveId}/close`),
  
  getApplications: () => 
    api.get('/admin/applications'),
  
  search: (query, type = null) => 
    api.get('/admin/search', { params: { q: query, type } }),
  
  getMonthlyReport: () => 
    api.get('/admin/reports/monthly')
}

// ============================================
// STUDENT API
// ============================================
export const studentAPI = {
  getDashboard: () => 
    api.get('/student/dashboard'),
  
  getProfile: () => 
    api.get('/student/profile'),
  
  updateProfile: (data) => 
    api.put('/student/profile', data),
  
  getDrives: () => 
    api.get('/student/drives'),
  
  applyForDrive: (driveId) => 
    api.post(`/student/drives/${driveId}/apply`),
  
  getApplications: () => 
    api.get('/student/applications'),
  
  getHistory: () => 
    api.get('/student/history'),
  
  exportCSV: () => 
    api.post('/student/export/csv')
}

// ============================================
// COMPANY API
// ============================================
export const companyAPI = {
  getDashboard: () => 
    api.get('/company/dashboard'),
  
  getProfile: () => 
    api.get('/company/profile'),
  
  updateProfile: (data) => 
    api.put('/company/profile', data),
  
  getDrives: () => 
    api.get('/company/drives'),
  
  createDrive: (data) => 
    api.post('/company/drives', data),
  
  updateDrive: (driveId, data) => 
    api.put(`/company/drives/${driveId}`, data),
  
  deleteDrive: (driveId) => 
    api.delete(`/company/drives/${driveId}`),
  
  getApplications: () => 
    api.get('/company/applications'),
  
  updateApplicationStatus: (applicationId, status, interviewSchedule = null, selectionResult = null) => 
    api.put(`/company/applications/${applicationId}/status`, { 
      status, 
      interview_schedule: interviewSchedule,
      selection_result: selectionResult 
    })
}

// ============================================
// DRIVE API (Shared)
// ============================================
export const driveAPI = {
  getAllDrives: (params = {}) => 
    api.get('/drive', { params }),
  
  getDriveDetails: (driveId) => 
    api.get(`/drive/${driveId}`)
}

// ============================================
// Helper function to handle API responses
// ============================================
export const handleResponse = (response) => {
  if (response.data.success) {
    return response.data.data
  }
  throw new Error(response.data.message || 'Request failed')
}

export const handleError = (error) => {
  if (error.response) {
    // Server responded with error
    const message = error.response.data?.message || 'Server error occurred'
    const errors = error.response.data?.errors || []
    return { message, errors, status: error.response.status }
  } else if (error.request) {
    // Request made but no response
    return { message: 'No response from server. Please check your connection.', errors: [], status: 0 }
  } else {
    // Request setup error
    return { message: error.message || 'Request failed', errors: [], status: 0 }
  }
}

export default api