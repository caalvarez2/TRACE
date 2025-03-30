<script lang="ts">
  import { goto } from '$app/navigation';

  function goToRoleSelector() {
    goto('/role-selector');
  }
</script>

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

  /* Overall page container */
  .page {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }

  /* Top Navigation Bar */
  .top-nav {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    padding: 1rem 2rem;
    background-color: #f9f9f9;
  }

  .top-nav a {
    margin-left: 1.5rem;
    text-decoration: none;
    color: #333;
    font-weight: 500;
  }

  /* Hero Section */
  .hero {
    flex: 1;
    position: relative;
    padding: 3rem 2rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    overflow: hidden;
  }

  .hero h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
    font-weight: bold;
  }

  .hero p {
    max-width: 600px;
    font-size: 1rem;
    color: #555;
    margin-bottom: 2rem;
    line-height: 1.5;
  }

  .hero button {
    background-color: #4ea8b2; /* START button color */
    color: #fff;
    border: none;
    padding: 0.8rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
  }

  .hero button:hover {
    background-color: #3b8991;
  }
</style>

<div class="page">
  <!-- Top Navigation -->
  <nav class="top-nav">
    <a href="#">Dashboard</a>
    <a href="#">Settings</a>
  </nav>

  <!-- Hero Section -->
  <section class="hero">
    <h1>Elevate Your Security Strategy with TRACE</h1>
    <p>
      A Cybersecurity Platform to Protect Your Digital Assets. Detect Vulnerabilities,
      Strengthen Defense, and Secure Your Network Seamlessly. Gain Real-Time Insights
      and Proactive Protection.
    </p>
    <button on:click={goToRoleSelector}>START</button>
  </section>
</div>
