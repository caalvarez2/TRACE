<script>
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
  import { goto } from '$app/navigation';

  // Example data with additional fields:
  let projects = [
    {
      id: 1,
      name: 'Encrypted Communications Hub',
      lastEdit: 'Nov 4, 2024',
      leadAnalyst: 'S.I.',
      port: 49153
    },
    {
      id: 2,
      name: 'Military Drone Command Interface Scan',
      lastEdit: 'Nov 4, 2024',
      leadAnalyst: 'J.S.',
      port: 49154
    },
    {
      id: 3,
      name: 'Field Intelligence Data Platform',
      lastEdit: 'Nov 4, 2024',
      leadAnalyst: 'R.S.',
      port: 49155
    },
    {
      id: 4,
      name: 'Secure Satellite Control Panel Audit',
      lastEdit: 'Nov 4, 2024',
      leadAnalyst: 'L.T.',
      port: 49156
    }
  ];

<<<<<<< HEAD
  let role = '';
  let isLead = false;
  let openMenu = null; // track 3-dot menu

  // Retrieve the 'role' query param from the URL
  $: roleParam = $page.url.searchParams.get('role');

  onMount(() => {
    role = roleParam || 'analyst';
    isLead = (role === 'lead_analyst');
  });

  function runScan(projectId) {
    goto(`/runTools?role=${role}&projectId=${projectId}`);
  }

  function toggleMenu(projectId) {
    openMenu = (openMenu === projectId) ? null : projectId;
  }

  function lockProject(projectId) {
    alert(`Lock Project clicked for project ID: ${projectId}`);
  }

  function unlockProject(projectId) {
    alert(`Unlock Project clicked for project ID: ${projectId}`);
  }

  function createNewProject() {
    alert('Create New Project button clicked!');
  }
</script>

<main class="page-container">
  <!-- Sidebar -->
  <aside class="sidebar">
    <!-- Logo or Top Icon -->
    <div class="sidebar-top-icon">
      <!-- Example: Could be your app logo or an icon. Inline SVG used here as a placeholder. -->
      <svg viewBox="0 0 24 24" fill="currentColor" class="top-icon">
        <circle cx="12" cy="12" r="10" />
      </svg>
=======
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
>>>>>>> 61b665ba4397e093425a401bb4c98063af5b8acc
    </div>

    <!-- Navigation Icons -->
    <nav class="nav-icons">
      <!-- Example icons: folder, text snippet, trash -->
      <!-- Each anchor (or button) can link to a different route or function -->
      <a href="#" class="icon-link" title="Projects">
        <!-- Folder Icon (placeholder SVG) -->
        <svg viewBox="0 0 24 24" fill="currentColor" class="nav-icon">
          <path d="M10 4H4C2.9 4 2 4.9 2 6v12c0 
                   1.1.9 2 2 2h16c1.1 0 2-.9 
                   2-2V8c0-1.1-.9-2-2-2h-8l-2-2z" />
        </svg>
      </a>
      <a href="#" class="icon-link" title="Text Snippet">
        <!-- Text Snippet Icon (placeholder SVG) -->
        <svg viewBox="0 0 24 24" fill="currentColor" class="nav-icon">
          <path d="M3 3v18h18V3H3zm2 
                   2h14v14H5V5zm3 
                   3h8v2H8V8zm0 
                   4h5v2H8v-2z" />
        </svg>
      </a>
      <a href="#" class="icon-link" title="Trash">
        <!-- Trash Icon (placeholder SVG) -->
        <svg viewBox="0 0 24 24" fill="currentColor" class="nav-icon">
          <path d="M9 3v1H4v2h16V4h-5V3H9zm-2 
                   6v12c0 1.1.9 2 2 
                   2h6c1.1 0 2-.9 
                   2-2V9H7z" />
        </svg>
      </a>
    </nav>

    <!-- Bottom Icon (Optional) -->
    <div class="sidebar-bottom-icon">
      <!-- Example: Could be a settings or help icon -->
      <a href="#" class="icon-link" title="Settings">
        <svg viewBox="0 0 24 24" fill="currentColor" class="nav-icon">
          <path d="M19.14 12.936a7.053 7.053 0 0 
                   0 .04-.936 7.053 7.053 0 0 
                   0-.04-.936l2.11-1.64a.504.504 0 
                   0 0 .12-.63l-2-3.464a.5.5 0 0 
                   0-.61-.22l-2.49 1a7.16 7.16 0 
                   0 0-1.62-.94l-.38-2.65A.503.503 
                   0 0 0 12 2h-4a.5.5 0 0 0-.49.41l-.38 
                   2.65a7.16 7.16 0 0 0-1.62.94l-2.49-1a.5.5 
                   0 0 0-.61.22l-2 3.464a.505.505 0 0 
                   0 .12.63l2.11 1.64c-.03.3-.05.62-.05.94s.02.64.05.94l-2.11 
                   1.64a.504.504 0 0 0-.12.63l2 3.464a.5.5 0 0 0 
                   .61.22l2.49-1c.49.38 1.04.7 1.62.94l.38 
                   2.65a.5.5 0 0 0 .49.41h4a.503.503 0 0 
                   0 .49-.41l.38-2.65a7.16 7.16 0 0 0 
                   1.62-.94l2.49 1a.5.5 0 0 0 
                   .61-.22l2-3.464a.504.504 0 0 
                   0-.12-.63l-2.11-1.64zM10 15a3 
                   3 0 1 1 0-6 3 3 0 0 1 0 6z" />
        </svg>
      </a>
    </div>
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

    <!-- Recent Projects -->
    <section class="recent-projects">
      <h2>Recent Projects</h2>
      <div class="recent-projects-cards">
        {#each projects.slice(0, 2) as proj}
          <div class="project-card">
            <h3>{proj.name}</h3>
          </div>
        {/each}
      </div>
    </section>

    <!-- All Projects -->
    <section class="all-projects">
      <h2>All Projects</h2>
      <table>
        <thead>
          <tr>
            <th>Project Name</th>
            <th>Last Edit</th>
            <th>Lead Analyst</th>
          </tr>
        </thead>
        <tbody>
          {#each projects as proj}
            <tr>
              <td>{proj.name}</td>
              <td>{proj.lastEdit}</td>
              <td>{proj.leadAnalyst}</td>
              <td class="actions-cell">
                <button class="run-scan-btn" on:click={() => runScan(proj.id)}>
                  Run Scan
                </button>
                {#if isLead}
                  <div class="dots-menu">
                    <div class="dots-icon" on:click={() => toggleMenu(proj.id)}>
                      <span>...</span>
                    </div>
                    {#if openMenu === proj.id}
                      <div class="submenu">
                        <button on:click={() => lockProject(proj.id)}>
                          Lock Project
                        </button>
                        <button on:click={() => unlockProject(proj.id)}>
                          Unlock Project
                        </button>
                      </div>
                    {/if}
                  </div>
                {/if}
              </td>
            </tr>
          {/each}
        </tbody>
      </table>
    </section>
  </div>
</main>

<style>
  /* Global Reset & Font */
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  html, body {
    height: 100%;
    width: 100%;
    background-color: #f0f1f1;
  }

  .page-container {
    display: flex;
    min-height: 100vh;
  }

  /* SIDEBAR */
  .sidebar {
    /* Make it narrower to focus on icons */
    width: 60px;
    background-color: #f5f5f5;
    display: flex;
    flex-direction: column;
    justify-content: space-between; /* space top icon, nav icons, bottom icon */
    align-items: center;
    padding: 1rem 0;
  }

  /* Example top icon (logo area) */
  .sidebar-top-icon {
    margin-bottom: 1rem;
  }
  .top-icon {
    width: 40px;
    height: 40px;
    color: #4ea8b2; /* example color */
  }

  /* Navigation icons in the middle */
  .nav-icons {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .icon-link {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    color: #666;
    text-decoration: none;
    cursor: pointer;
  }

  .icon-link:hover {
    background-color: #e9e9e9;
  }

  .nav-icon {
    width: 24px;
    height: 24px;
  }

  /* Bottom icon (optional) */
  .sidebar-bottom-icon {
    margin-top: 1rem;
  }

  /* MAIN CONTENT */
  .main-content {
    flex: 1;
    padding: 2rem;
    background-color: #fff;
  }

  /* HEADER */
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
    background-color: #4ea8b2;
    color: #fff;
    border: none;
    padding: 0.6rem 1rem;
    border-radius: 4px;
    cursor: pointer;
  }
  .create-btn:hover {
    background-color: #3b8991;
  }

  /* RECENT PROJECTS */
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

  /* ALL PROJECTS */
  .all-projects {
    margin-bottom: 2rem;
  }
  table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0 8px;
  }
  thead {
    background-color: #ffffff;
    font-size: 10pt;
    color: #63656c;
  }
  th, td {
    border: none;
    text-align: left;
    padding: 0.8rem;
  }
  tbody tr {
    background-color: #e1e1e1;
    border-radius: 12px;
  }
  .actions-cell {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 1rem;
    position: relative;
  }
  .run-scan-btn {
    background-color: #4ea8b2;
    color: #fff;
    border: none;
    padding: 0.4rem 0.6rem;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.85rem;
  }
  .run-scan-btn:hover {
    background-color: #3b8991;
  }

  /* DOTS MENU */
  .dots-menu {
    position: relative;
  }
  .dots-icon {
    cursor: pointer;
    padding: 0.4rem;
    border-radius: 4px;
    color: #666;
  }
  .dots-icon:hover {
    background-color: #e9e9e9;
  }
  .submenu {
    position: absolute;
    top: 2rem;
    right: 0;
    background: #fff;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 0.4rem;
    display: flex;
    flex-direction: column;
    width: 120px;
    z-index: 10;
  }
  .submenu button {
    background: none;
    border: none;
    color: #333;
    text-align: left;
    padding: 0.4rem;
    font-size: 0.85rem;
    cursor: pointer;
    border-radius: 4px;
  }
  .submenu button:hover {
    background-color: #f5f5f5;
  }
</style>
