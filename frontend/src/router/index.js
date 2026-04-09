import { createRouter, createWebHistory } from 'vue-router'
import Layout from '@/views/Layout.vue'
import LandingPage from '../views/shared/LandingPage.vue'


// Auth Views
import Login from '@/views/auth/Login.vue'
import StudentRegister from '@/views/auth/StudentRegister.vue'
import CompanyRegister from '@/views/auth/CompanyRegister.vue'

// Admin Views
import AdminDashboard from '@/views/admin/AdminDashboard.vue'
import CompanyApproval from '@/views/admin/CompanyApproval.vue'
import DriveApproval from '@/views/admin/DriveApproval.vue'
import ManageStudents from '@/views/admin/ManageStudents.vue'
import ManageCompanies from '@/views/admin/ManageCompanies.vue'
import ReportsDashboard from '@/views/admin/ReportsDashboard.vue'
import MonthlyReport from '@/views/admin/MonthlyReport.vue'

// Student Views
import StudentDashboard from '@/views/student/StudentDashboard.vue'
import AvailableDrives from '@/views/student/AvailableDrives.vue'
import MyApplications from '@/views/student/MyApplications.vue'
import PlacementHistory from '@/views/student/PlacementHistory.vue'
import StudentProfile from '@/views/student/StudentProfile.vue'
import ExportHistory from '@/views/student/ExportHistory.vue'

// Company Views
import CompanyDashboard from '@/views/company/CompanyDashboard.vue'
import CompanyProfile from '@/views/company/CompanyProfile.vue'
import CreateDrive from '@/views/company/CreateDrive.vue'
import ManageDrives from '@/views/company/ManageDrives.vue'
import ViewApplicants from '@/views/company/ViewApplicants.vue'
import ShortlistStudents from '@/views/company/ShortlistStudents.vue'
import InterviewSchedule from '@/views/company/InterviewSchedule.vue'

// Shared Views

import DriveDetails from '@/views/shared/DriveDetails.vue'
import SearchResults from '@/views/shared/SearchResults.vue'
import NotFound from '@/views/shared/NotFound.vue'






const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes:[
  {
    path: '/',
    name: 'Landing',
    component: LandingPage,
    meta: { showNavbar: true, showSidebar: false, showFooter: false }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { showNavbar: false, showSidebar: false, showFooter: false }
  },
  {
    path: '/register/student',
    name: 'StudentRegister',
    component: StudentRegister,
    meta: { showNavbar: false, showSidebar: false, showFooter: false }
  },
  {
    path: '/register/company',
    name: 'CompanyRegister',
    component: CompanyRegister,
    meta: { showNavbar: false, showSidebar: false, showFooter: false }
  },
  {
    path: '/',
    component: Layout,
    meta: { requiresAuth: true },
    children: [
      // Admin Routes
      {
        path: '/admin/dashboard',
        name: 'AdminDashboard',
        component: AdminDashboard,
        meta: { role: 'ADMIN', showSidebar: true ,showFooter: false , showNavbar:false , showModal:false}
      },
      {
        path: '/admin/applications',
        name: 'CompanyApproval',
        component: CompanyApproval,
        meta: { role: 'ADMIN', showSidebar: true ,showFooter: false , showNavbar:false , showModal:false}
      },
      {
        path: '/admin/drives',
        name: 'DriveApproval',
        component: DriveApproval,
        meta: { role: 'ADMIN', showSidebar: true,showFooter:false , showNavbar:false,showModal:false }
      },
      {
        path: '/admin/students',
        name: 'ManageStudents',
        component: ManageStudents,
        meta: { role: 'ADMIN', showSidebar: true,showFooter:false , showNavbar:false,showModal:false }
      },
      {
        path: '/admin/companies',
        name: 'ManageCompanies',
        component: ManageCompanies,
        meta: { role: 'ADMIN', showSidebar: true,showFooter:false , showNavbar:false , showModal:false }
      },
      {
        path: '/admin/reports',
        name: 'ReportsDashboard',
        component: ReportsDashboard,
       meta: { role: 'ADMIN', showSidebar: true ,showFooter: false , showNavbar:false , showModal:false}
      },
      {
        path: '/admin/reports/monthly',
        name: 'MonthlyReport',
        component: MonthlyReport,
        meta: { role: 'ADMIN', showSidebar: true }
      },
      
      // Student Routes
      {
        path: '/student/dashboard',
        name: 'StudentDashboard',
        component: StudentDashboard,
        meta: { role: 'STUDENT', showSidebar: false,showNavbar:true , showFooter:false , showModal:false }
      },
      {
        path: '/student/drives',
        name: 'AvailableDrives',
        component: AvailableDrives,
        meta: { role: 'STUDENT', showSidebar: false,showNavbar:true , showFooter:false, showModal:false }
      },
      {
        path: '/student/applications',
        name: 'MyApplications',
        component: MyApplications,
        meta: { role: 'STUDENT', showSidebar: false,showNavbar:true , showFooter:false , showModal:false}
      },
      {
        path: '/student/history',
        name: 'PlacementHistory',
        component: PlacementHistory,
        meta: { role: 'STUDENT', showSidebar: false,showNavbar:true , showFooter:false , showModal:false}
      },
      {
        path: '/student/profile',
        name: 'StudentProfile',
        component: StudentProfile,
        meta: { role: 'STUDENT', showSidebar: false,showNavbar:true , showFooter:false , showModal:false}
      },
      {
        path: '/student/export',
        name: 'ExportHistory',
        component: ExportHistory,
        meta: { role: 'STUDENT', showSidebar: false,showNavbar:true , showFooter:false, showModal:false }
      },
      
      // Company Routes
      {
        path: '/company/dashboard',
        name: 'CompanyDashboard',
        component: CompanyDashboard,
        meta: { role: 'COMPANY', showSidebar: false ,showModal:true , showNavbar:false , showFooter:false }
      },
      {
        path: '/company/profile',
        name: 'CompanyProfile',
        component: CompanyProfile,
        meta: { role: 'COMPANY', showSidebar: false ,showModal:true , showNavbar:false , showFooter:false }
      },
      {
        path: '/company/drives/create',
        name: 'CreateDrive',
        component: CreateDrive,
       meta: { role: 'COMPANY', showSidebar: false ,showModal:true , showNavbar:false , showFooter:false }
      },
      {
        path: '/company/drives',
        name: 'ManageDrives',
        component: ManageDrives,
        meta: { role: 'COMPANY', showSidebar: false ,showModal:true , showNavbar:false , showFooter:false }
      },
      {
        path: '/company/applications',
        name: 'ViewApplicants',
        component: ViewApplicants,
        meta: { role: 'COMPANY', showSidebar: false ,showModal:true , showNavbar:false , showFooter:false }
      },
      {
        path: '/company/drives/:driveId/shortlist',
        name: 'ShortlistStudents',
        component: ShortlistStudents,
        meta: { role: 'COMPANY', showSidebar: false ,showModal:true , showNavbar:false , showFooter:false }
      },
      {
        path: '/company/drives/:driveId/interviews',
        name: 'InterviewSchedule',
        component: InterviewSchedule,
        meta: { role: 'COMPANY', showSidebar: false ,showModal:true , showNavbar:false , showFooter:false }
      },
      
      // Shared Routes
      {
        path: '/drives/:driveId',
        name: 'DriveDetails',
        component: DriveDetails,
        meta: { showSidebar: true }
      },
      {
        path: '/search',
        name: 'SearchResults',
        component: SearchResults,
        meta: { showSidebar: true }
      }
    ]
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: NotFound,
    meta: { showNavbar: true, showSidebar: false, showFooter: false }
  },
]

})
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('user_token');
  const userRole = localStorage.getItem('user_role');

  // If the route requires login
  if (to.meta.requiresAuth && !token) {
    next('/login');
  } 
  // If the route requires a specific role
  else if (to.meta.role && to.meta.role !== userRole) {
    alert("Access Denied: You don't have the right permissions.");
    next('/'); // Send back to home or a 403 page
  } 
  else {
    next();
  }
});

export default router
