<script>
  import { goto } from '$app/navigation';
  let initials = '';

  // Redirect user to the /projects route with the selected role and initials (if any)
  function selectRole(role) {
    // Build query parameters based on the role and the initials input
    let query = `role=${role}`;
    if (initials.trim()) {
      query += `&initials=${encodeURIComponent(initials)}`;
    }
    goto(`/projects?${query}`);
  }
</script>

<main class="selector-container">
  <h1>Select Your Role</h1>
  <div class="initials-input">
    <p>Enter your initials:</p>
    <input type="text" bind:value={initials} placeholder="e.g., K.C" />
  </div>

  <div class="role-buttons">
    <button on:click={() => selectRole('analyst')}>Analyst</button>
    <button on:click={() => selectRole('lead_analyst')}>Lead Analyst</button>
  </div>
</main>

<style>
  /* Basic Reset + Global Font */
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
    background-color: #f0f1f1; /* Page background color */
  }

  .selector-container {
    text-align: center;
    margin-top: 5rem;
  }

  .selector-container h1 {
    margin-bottom: 2rem;
    font-size: 2rem;
    font-weight: bold;
  }

  .initials-input {
    margin-top: 2rem;
    margin-bottom: 2rem; /* Added padding between initials and buttons */
  }

  .initials-input p {
    margin-bottom: 0.5rem;
    font-size: 1rem;
  }

  .initials-input input {
    padding: 0.6rem;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    width: 200px;
  }

  .role-buttons {
    margin-bottom: 2rem;
  }

  button {
    margin: 0 1rem;
    padding: 0.6rem 1.2rem;
    background-color: #4ea8b2;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
  }

  button:hover {
    background-color: #3b8991;
  }
</style>