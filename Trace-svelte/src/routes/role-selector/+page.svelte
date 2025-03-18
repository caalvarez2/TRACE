<script>
    import { goto } from '$app/navigation';
  
    // Let the user choose between "analyst" or "lead_analyst"
    // and redirect them to the Projects page with that role.
    function selectRole(role) {
      // Example: pass the chosen role as a query parameter to the /projects route
      goto(`/projects?role=${role}`);
    }
  </script>
  
  <main class="selector-container">
    <h1>Select Your Role</h1>
    <div class="role-buttons">
      <button on:click={() => selectRole('analyst')}>
        Analyst
      </button>
      <button on:click={() => selectRole('lead_analyst')}>
        Lead Analyst
      </button>
    </div>
  </main>
  
  <style>
    .selector-container {
      text-align: center;
      margin-top: 5rem;
    }
    .role-buttons {
      margin-top: 2rem;
    }
    button {
      margin: 0 1rem;
      padding: 0.6rem 1.2rem;
      background-color: #2684FF;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      opacity: 0.9;
    }
  </style>
  