<style scoped>
.main-container{
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  margin-left: 300px;
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



</style>

<template>
  <div class="main-container">
    <div class="header">
      <h1>Admin Dashboard</h1>
    </div>

    <div class="stats">
    <div class="stat hov">
        <div class="stat-number">10</div>
        <div class="stat-label">Total Applications</div>
    </div>
    <div class="stat hov applied">
        <div class="stat-number">10</div>
        <div class="stat-label">Total Student</div>
    </div>
    <div class="stat hov shortlisted">
        <div class="stat-number">10</div>
        <div class="stat-label">Total Companies</div>
    </div>
    <div class="stat hovr selected">
        <div class="stat-number">10</div>
        <div class="stat-label"> Total Drives</div>
    </div>
    <div class="stat hovr rejected">
        <div style="color: red;" class="stat-number">10</div>
        <div class="stat-label">Pending Drives</div>
    </div>
    <div class="stat hovr rejected">
        <div style="color: red;" class="stat-number">10</div>
        <div class="stat-label">Pending Companies</div>
    </div>
    <div class="stat hovr rejected">
        <div style="color: red;" class="stat-number">10</div>
        <div class="stat-label">Blocked Students</div>
    </div>

</div>
  </div>
</template>

<script>
export default {
  name: 'AdminDashboard'
}
</script>