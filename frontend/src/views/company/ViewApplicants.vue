<style scoped>
.main-container{
  margin: 10px 200px;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
.sec-card {
            background: white;
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            margin-bottom: 30px;
            width: 1000px;
        }

        .sec-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 25px;
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
.app-list {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .app-card {
            background: #f8f9fa;
            border-radius: 12px;
            padding: 18px;
            transition: all 0.3s ease;
            border-left: 4px solid blue;
        }

        .app-card:hover {
            background: white;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            transform: translateX(5px);
        }

        .app-h {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 10px;
        }
.app-i {
            flex: 1;
        }

        .app-n {
            font-weight: 700;
            color: #2d3436;
            font-size: 1rem;
            margin-bottom: 3px;
        }

        .app-d {
            font-size: 0.85rem;
            color: #636e72;
        }

        .app-b {
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
        }

        .badge-new {
            background: #e8f4ff;
            color: #0984e3;
        }

        .app-m {
            display: flex;
            gap: 20px;
            margin-top: 10px;
            font-size: 0.85rem;
            color: #636e72;
        }

        .app-m-i {
            display: flex;
            align-items: center;
            gap: 5px;
        }

        .app-m-i i {
            color: #667eea;
        }
.app {
        background: rgba(255, 255, 255, 0.2);
    }

    a {
        text-decoration: none;
    }

    .status-applied {
        background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
        margin: 1px;
        padding-top: 5px;
        padding: 5px;
        border-radius: 12px;
        color: white;
        border: 2px solid blue;
    }

    .status-shortlisted {
        background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%);
        color: #2d3436;
        margin: 1px;
        padding-top: 5px;
        padding: 5px;
        border-radius: 12px;
        border: 2px solid blue;
    }

    .status-selected {
        background: linear-gradient(135deg, #55efc4 0%, #00b894 100%);
        color: white;
        margin: 1px;
        padding-top: 5px;
        padding: 5px;
        border: 2px solid blue;
        border-radius: 12px;
    }

    .status-rejected {
        background: linear-gradient(135deg, #fab1a0 0%, #ff7675 100%);
        color: white;
        margin: 1px;
        padding-top: 5px;
        padding: 5px;
        border: 2px solid blue;
        border-radius: 12px;
    }
    .drive-actions{
         margin-top: 20px;
    }
.btn-action {
            flex: 1;
            padding: 10px 18px;
            border-radius: 8px;
            border: none;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            gap: 6px;
            font-size: 0.9rem;
        }

        .btn-view {
            background-color: blue;
            color: white;
            margin: 5px 10px;
        }

        .btn-view:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .btn-edit {
            background: white;
            color: blue;
            border: 2px solid blue;
            margin: 0 10px 0 0;
        }

        .btn-edit:hover {
            background: #667eea;
            color: white;
        }


</style>


<template>
  <div class="main-container">
    <div class="sec-card">
        <div class="sec-header">
            <h2>
                <i class="bi bi-people-fill icon"></i>
                All Applicants
            </h2>

        </div>
       
        <div class="app-list">



            <div class="app-card">
                <div class="app-h">

                    <div class="app-i">
                        <div class="app-n">Name </div>
                        <div class="app-d">Branch • CGPA </div>
                    </div>

                   
                    <button class="status-applied">

                        Status : Pending
                    </button>
                   
                    <button class="status-shortlisted">

                        Status : Shortlisted
                    </button>
                   
                    <button class="status-rejected">

                        Status : Rejected
                    </button>
                  
                    <button class="status-selected">

                        Status : Selected
                    </button>
                   
                </div>
                <div class="app-m">

                    <div class="app-m-i">
                        <i class="bi bi-briefcase"></i>
                        <span><span>Job Title </span></span>
                    </div>
                    <div class="app-m-i">
                        <i class="bi bi-star-fill"></i>
                        <span>CGPA:  </span>
                    </div>

                </div>
                <div class="drive-actions">
                    <a href="">
                        <button class="btn-action btn-view">
                            <i class="bi bi-people"></i>
                            Shortlist
                        </button>
                    </a>
                    <a href="">
                        <button class="btn-action btn-edit">

                            Select
                        </button>
                    </a>
                    <a href="">
                        <button class="btn-action btn-edit">

                            Pending
                        </button>
                    </a>
                    <a href="">
                        <button class="btn-action btn-edit">

                            Reject
                        </button>
                    </a>
                </div>

            </div>
        </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'ViewApplicants'
}
</script>