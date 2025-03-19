<script>
    import { onMount } from 'svelte';
    import { page } from '$app/stores';
    import { goto } from '$app/navigation';


    //all # are placeholders to pages other teams are making. 
  
    // We'll read the chosen role from the URL query string (?role=analyst or ?role=lead_analyst)
    let role = '';
    let isLead = false;
  
    // For demonstration, we hardcode a "userId" or you might store it in a session.
    let userId = 2; // Suppose user #2 is a lead_analyst in your stubs
  
    // Example projects data (in real usage, you'd fetch from your backend)
    let projects = [
      { id: 1, name: 'Project Alpha' },
      { id: 2, name: 'Project Beta' }
    ];
  
    // On component mount, determine the role from the URL,
    // then optionally verify permissions with your Role Manager
    $: roleParam = $page.url.searchParams.get('role');
  
    onMount(async () => {
      role = roleParam || 'analyst'; // default to 'analyst' if not specified
  
      // Option 1: If you trust the query param, just check if it's 'lead_analyst'
      isLead = (role === 'lead_analyst');
  
      // Option 2: Stubbed check via Role Manager backend
      // e.g., call your FastAPI /role_manager/authorize_action endpoint:
      /*
      const action = 'MANAGE_PROJECTS'; 
      const res = await fetch(`http://localhost:8000/role_manager/authorize_action?user_id=${userId}&action=${action}`, { 
        method: 'POST'
      });
      const data = await res.json();
      isLead = data.authorized; // If authorized is true, user can do lead operations
      */
    });
  
    // Action handlers (stubbed with alerts)
    async function runScan(projectId) {
      try {
        const response = await fetch("http://127.0.0.1:8000/analysts/execute_scan", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ analyst_id: 1, project_id: projectId })  // Hardcoded analyst_id=1 for now
        });

        if (!response.ok) throw new Error("Scan failed");

        const data = await response.json();
        alert(`Scan started! ID: ${data.scan_id}`);
      } catch (error) {
        console.error("Error starting scan:", error);
        alert("Failed to start scan.");
      }
    }
  
    function lockProject(projectId) {
      alert(`Lock Project clicked for project ID: ${projectId}`);
      // In real usage, call your backend endpoint
    }
  
    function deleteProject(projectId) {
      const confirmed = confirm(`Are you sure you want to delete project ID: ${projectId}?`);
      if (confirmed) {
        // Remove from local array for demonstration; later call your backend
        projects = projects.filter(p => p.id !== projectId);
      }
    }
  
    function createNewProject() {
      alert('Create New Project button clicked!');
      // Later, open a modal or redirect to a project creation form
    }

    let scanResults = {};

    async function viewScanResults() {
        try {
            const response = await fetch("http://127.0.0.1:8000/analysts/1/results/");
            if (!response.ok) throw new Error("Failed to fetch scan results");

            scanResults = await response.json();
        } catch (error) {
            console.error("Error fetching scan results:", error);
            alert("Failed to retrieve scan results.");
        }
    }

  </script>
  
  <main class="page-container">
    <!-- Sidebar -->
    <aside class="sidebar">
      <div class="logo">
        <h2>TRACE</h2>
      </div>
      <nav>
        <ul>
          <li><a href="#">Dashboard</a></li>
          <li class="active"><a href="#">Projects</a></li>
          <li><a href="#">Reports</a></li>
          <li><a href="#">Settings</a></li>
        </ul>
      </nav>
    </aside>
  
    <!-- Main Content -->
    <div class="main-content">
      <!-- Header -->
      <header class="header">
        <h1>Project Selection</h1>
        {#if isLead}
          <button class="create-btn" on:click={createNewProject}>+ Create new</button>
        {/if}
      </header>
  
      <!-- Recent Projects Section (for demonstration) -->
      <section class="recent-projects">
        <h2>Recent Projects</h2>
        <div class="recent-projects-cards">
          {#each projects as proj}
            <div class="project-card">
              <h3>{proj.name}</h3>
              <!-- In a real app, include more details such as date and lead analyst -->
            </div>
          {/each}
        </div>
      </section>
  
      <!-- All Projects Section -->

      <section class="scan-results">
        <h2>Scan Results</h2>
        <button on:click={viewScanResults}>View Scan Results</button>

        {#if Object.keys(scanResults).length > 0}
          <ul>
            {#each Object.entries(scanResults) as [scanId, result]}
              <li><strong>Scan {scanId}:</strong> {result}</li>
            {/each}
          </ul>
        {/if}
      </section>

      <section class="all-projects">
        <h2>All Projects</h2>
        <table>
          <thead>
            <tr>
              <th>Project Name</th>
              <th>Actions</th>
              {#if isLead}
                <th>Lead Analyst Actions</th>
              {/if}
            </tr>
          </thead>
          <tbody>
            {#each projects as proj}
              <tr>
                <td>{proj.name}</td>
                <td>
                  <button on:click={() => runScan(proj.id)}>Run Scan</button>
                </td>
                {#if isLead}
                  <td>
                    <button on:click={() => lockProject(proj.id)}>Lock/Unlock</button>
                    <button on:click={() => deleteProject(proj.id)}>Delete</button>
                  </td>
                {/if}
              </tr>
            {/each}
          </tbody>
        </table>
      </section>
    </div>
  </main>
  
  <style>
    /* Basic reset */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    body, html {
      font-family: Arial, sans-serif;
      height: 100%;
      width: 100%;
    }
    .page-container {
      display: flex;
      min-height: 100vh;
    }
    /* Sidebar */
    .sidebar {
      background-color: #f5f5f5;
      width: 220px;
      padding: 1rem;
    }
    .logo {
      text-align: center;
      margin-bottom: 2rem;
    }
    .logo h2 {
      color: #333;
      font-size: 1.5rem;
    }
    nav ul {
      list-style: none;
    }
    nav ul li {
      margin-bottom: 1rem;
    }
    nav ul li a {
      color: #555;
      text-decoration: none;
      font-weight: 500;
    }
    nav ul li.active a {
      font-weight: bold;
      color: #000;
    }
    /* Main Content */
    .main-content {
      flex: 1;
      padding: 2rem;
      background-color: #fff;
    }
    /* Header */
    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2rem;
    }
    .header h1 {
      font-size: 1.5rem;
    }
    .create-btn {
      background-color: #2684FF;
      color: #fff;
      border: none;
      padding: 0.6rem 1rem;
      border-radius: 4px;
      cursor: pointer;
    }
    .create-btn:hover {
      background-color: #0f66cc;
    }
    /* Recent Projects */
    .recent-projects {
      margin-bottom: 2rem;
    }
    .recent-projects-cards {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
    }
    .project-card {
      border: 1px solid #ddd;
      border-radius: 4px;
      padding: 1rem;
      width: 220px;
      background-color: #fafafa;
    }
    .project-card h3 {
      margin-bottom: 0.5rem;
      font-size: 1rem;
    }
    /* All Projects */
    .all-projects {
      margin-bottom: 2rem;
    }
    table {
      width: 100%;
      border-collapse: collapse;
    }
    thead {
      background-color: #f5f5f5;
    }
    th, td {
      padding: 0.8rem;
      border: 1px solid #eee;
      text-align: left;
    }
    td button {
      margin-right: 0.5rem;
      background-color: #2684FF;
      color: #fff;
      border: none;
      padding: 0.4rem 0.6rem;
      border-radius: 4px;
      cursor: pointer;
      font-size: 0.85rem;
    }
    td button:nth-child(2) {
      background-color: #777;
    }
    td button:nth-child(3) {
      background-color: #D9534F;
    }
    td button:hover {
      opacity: 0.9;
    }
  </style>
  