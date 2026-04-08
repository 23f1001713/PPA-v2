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
      <h1>Company Management </h1>
    </div>
    <div class="nav">
    <form >
        <div class="search">
            <input type="text" placeholder="Search companies..." name="search">
        
        <input style="background-color: blue; color: white;" class="btn btn-outline-success" type="submit" value="Search">
        </div>
    </form>

</div>
<div class="stats ">
    <div class="stat hov">
        <div class="stat-number">10</div>
        <div class="stat-label">Total Companies</div>
    </div>
    <div class="stat applied hov">
        <div class="stat-number">10</div>
        <div class="stat-label">Total Drives</div>
    </div>
    <div class="stat shortlisted hovr">
        <div class="stat-number">10</div>
        <div class="stat-label">Applications</div>
    </div>
<div class="stat shortlisted hovr">
        <div style="color: red;" class="stat-number">10</div>
        <div class="stat-label">Blacklisted</div>
    </div>

</div>
<div id="tableView">
    <table class="app-tab">
        <thead>
            <tr>

                <th>Company ID</th>
                <th>Company Name</th>
                <th>Total Drives</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            
            <tr>


                <td><strong>1</strong></td>
                <td>
                    <div class="s-cell">

                        <div class="stud-deta">
                            <div class="stud-name">Akash Maurya</div>

                        </div>
                    </div>
                </td>

                <td>
                    <div class="d-info">
                        
                        <div class="drive-title-sm">5</div>

                    </div>
                </td>

                <td>

                    <span class="status-badge status-selected">Approved</span>

                    
                    <span class="status-badge status-shortlisted">Blocked</span>

                    

                </td>
                <td>
                    <div class="t-a">
                        <a href="#">
                            
                            <button style="background-color: #28a745; color: white;" class="btn-sm btn-view">
                                <i class="bi bi-unlock"></i> Unblock
                            </button>
                           
                            <button style="background-color: #dc3545; color: white;" class="btn-sm btn-view">
                                <i class="bi bi-slash-circle"></i> Block
                            </button>
                          
                        </a>
                        <a href="#">
                            <button class="btn-sm btn-view">
                                <i class="bi bi-eye"></i> View Details
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

<script>
export default {
  name: 'ManageCompanies'
}
</script>