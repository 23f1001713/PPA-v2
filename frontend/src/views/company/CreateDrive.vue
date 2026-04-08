<style scoped>
.main-container{
  margin: 10px 300px;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
.form-container {
            width: 800px;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
.form-group {
            margin-bottom: 10px;
            margin-left: 100px;
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
            width: 550px;
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
.btn{
  padding: 10px 20px;
  margin: 20px 0 0 200px;
}
</style>

<template>
  <div class="main-container">
    <div class="form-container">
            <h3 class="mb-4 text-center">Create New Placement Drive</h3>

            <form action="" method="POST">


                <div class="form-group">
                    <label for="jobTitle" class="form-label fw-bold">Job Title</label>
                    <input type="text" class="form-control" id="jobTitle" name="job_title" maxlength="100"
                        placeholder="e.g., Junior Software Engineer" required>
                </div>

                <div class="form-group">
                    <label for="description" class="form-label fw-bold">Job Description</label>
                    <textarea class="form-control" id="description" name="description" rows="3" maxlength="200"
                        placeholder="Briefly describe the role..." required></textarea>
                    <div class="form-text text-end">Max 200 characters</div>
                </div>

                <div class="form-group">
                    <label for="eligibility" class="form-label fw-bold">Eligibility Criteria</label>
                    <input type="text" class="form-control" id="eligibility" name="eligibility" maxlength="100"
                        placeholder="e.g., B.Tech CSE, Min 7.5 CGPA" required>
                </div>

                <div class="form-group">
                    <label for="deadline" class="form-label fw-bold">Application Deadline</label>
                    <input type="datetime-local" class="form-control" id="deadline" name="deadline" required>
                </div>



                <div class="form-group">
                  
                    <button type="submit" class="btn">Create Drive</button>
                </div>

            </form>
        </div>

  </div>
</template>

<script>
export default {
  name: 'CreateDrive'
}
</script>