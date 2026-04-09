<template>
  <div >
    <Navbar v-if="showNavbar" />
    <Modal v-if = 'showModal'/>
    
    <div class="side">
      <Sidebar v-if="showSidebar" />
      
        <router-view />
      
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/common/Navbar.vue'
import Sidebar from '@/components/common/Sidebar.vue'
import Modal from '@/components/common/Modal.vue'


export default {
  name: 'Layout',
  components: { Navbar, Sidebar,Modal },
  computed: {
    showNavbar() {
      return this.$route.meta.showNavbar !== false
    },
    showModal(){
      return this.$route.meta.showModal !== false
    },
    showSidebar() {
      // const role = localStorage.getItem('userRole')
      return this.$route.meta.showSidebar !== false 
      // && role && role !== 'guest'
    }
  }
}
</script>

<style scoped>

.side{
  display: flex;
  justify-content: space-between;
  gap: 40px;
}
</style>